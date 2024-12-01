'''
import csv

with open('Data.csv') as fichier:
	reader = csv.reader(fichier, delimiter=',')
	champs = next(reader)
	print(champs)
	print('Voici les données :')
	for ligne in reader:
		print(ligne)
'''

'''
import pandas

dataframe = pandas.read_csv('Data.csv', delimiter=',') 
print(dataframe)

for index, ligne in dataframe.iterrows():
	print(ligne['ville'] + " " + ligne['type'])
'''

'''
import csv

with open('Data_w.csv', 'w') as fichier:
	writer = csv.writer(fichier, delimiter=',')
	writer.writerow(['nom', 'prenom'])
	writer.writerow(['Jean', 'Prince'])
	writer.writerow(['Michel', 'Roger'])
	writer.writerow(['Joseph', 'Marie'])
'''

import pandas

data = pandas.DataFrame([['Jean', 'Prince'], ['Michel', 'Roger']], columns=['Nom', 'Prenom'])
data.to_csv('panda_w.csv', index=False)	
