

def choix ():
	f=open("ressource/menu.txt",'r').readlines()
	f = [ f[i][:-1] for i in range (len(f)) ]
	for i in range (len (f)):
		print (f" {i+1} : {f[i]} ")
	choix = input("que dois je faire ? ")
	maxi=len(f)
	return choix,maxi


def main (): 
	choise,maxi = choix () 
	try :
		choise = int(choise)
	except :
		print ("prendre un numéro\nFermeture du programme")
	if (choise == 2 ):
		import mode.filtrage as fi
		print ('\n------------------\n')
		fi.filtrage()
		
	print('\n+---------+\n|task over|\n+---------+\n')
		 
		
	
main()

"""
+---------+
|task over|
+---------+

"""