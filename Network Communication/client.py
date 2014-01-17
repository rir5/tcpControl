import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = '192.168.1.14'
port = 8888
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
#print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host
 
#Send some data to remote server
while 1:
    message = raw_input("Write Something: ")
    try :
        #Set the whole string
        s.sendall(message)
        if message == "off":
            s.close()
            sys.exit()
            break
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
 
print 'Message send successfully'
