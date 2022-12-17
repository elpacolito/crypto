from PIL import Image
import pytesseract

def openFile () :
	img = Image.open("UserFile/test.png")
	img = img.convert("L")
	return img 
			
def captchaDecoder () :
	captcha_image = openFile()
	#image = withoutNoise(image)
	threshold = captcha_image.point(lambda x: 0 if x < 128 else 255, '1')
	captcha_text = pytesseract.image_to_string(threshold)
	print (captcha_text)
