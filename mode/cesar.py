
		
def openfile ():
	fileToOpen=open("UserFile/ch7.bin",'rb')
	return fileToOpen.read()
	
def cesar() :
	test = ''
	data=openfile()
	for val in data :
		test += chr(val)
	print (test) 
	
