import nmap


def namp_scan():
	ip = "192.168.0.130"
	port_range = raw_input("Enter the port range:\t ")
	nm = nmap.PortScanner()
	nmap_info= nm.scan(ip, port_range)
	print "For IP address: ",ip ,"\n"
	if int(nmap_info['nmap']['scanstats']['uphosts']):
		for port in nm[ip]['tcp'].keys():
			print "Open Port:\t ",port,"\tDescription\t", nm[ip]['tcp'][port]['name']
				
namp_scan()
	
	
"""
{'status': {'state': 'up', 'reason': 'localhost-response'}, 'hostnames': [{'type': '', 'name': ''}], 'vendor': {}, 'addresses': {'ipv4': '192.168.0.1'}, 'tcp': {137: {'product': '', 'state': 'filtered', 'version': '', 'name': 'netbios-ns', 'conf': '3', 'extrainfo': '', 'reason': 'no-response', 'cpe': ''}, 139: {'product': 'Microsoft Windows netbios-ssn', 'state': 'open', 'version': '', 'name': 'netbios-ssn', 'conf': '10', 'extrainfo': '', 'reason': 'syn-ack', 'cpe': 'cpe:/o:microsoft:windows'}, 135: {'product': 'Microsoft Windows RPC', 'state': 'open', 'version': '', 'name': 'msrpc', 'conf': '10', 'extrainfo': '', 'reason': 'syn-ack', 'cpe': 'cpe:/o:microsoft:windows'}}}

{'nmap': {'scanstats': {'uphosts': '1', 'timestr': 'Sun Mar 18 17:04:58 2018', 'downhosts': '0', 'totalhosts': '1', 'elapsed': '10.27'}, 'scaninfo': {'tcp': {'services': '22-443', 'method': 'syn'}}, 'command_line': 'nmap -oX - -p 22-443 -sV 127.0.0.1'}, 'scan': 

{'127.0.0.1': {'status': {'state': 'up', 'reason': 'localhost-response'}, 'hostnames': [{'type': 'PTR', 'name': 'localhost'}], 'vendor': {}, 'addresses': {'ipv4': '127.0.0.1'}, 'tcp': {137: {'product': '', 'state': 'filtered', 'version': '', 'name': 'netbios-ns', 'conf': '3', 'extrainfo': '', 'reason': 'no-response', 'cpe': ''}, 135: {'product': 'Microsoft Windows RPC', 'state': 'open', 'version': '', 'name': 'msrpc', 'conf': '10', 'extrainfo': '', 'reason': 'syn-ack', 'cpe': 'cpe:/o:microsoft:windows'}}}}}
"""