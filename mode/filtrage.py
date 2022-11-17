
"""
FTR = 	FileToRead 
FTW = 	FileToWrite
data = 	Data in FTR
DWS = 	Data Without Space
"""

ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ABC123='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
UF = 'UserFile/'

def readFile (FTR):  
	f = open(FTR,'r')
	data = f.read()
	f.close ()
	return data

def writeFile (FTW,DWS):
	f=open (FTW,'w')
	f.write(DWS)
	f.close()
	

def filtrage ():
	FTR = UF
	FTR += input ('nom du fichier à lire (doit se trouver dans UserFile) : ')
	data = readFile(FTR)
	DWS = ''
	alphabet= input("choisir l'alphabet autorisé \n1 pour tout l'alphabet\n2 pour alphabet + chiffre\nSinon mettre les caracteres autorisés alphabet autorisé ? ")
	if alphabet=='1' :
		alphabet = ABC
	elif alphabet =='2' :
		alphabet = ABC123
	for letter in data :
		if (letter in alphabet):
			DWS += letter 
	FTW = UF
	FTW +=  input ('nom du fichier pour enregistrer le résultat : ')
	writeFile (FTW,DWS)
	
	
	
	
	