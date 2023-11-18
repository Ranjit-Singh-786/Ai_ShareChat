from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os , sys

class ChatMessage:

    def filter_message_address(self,RecieveDat):
        """Function returns message , ip address , port no"""
        try:
            logging.info('filtering the recieving data !')
            message = RecieveDat[0]
            if message[0:1] != b'2':
                message = message.decode('ascii')
                address = RecieveDat[1]
                ip_address = address[0]
                port_no = address[1]
                logging.info(f"successfully filter Recieve Data of the :- {ip_address}")
                return message , ip_address , port_no
            else:
                address = RecieveDat[1]
                ip_address = address[0]
                port_no = address[1]
                logging.info(f"successfully filter Recieve Data of the :- {ip_address}")
                return message , ip_address , port_no

        except Exception as e:
            raise ShareChatException(e,sys)