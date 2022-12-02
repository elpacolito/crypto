import requests
import os
import base64
import re
import subprocess
import urllib

def openFile () :
	CaptchaFile = input ('Nom du fichier contenant le Captcha : ')
	CaptchaFile = 'UserFile/'+CaptchaFile
	Captcha = open (CaptchaFile,'rb').read()
	#print (Captcha)
	return base64.b64decode(Captcha.decode('ascii'))
	
def captchaDecoder () :
	print ('hello word')
	Captcha =  openFile()
	Captcha = Captcha.replace("\n","")
	Captcha = Captcha.replace("\r","")
	Captcha = Captcha.replace(" ","")
	Captcha = Captcha.replace(",","")
	Captcha = Captcha.replace("_","")
	print (Captcha)
