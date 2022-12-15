from PIL import Image

def openFile () :
	img = Image.open("UserFile/test.png")
	img = img.convert("P")
	return img 

def withoutNoise (img1)	:
	img2 = Image.new('P',img1.size,0)
	temp = []
	for x in range (img1.size[1]):
		for y in range (img1.size[0]):
			pix = img1.getpixel((y,x))
			if pix not in temp :
				temp.append(pix)
			
	print (temp)
	#img2.save("UserFile/test2.png") 
			
def captchaDecoder () :
	image = openFile()
	image = withoutNoise(image)

