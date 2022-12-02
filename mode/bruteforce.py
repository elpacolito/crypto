import hashlib

def OpenFile(hashesFile): 
	hashes = open (hashesFile,'r').readlines()
	return hashes

def hashToDecode():
	print ('\nou se trouve le hash ?\n1 : dans un fichier (chaque ligne correspond à un hash)\n2 : dans le presse papier\n')
	hashes=[]
	choix = int(input('mettre un numéro : '))
	if (choix == 1) :
		hashesFile = input ('Nom du fichier contenant le ou les hash : ')
		hashesFile = 'UserFile/'+hashesFile
		hashes = OpenFile(hashesFile)
	if (choix == 2) :
		tmp = input ("hash à décoder : ")
		hashes.append(tmp)
	return hashes
	
	
def BF_MD5(hashes,liste_bf) :
	result = []
	for val in hashes : 
		for mdp in liste_bf :
			print (hashlib.md5(mdp.encode()).digest())
			if  hashlib.md5(mdp.encode()).hexdigest()== val :
				print (f'le hash de {mdp} est {val}')
				result.append(mdp)
				return result 
		print (f"no password found for {val}") 
	


def bfmain() :
	hashes = hashToDecode()
	liste_bf = OpenFile('ressource/test.txt')
	#liste_bf = OpenFile('ressource/rockyou.txt')
	result = BF_MD5(hashes,liste_bf)


# 5f4dcc3b5aa765d61d8327deb882cf99 : password
