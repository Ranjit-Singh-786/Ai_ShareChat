from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os ,sys

class TextFileProcess:

    def Data_sampling(self,file_path):
        """This function returns text data after reading from text file. and label and filename"""
        try:
            file_name = os.path.basename(file_path)
            file_name ,  extension = file_name.split('.')

            if extension == 'txt':
                logging.info(f'Sampling Text file from :- {file_path}')
                with open(file_path,'r',encoding='utf-8') as file:
                    file_data = file.read()
                    Data_label = "1"
                    file_data_with_label = Data_label + file_name + '|' + file_data
                    encrypted_file_data_with_label = file_data_with_label.encode('ascii')
                    logging.info('successfully sampled your text data !')
                return encrypted_file_data_with_label
            else:
                logging.info(f'we are not able to read your file from your path :- {file_path}')

        except Exception as e:
            raise ShareChatException(e,sys)




    def Data_resampling_write(self,Recieve_data , writing_path):
        try:
            logging.info('resampling the Text data !')
            Data_label = Recieve_data[0]
            file_name = Recieve_data[1:Recieve_data.find('|')]
            Data = Recieve_data[Recieve_data.find('|')+1:]
            file_name = file_name+'.txt'
            os.makedirs(writing_path,exist_ok=True)
            file_dir_path = writing_path + "\\"+file_name
            print(file_dir_path)
            logging.info(f'writing text file data into text file {writing_path}')
            with open(file_dir_path ,'w',encoding='utf-8') as text_file:
                text_file.write(Data)
            logging.info(f"successfully written text data  into text file :- {writing_path}")
        except Exception as e:
            raise ShareChatException(e,sys)