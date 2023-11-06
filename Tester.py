#### 1.  TESTING LOGGING AND EXCEPTION HANDLING
from Ai_ShareChat.logger import logging
import os,sys
from Ai_ShareChat.exception import ShareChatException

num1 = int(input('enter first number'))
num2 = int(input('enter secorn number'))

try:
    logging.info('we are going to deviding ')
    result = num1 / num2
    print(f"This is your output :-{result}")
except Exception as e:
    raise ShareChatException(e,sys)

# OUTPUT >>> SUCCESSFULLY TESTED