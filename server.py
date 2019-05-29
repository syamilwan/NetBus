# import the socket library 
import socket                
  
# create socket object 
s = socket.socket()          
print "Socket successfully created"
  
# reserve a port
port = 12345                
  
# Next bind to the port, inputted an empty string makes the server listen to requests
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            

# a infinite loop until interrupted or error occurs (always in listening state)
while True: 

   # Establish connection with client. 
   c, addr = s.accept()
   c.send('>Connected')
   print "Connection from", addr
   sLoop='ok'
   while sLoop=='ok':
     if c.recv=='quitt'
      print c.recv(1024)
      sLoop='xx'
     else
      print c.recv(1024)
