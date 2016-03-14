#!/usr/bin/python

__author__ = "Markus Lohr"
__copyright__ = "Copyright 2016, Markus Lohr"
__credits__ = ["Markus Lohr"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Markus Lohr"
__email__ = "markus.lohr.acn@gmail.com"
__status__ = "Development"
__note__ = """Main class of the app: This app reads IPs from AWSdynamoDB and/
                perioticly a timestamp to this IPs, the destination reply with 
                two timestamps (received, new send). The sender will add the 
                fourth an receiving and will put it in another tyble on 
                AWSdynamoDB for later analytics."""

import socket
import time
from aws_ddb_writer import AwsRoundTripsATW

isSender =  True

sendToAddress = '192.168.178.30'
mirrorSRVip = '192.168.178.31'

PORT = 4711
mirrorAddr = (mirrorSRVip, PORT)
sendAddr = (sendToAddress, PORT)
message = 'This is the message, it is send at: ' + str(int(round(time.time() * 1000)))
messageID = 0
nicBuffer = 1024

ddb_connection = AwsRoundTripsATW()

try:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', PORT))
    hostName = socket.gethostname()

    while True:
        message = str(hostName) + ": This is the message #" + str(messageID) + ", it is send at |" + str(int(round(time.time() * 1000)))
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


