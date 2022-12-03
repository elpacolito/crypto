
"""
FTR = 	FileToRead 
counter= affiche le nombre de fois ou chaque lettre apparait

marche mieux si on remplace les lettre avec accent avec les lettres sans accent 
"""
ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def readFile (FTR):  
	FTR = "UserFile/" + FTR 
	f = open(FTR,'r')
	data = f.read()
	f.close ()
	return data

def writeFile (FTW,DWS):
	FTR = 'UserFile/' + FTR
	f=open (FTW,'w')
	f.write(DWS)
	f.close()


def ioc():

	FTR = input("fichier à ouvrir : ")
	data = readFile(FTR)
	data=data.upper()
	counter = []
	taille = 0
	den = 0
	num = 0
	finalresult=0
	
	
	for letter in ABC : 
		num = data.count(letter)
		counter.append(num*(num-1))
		taille +=num 
		
	
	den = taille * (taille - 1)
	print (counter)
	print (taille)
		
	for i in range (len(counter)):
		finalresult+= counter[i]/den
	
	print (f"l indice de coincidence est de : {finalresult} \n")
	
	if (finalresult < 0.05) :
		print ("le texte est surement aléatoire ou a subit un chiffrement polyalphabétique")
	else :
		print ("le texte est lisible ou a du recevoir un substitution monoalphabétique ou une transposition")
		
		
#ioc ()
	
