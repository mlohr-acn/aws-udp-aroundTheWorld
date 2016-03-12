import socket
import time

isSender =  True

sendToAddress = '192.168.178.30'
mirrorSRVip = '192.168.178.31'

PORT = 4711
mirrorAddr = (mirrorSRVip, PORT)
sendAddr = (sendToAddress, PORT)
message = 'This is the message is send at: ' + str(int(round(time.time() * 1000)))
messageID = 0
nicBuffer = 1024

try:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', PORT))
    hostName = socket.gethostname()

    while True:
        message = str(hostName) + ": This is the message #" + str(messageID) + " is send at|" + str(int(round(time.time() * 1000)))
        messageID += 1
        
        if isSender:
            # Send data
            print '<<<<  sending:: "%s"' % message
            sent = sock.sendto(message, mirrorAddr)
        
            # Receive response
            print '....... waiting to receive'
            
        data, server = sock.recvfrom(nicBuffer)
        print '>>>> received MIRROR:: "%s"' % data
        
        if not isSender:   
            # echoing
            print "echoing"
            message = data + "|" + str(int(round(time.time() * 1000)))
            sent = sock.sendto(message, server)
            
            #data, server = sock.recvfrom(nicBuffer)
            #print '>>>> received SENDER:: "%s"' % data
        
        time.sleep(5)

finally:
    print 'closing sockets'
    sock.close()


