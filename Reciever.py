from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
from ShareChat.component.chat_message import ChatMessage
from ShareChat.entity.config_entity import SharingConfig
from ShareChat.entity.config_entity import MessageConfig
from ShareChat.component.Text_file_Process import TextFileProcess
from ShareChat import utils
import os,sys,socket,time

#creating Instance of the classes
Chat_msg_obj = ChatMessage()
path_obj = SharingConfig()
message_config_obj = MessageConfig()
artifact_dir_path = path_obj.artifact_dir
textfile_class_obj = TextFileProcess()


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 



my_ip="0.0.0.0"
my_port=1005
my_address=(my_ip,my_port)
s.bind(my_address)
image_temp = 0
while True :
    if image_temp == 0:  # condition due to only image sharing
        recieved_data = s.recvfrom(65000)
        message , ip_address , port = Chat_msg_obj.filter_message_address(RecieveDat=recieved_data)
        Data_label = utils.Data_identifier(Recieve_data_message=message) # to identifie the data


    if Data_label == "message":
        try:
            logging.info('Dealing with message...')
            time.sleep(2)

            #file handling to save the Data of messaging
            message_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'chat_message')
            os.makedirs(message_artifact_path_with_ip, exist_ok=True)


            message_file_path = os.path.join(message_artifact_path_with_ip , message_config_obj.message_file_name)
            logging.info(f"writing message in Database !")
            with open(message_file_path,'a+') as message_file:
                message_file.write('\n'+message[1:])

        except Exception as e:
            raise ShareChatException(e,sys)

    elif Data_label == 'text-file':
        try:

            textfile_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'text_files')
            print(textfile_artifact_path_with_ip)
            text_data = message
            textfile_class_obj.Data_resampling_write(Recieve_data = text_data , writing_path= textfile_artifact_path_with_ip)
            logging.info(f"successfully recieved the Text-file !")
        except Exception as e:
            raise ShareChatException(e,sys)


    else:
        try:
            # <<<<< CODE TO PREPARE SAVE FILE PATH >>>>>>
            image_dir_file_path = os.path.join(artifact_dir_path,ip_address,'Images')
            os.makedirs(image_dir_file_path,exist_ok=True)

            # <<<<<<<<<< GET FILE NAME FROM FIRST PACKET OF DATA   >>>>>>>>>>>
            Data_label = message[0:1]
            file_name_with_extension = message[1:message.find(b'|')]
            first_data_packet = Data = message[message.find(b'|')+1:]
            image_file_path = os.path.join(image_dir_file_path,str(file_name_with_extension)[2:-1])          # <<<<<<<< FILE NAME DECODING ERROR

            if image_temp == 0:
                with open(image_file_path,'ab') as file:
                    file.write(first_data_packet)
                    image_temp +=1
                    continue   # to skip further lines of code in a first iteration

            if image_temp == 1 :
                try:
                    recieved_data = s.recvfrom(65000)
                    image_file_path = os.path.join(image_dir_file_path,str(file_name_with_extension)[2:-1])          # <<<<<<<< FILE NAME DECODING ERROR
                    with open(image_file_path,'ab') as file:
                        file.write(recieved_data[0])

                except Exception as e:
                    raise ShareChatException(e,sys)

            logging.info('Dealing with image..')
        except Exception as e:
            raise ShareChatException(e,sys)
    
