
		
def openfile ():
	fileToOpen=open("ch7.bin",'rb')
	return fileToOpen.read()
	
def cesar() :
	data=openfile()
	for i in range (256):
		print (i)