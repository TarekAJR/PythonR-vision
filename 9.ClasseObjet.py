#coding:utf-8

print ("						LES CLASSES & OBJETS\n\n")

class Pays:
	Nom = ""
	Capital = ""
	Superficie = ""
	Population = ""
	Politique = ""

	def Exposer(self):
		intro = "Le %s est une %s, La Capital est %s, Le Pays a une Superficie total de $% km² ainsi qu'une population de %s.2f." % (self.Nom, self.Politique, self.Capital, self.Superficie, self.Population)
		return intro

p1 = Pays()
p1.Nom = "MAROC"
p1.Capital = "RABAH"
p1.Superficie = 710.850
p1.Population = "34 Millions habitants"
p1.Politique = "Monarchie Constitutionnel"

print (p1.Exposer())
