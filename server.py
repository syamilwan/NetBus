import socket
import os
import random
  
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
   #c.send(">Connected")
   print "Connection from", addr
   sLoop='go'
   
   while sLoop!='stop':
     dapat=c.recv(5)
     print '>', dapat
     if dapat=='-quit':
      print addr, "will be disconnected"
      break
     elif dapat=='-shut':
      print "Shutting Down"
      os.system('shutdown -p now')
     elif dapat=='-spam':
      for x in range(5):
        y= random.randint(0,1274)
        z= random.randint(0,759)
        zz='xdotool mousemove '+str(y)+' '+str(y)+' click 1'
        os.system(zz)
     else:
      print 'Unknown Command'
      break
   
   # closing current socket
   c.close()
   print addr, 'Disconnected'
   
   
   
