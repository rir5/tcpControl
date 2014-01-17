import socket
import sys
 
HOST = '192.168.1.6'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:    
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'

#wait to accept a connection - blocking call
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#now keep talking with the client
while 1:

    data = conn.recv(1024)
    reply = 'OK...' + data
    print data
    if data == "off":
        conn.close()
        s.close()
        SystemExit
        #sys.exit()
        break
     
    conn.sendall(reply)
 
#conn.close()
#s.close()
