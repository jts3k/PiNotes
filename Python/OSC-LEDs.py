""" receiving OSC with pyOSC
https://trac.v2.nl/wiki/pyOSC
example by www.ixi-audio.net based on pyOSC documentation

this is a very basic example, for detailed info on pyOSC functionality check the OSC.py file
or run pydoc pyOSC.py. you can also get the docs by opening a python shell and doing
>>> import OSC
>>> help(OSC)
"""

#! /usr/bin/python
from __future__ import division
import socket
import OSC
import time, threading
import Adafruit_PCA9685
import os
import socket

time.sleep(5)

pwm = Adafruit_PCA9685.PCA9685()

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

ip = get_lan_ip()
port = 9000

LEDs = 16

print("Listening on {i}, {p}".format(i=ip, p=port))

# tupple with ip the OSC server will listen to.
receive_address = ip, port
# receive_address = "127.0.0.1", 9000

time.sleep(1)

# OSC Server. there are three different types of server.
s = OSC.OSCServer(receive_address) # basic
##s = OSC.ThreadingOSCServer(receive_address) # threading
##s = OSC.ForkingOSCServer(receive_address) # forking



# this registers a 'default' handler (for unmatched messages),
# an /'error' handler, an '/info' handler.
# And, if the client supports it, a '/subscribe' & '/unsubscribe' handler
s.addDefaultHandlers()



# define a message-handler function for the server to call.
def printing_handler(addr, tags, stuff, source):
    print "---"
    print "received from :  %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags : %s" % tags
    print "data : %s" % stuff
    print "---"

# messages will control numberOfLEDs
def LED_handler(addr, tags, stuff, source):
#    print int(addr.strip('-LED').strip('/'))
    pwm.set_pwm(int(addr.strip('-LED').strip('/')), 0, stuff[0])

s.addMsgHandler("/test", printing_handler) # adding our function, first parameter corresponds to the OSC address you want to listen to

# adding LED inputs...

for x in range (0, LEDs):
    s.addMsgHandler("{l}-LED".format(l=x), LED_handler)


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()


try :
    while 1 :
        time.sleep(5)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"
