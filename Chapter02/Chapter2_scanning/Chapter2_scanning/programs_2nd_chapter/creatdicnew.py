import cPickle 
pickle_file = open("port_description.dat","w") 
file_name = raw_input("Enter the file name ")
f = open(file_name,"r")
dict1 = {}
for line in f:
	key, value = line.split(':', 1)
	
	dict1[int(key.strip())] = value.strip()
	
print "Dictionary is created"
cPickle.dump(dict1,pickle_file) 
pickle_file.close()
print "port_description.dat is created"
