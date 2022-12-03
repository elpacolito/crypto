import json
"""
FTO = File To Open
HTO = How To Open 
"""

def openfile(FTO,HTO):
	fileToOpen=open(FTO,HTO)
	return fileToOpen.read()
	
def cesar():
	hexval = ''
	liste = []
	data=openfile("UserFile/ch7.bin","rb")
	hexval = data.hex(' ',1)
	liste = hexval.split(' ') 
	liste = [ int(val,16) for val in liste ]
	bruteforce(liste)
	
def bruteforce(liste):
	dicoraw = openfile("ressource/dicofr.json","r") 
	dico = json.loads(dicoraw)
	values = []
	for i in range (255) : 
		potentiel_flag = ''
		count = 0
		for val  in liste :
			 potentiel_flag += chr ( (val + i) % 255 )
		
		for word in dico :
			if (word in potentiel_flag) :
				count += 1 
		values.append(count)
	i = values.index(max(values))
	message = "".join([chr( (val + i)%255) for val in liste])
	print (message)
			
		
		#print (potentiel_flag)
		
			
		
	
