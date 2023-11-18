import os, sys, socket
from ShareChat.logger import logging
from ShareChat.exception import ShareChatException
from ShareChat.component.Text_file_Process import TextFileProcess
from ShareChat.component.Image_Process import ImageSender
from PIL import Image
import numpy as np 
textfile_processObj = TextFileProcess()
img_sender_obj = ImageSender()

# establishing connection with UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 


target_ip="127.0.0.1"
target_port=1005
final_target=(target_ip,target_port)

title_message="""
What do you want to share ?
0    ---->  MESSAGE
1    ---->  TEXT-FILE
2    ---->  IMAGE"""
print(title_message)
task_choice = input('Plz enter your choice :- ')
print()

if task_choice == '0':
    try:
        logging.info(f"we are sending message to :- {final_target}")
        break_condition = True
        while break_condition:
            msg=input("Plz enter your message : ")
            if msg :
                msg = '0'+msg
                encrepted_message=msg.encode('ascii')
                s.sendto(encrepted_message,final_target)
            else:
                break_condition = False
    except Exception as e:
        raise ShareChatException(e,sys)


elif task_choice == '1':
    try:
        Data_file_path = input('Plz paste your file path ... ')
        encrypted_file_data_with_label = textfile_processObj.Data_sampling(file_path= Data_file_path)
        s.sendto(encrypted_file_data_with_label,final_target)
        logging.info(f"Text-file Data has been successfully sent to :- {final_target}")

    except Exception as e:
        raise ShareChatException(e,sys)
        
else:
    #images
    try:
        
        logging.info(f"We are sending Image !")
        image_path = input('Plz past image url path :- ')
        file_name_with_extension = os.path.basename(image_path)

        file_name , extension = file_name_with_extension.split('.')
        img_extensions = ['jpeg','jpg','png']

        if extension in img_extensions:

            img_sender_obj.SendingImage(image_path=image_path,s=s,destination=final_target,file_name_wth_extension=file_name_with_extension)




                

            logging.info(f"we have successfully sent the image {image_path}")
        
        else:
            logging.info(f"you have choose wrong path of the image !")
            print('Plz enter valid image path !')

    except Exception as e:
        raise ShareChatException(e,sys)
