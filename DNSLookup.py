import socket
import sys
print "#" * 50
print "DNSLOOKUP"
print "#" * 50

try:
   for n in range (1,100):
	address1 = raw_input("Enter address: ")
	addr1 = socket.gethostbyname(address1)
	print "DNSlookup for", address1, "is", addr1
	print "Press ctrl+C to exit"

except KeyboardInterrupt:
	print "\n Exiting \n"
	sys.exit()


