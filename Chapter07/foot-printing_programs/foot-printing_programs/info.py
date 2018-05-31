import re
import random
import urllib
url1 = raw_input("Enter the URL ")
u = chr(random.randint(97,122))
url2 = url1+u
http_r = urllib.urlopen(url2)
http_r1 = urllib.urlopen(url2)
http_r2 = urllib.urlopen(url2)
flag =0
i=0
list1 = []
a_tag = "<*address>"
file_text = open("result.txt",'a')

while flag ==0:
	if http_r.code == 404:
		file_text.write("--------------")
		file_text.write(url1)
		file_text.write("--------------\n")
		file_text.write(http_r1.read())
		for match in re.finditer(a_tag,http_r.read()):
			i=i+1
			s= match.start()
			e= match.end()
			list1.append(s)
			list1.append(e)
		if (i>0):
			print "Coding is not good"
		if len(list1)>0:
			a= list1[1]
			b= list1[2]
			print http_r2.read()[a:b]
		else:
			print "error handling seems ok"
		flag =1
	
	


		
		
		
	