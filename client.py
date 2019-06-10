# Import socket module 
import socket
import os
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.59.75', port))
print('Connection request sent')
  
# receive data from the server 
print s.recv(1024)

# prompt input for command loop
prompt=True
while prompt:
  print("\n##Input command: ") 
  hantar = raw_input()
  
  if hantar=='-help':
    print("\n##Command list: --- \n  -shut: Shut Down server \n  quit: Disconnect from server \n  more:")
  elif hantar=='-shut':
    print("\n##Shutting down server")
    s.send(hantar)
  elif hantar=='-quit':
    print("\n##Quiting the connection to server")
    s.send(hantar)
    s.close()  # close the connection
    prompt=False
  else:
    print("\n##Unrecognized input, input '-help' for manual")
    
 


