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
  
        

# a infinite loop until interrupted or error occurs (always in listening state)
while True: 
   # put the socket into listening mode 
   s.listen(5)      
   print "socket is listening"    
   # Establish connection with client. 
   c, addr = s.accept()
   c.send('>Connected')
   print "Connection from", addr
   sLoop='go'
   while sLoop!='stop'
     dapat=c.recv(1024)
     print '>', dapat
     if dapat=='quitt':
      print addr, "Disconnected"
      c.close()
     elif dapat=='shutt':
      print "Shutting Down"
     else:
      print '>', dapat
   
   
   
