#### 1.  TESTING LOGGING AND EXCEPTION HANDLING
from ShareChat.logger import logging
import os,sys
from Ai_ShareChat.exception import ShareChatException

num1 = int(input('enter first number'))
num2 = int(input('enter secorn number'))

try:
    logging.info('We are going to Testing logging module !')
    result = num1 / num2
    print(f"This is your output :-{result}")
    logging.info('Logging Module working successfully')
except Exception as e:
    logging.info('we are getting Zero Division error')
    raise ShareChatException(e,sys)

# OUTPUT >>> SUCCESSFULLY TESTED