#coding:utf-8

print ("							FONCTIONS\n\n")

#APPEL DE FONCTIONS



COMMAND = input("ENTREZ UNE FONCTION : ")
print ("\n")

def Salutation():
	return "Bonjour\n"

def Presentation():
	return "Je suis VARIS\n"

def Meteo():
	return "19°C Il pleut\n"

def Geo_Politique():
	return "La civilisation est toujours presente sur Terre\n"

def Prevision():
	return "La Civilisation fut deciment par plusieur Mutation d'un virus mortel pour l'être humain appeler LE COVID19\n"

def PEGESUS():
	return "JE LANCE LE PROTOCOLE DE SURVEILLANCE GLOBAL PEGASUS\n"



if COMMAND in ["Salutation", "SALUTATION", "salutation"]:
	print (Salutation())

elif COMMAND in ["Presentation", "PRESENTATION", "PRESENTATION"]:
	print (Presentation())

elif COMMAND in ["Meteo", "METEO", "meteo"]:
	print (Meteo())

elif COMMAND in ["Geo_Politique", "GEO_POLITIQUE", "geo_politique"]:
	print (Geo_Politique())

elif COMMAND in ["Prevision", "PREVISION", "prevision"]:
	print (Prevision())

elif COMMAND in ["Pegasus", "PEGESUS", "pegasus"]:
	print (PEGESUS())

else:
	print ("ENTREZ UNE FONCTION EXISTANTE")

