import random
import json

############### INPUT USER : FICHIER, TAILLE MAX GROUPE #################

fichier = input('Nom du fichier qui contient la liste des prénoms :\n')
nbrpersonnemax = int(input('Entrez la taille maximum des groupes :\n'))

#########################################################################

############## OUVERTURE, LECTURE, MESURE DU FICHIER ####################

fichier = open(fichier, encoding="utf-8")
fichier = fichier.readlines()
tailleliste = len(fichier)

#########################################################################

########## CALCUL NBR GROUPE TOTAL & NBR GROUPE PLEINS ##########################

nbrgroupe = (tailleliste//nbrpersonnemax)+1
nbrgroupecharge = tailleliste%nbrgroupe
resultjson = {}

#########################################################################

result = [] # liste vide qui accueillera nos groupes finaux #############

############### BOUCLE WHILE POUR CREER LES GROUPES DANS RESULT #########

i=0
while i < nbrgroupe:
    result.append([])
    i+=1

#########################################################################

"""######################################################################
Pour chaque groupe, on vérifie d'abord si c'est un groupe plein ou pas, 
si oui : on ajoute aléatoirment le nombre max de personne par groupe dedans
sinon : on ajoute le même nombre - 1 de personne toujours aléatoirement
une fois l'ajout terminé, afin de ne pas ajouter quelqu'un dans 2 groupe en même il est rétirer de la liste du fichier
"""

i=0
while i < len(result):
    if i < nbrgroupecharge:
        j = 0
        while j < nbrpersonnemax:
            elevechoisi = random.choice(fichier)
            result[i].append(elevechoisi)
            fichier.remove(elevechoisi)
            j+=1
    else:
        j = 0
        while j < nbrpersonnemax-1:
            elevechoisi = random.choice(fichier)
            result[i].append(elevechoisi)
            fichier.remove(elevechoisi)
            j+=1
    i+=1
###################################################################
#print(result)

# pour chaque groupe on print (groupe (index+1)) puis chacun des élèves qu'il contient

for groupe in result:
    print("groupe",result.index(groupe)+1)

    for eleve in groupe:
        print(eleve.strip())


with open("resultat_groupe.json", "w", encoding="utf-8") as write_file:
    json.dump(eleve.strip(),write_file)
###################################################################       BY GOGODEV & Y4N1S :)

resultjson["groupe1"] = []
print(resultjson)