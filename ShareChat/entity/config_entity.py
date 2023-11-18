from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os , sys


class SharingConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),'Artifact')
        except Exception as e:
            raise ShareChatException(e,sys)


class MessageConfig:
    def __init__(self):
        try:
            self.message_file_name = 'Inbox.txt'
        except Exception as e:
            raise ShareChatException(e,sys)



# class ImageConfig:
#     def __init__(self):
#         try:
#             self.message_file_name = 'Inbox.txt'
#         except Exception as e:
#             raise ShareChatException(e,sys)








