from ShareChat.exception import ShareChatException
from ShareChat.logger import logging
import os,sys
from PIL import Image
import io
import numpy as np 
from typing import List
import time

class ImageSender:
    def __init__(self):
        pass


    def SendingImage(self,image_path,s,destination,file_name_wth_extension):
        try:

            logging.info(f" Sending the image in a packets")
            with open(image_path,'rb') as file:
                data = file.read()

        # >>>>>>>>>>>> RESIZING CODE   <<<<<<<<<<<<<<<<<<<<<
                image = Image.open(io.BytesIO(data))
                new_size = (550, 470)  # Replace with your desired dimensions
                resized_image = image.resize(new_size)
                resized_data = io.BytesIO()
                resized_image.save(resized_data, format='JPEG')  # Adjust format as needed
                resized_data = resized_data.getvalue()

        # >>>>>>>>>> ADDING LABEL WITH DATA  <<<<<<<<<<<<<<
                label_tag = '2'+file_name_wth_extension+'|'
                data_with_tag = label_tag.encode('ascii')+resized_data

        # >>>>>>>>>> CODE TO SENDING IMAGE DATA PACKETS    <<<<<<<<<<<<<<<<<<
                sent_packets = 0
                cost_mul = 20000
                total_pack = len(data_with_tag)
                i = 0
                while sent_packets <= total_pack:
                    if i == 0:
                        s.sendto(data_with_tag[0:cost_mul],destination)
                        sent_packets += cost_mul
                        i+=1
                        time.sleep(1)
                    else:
                        remaining = len(data_with_tag[cost_mul:])
                        difference = total_pack - remaining

                        if difference >= 20000:
                            s.sendto(data_with_tag[cost_mul:cost_mul*2],destination)
                            cost_mul = cost_mul * 2 
                            sent_packets = cost_mul
                            time.sleep(1)
                        else:
                            last_remaining = len(data_with_tag[cost_mul:])
                            s.sendto(data_with_tag[cost_mul:],destination)
                            sent_packets += last_remaining
                            time.sleep(1)

        except Exception as e:
            raise ShareChatException(e,sys)

    def Img_to_array_single(self,image_path:str):
        try:
            logging.info(f"converting image into array fetch image from {image_path}")
            file_name_with_extension = os.path.basename(image_path)
            file_name ,  extension = file_name_with_extension.split('.')
            image = Image.open(image_path)
            arr_img = np.array(image)
            label_list = [2,file_name_with_extension,file_name,extension]
            logging.info(f"successfully prepared the image data !")
            return arr_img,label_list

        except Exception as e:
            raise ShareChatException(e,sys)



    def Array_to_img_single(self,img_array, saving_img_path:str,labels:list):
        try:
            logging.info(f"getting image from array")
            image = Image.fromarray(img_array)
            image_saving_file_path = os.path.join(saving_img_path,labels[1])
            image.save(image_saving_file_path)
            logging.info(f"successfully saved the {labels[1]} image at this location :- {image_saving_file_path}")
        except Exception as e:
            raise ShareChatException(e,sys)



    def Img_to_array_Multiple(self,image_path:str):
        try:
            pass
        except Exception as e:
            raise ShareChatException(e,sys)



    def Array_to_img_Multiple(self,image_path:str):
        try:
            pass
        except Exception as e:
            raise ShareChatException(e,sys)
    