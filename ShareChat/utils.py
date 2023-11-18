from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os,sys

def Data_identifier(Recieve_data_message):
    try:
        logging.info('Identifying Recieving Data !')
        Data_label = Recieve_data_message[0]
        # There are Data label
        # 0   --->  Message
        # 1   --->  Text file
        # 2   --->  Image
        if Data_label == '0':
            return 'message'
        elif Data_label == '1':
            return 'text-file'
        else:
            return 'image'

    except Exception as e:
        raise ShareChatException(e,sys)