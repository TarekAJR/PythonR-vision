#coding:utf-8
print("					LISTE\n\n")

# EN HOMMAGE A SOUFIANE EL-BAKKALI MEDAILLER D'OR AU JO DE TOKYO 2020 EN LA DISCIPLINE DU 3000M STEEPLES
MEDAILLE = []
PAYS = []
NOM = []


#AJOUTE DES ELEMENTS DANS LA LISTE

MEDAILLE.append("OR")
MEDAILLE.append("ARGENT")
MEDAILLE.append("BRONZE")

Prix_du_champion = MEDAILLE[0]

PAYS.append("FRANCE")
PAYS.append("KENYA")
PAYS.append("MAROC")
PAYS.append("BRESIL")
PAYS.append("ETHIOPY")

Pays_du_champion = PAYS[2]

NOM.append("ASSAYDI")
NOM.append("BOUFAL")
NOM.append("SAISS")
NOM.append("EL-BAKKALI")
NOM.append("AJRAOU")

Nom_du_champion = NOM[3]

print("LE COURREUR SACREE CHAMPION OLYMPIQUE SE NOMME %s\n" % Nom_du_champion)

print("LE CHAMPION COUR SOUS LA BINIAIRE DU %s\n" % Pays_du_champion)

print("SOUFIANE %s EST MEDAILLER D'%s AU JO TOKYO 2020\n" % (Nom_du_champion, Prix_du_champion))
