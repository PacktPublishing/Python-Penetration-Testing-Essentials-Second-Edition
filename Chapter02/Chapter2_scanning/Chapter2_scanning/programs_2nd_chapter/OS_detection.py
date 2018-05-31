
import nmap, sys
syntax="OS_detection.py  <hostname/IP address>"
if len(sys.argv) == 1:
    print (syntax)
    sys.exit()

host = sys.argv[1]
	
nm=nmap.PortScanner()
open_ports_dict =  nm.scan(host, arguments="-O").get("scan").get(host).get("tcp")
print "Open ports ", " Description"
port_list = open_ports_dict.keys()
port_list.sort()
for port in port_list:
	print port, "---\t-->",open_ports_dict.get(port)['name']
print "\n--------------OS detail---------------------\n"
print "Details about the scanned host are: \t", nm[host]['osmatch'][0]['osclass'][0]['cpe']
print "Operating system family is: \t\t", nm[host]['osmatch'][0]['osclass'][0]['osfamily']
print "Type of OS is: \t\t\t\t", nm[host]['osmatch'][0]['osclass'][0]['type']
print "Generation of Operating System :\t", nm[host]['osmatch'][0]['osclass'][0]['osgen']
print "Operating System Vendor is:\t\t", nm[host]['osmatch'][0]['osclass'][0]['vendor']
print "Accuracy of detection is:\t\t", nm[host]['osmatch'][0]['osclass'][0]['accuracy']

