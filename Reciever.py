import  socket 
import  time 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="0.0.0.0"
my_port=1005
my_address=(my_ip,my_port)
s.bind(my_address)

while True :
    data=s.recvfrom(100) 
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    print(final_msg)
    time.sleep(2)