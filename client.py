# Import socket module 
import socket
import os
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.59.74', port))
print('Connection request sent')
  
# receive data from the server 
print s.recv(1024)

# prompt input for command loop
prompt=True
while prompt:
  print("\n##Input command: ") 
  hantar = raw_input()
  
  if hantar=='helpp':
    print("\n##Command list: --- \n  shutt: Shut Down server \n  quitt: Disconnect from server \n  moree:")
  elif hantar=='shutt':
    print("\n##Shutting down server")
    s.send(hantar)
  elif hantar=='quitt':
    print("\n##Quiting the connection to server")
    s.send(hantar)
    s.close()  # close the connection
    prompt=False
  else:
    print("\n##Unrecognized input, input 'helpp' for manual")
    
 


