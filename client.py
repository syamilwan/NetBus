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
  print("Input %s received." % cmd)
  
  if cmd=="help":
    print("Command list: ")
    s.send(hantar)
  elif cmd=="shut":
    print("Shutting down server")
    s.send(hantar)
  elif cmd=="quit":
    print("Quiting the connection to server")
    s.close()  # close the connection
    prompt=False
  else:
    print("Unrecognized input, input 'help' for manual")
 


