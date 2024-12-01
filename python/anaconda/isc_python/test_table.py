'''
identifiant,ville,CP,revenu,remboursement,duree,type,taux
0,TOULOUSE,31100,3669.0,1130.05,240,immobilier,1.168
'''

## Supprime Doublon
def supprime_doublon(table, colonne):
	tableTriee = sorted(table, key = lambda ligne:ligne[colonne], reverse=True)
	tmp=[tableTriee[0]]
	for ligne in tableTriee:
		if (ligne[colonne] != tmp[-1][colonne]):
			tmp.append(ligne)
	return tmp
	

## Donnees brutes
def get_table(fichier):
	f = open(fichier, "r")
	#tab=[ligne.rstrip().split(",") for ligne in f]
	nom_champs=f.readline().rstrip().split(",")
	tab = []
	for ligne in f:
		data = ligne.rstrip().split(",")
		data[0] = int(data[0])
		data[2] = int(data[2])
		data[3] = float(data[3])#revenu
		data[4] = float(data[4])#remboursement
		data[7] = float(data[7])#taux
		tab.append(data)
	f.close()
	return nom_champs, tab
	

## Importer Data.csv : return tuple
champs, table = get_table("Data.csv")
tup = get_table("Data.csv")
print(type(champs))
print(type(table))
print(type(tup))
print(dir(tup))


## Trier le tableau
sorted_tab = sorted(table, key = lambda ligne:ligne[3], reverse=True)

## Search on one condition 
# ~ search_tab = []

# ~ for ligne in tab:
	# ~ if ligne[0] > 3:
		# ~ search_tab.append(ligne)

# ~ print(tab)
# ~ print(search_tab)
print(sorted_tab)
print(supprime_doublon(sorted_tab, 1))
