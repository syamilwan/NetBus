# Import socket module 
import socket                
  
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
  print("Input command: ") 
  hntar = input()
  print("Input %d received." % cmd)
  
  if cmd==1:
    print("Command list: ")
    s.send(hantar)
  elif cmd==2:
    print("Shutting down server")
    s.send(hantar)
  elif cmd==3:
    print("Quiting the connection to server")
    s.close()  # close the connection
    prompt=False
  else:
    print("Unrecognized input, input 'help' for manual")
 


