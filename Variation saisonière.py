import csv
import matplotlib.pyplot as plt
def filtre(mois):
    rte = []
    Resultat = [0, 0, 0]  #initialisation des futur somme
    with open('/home/Etudiants/RT/BUT-RT-1/am620105/BEBOU_NECTOUX_2/RTE_2020.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rte.append(row)
    for i in range(len(rte) - 1):
        Division_date = rte[i][2].split('-') #permet de diviser les dates en 3 partie (années, mois, jour)
        if Division_date[0] == '2020' and Division_date[1] == str(mois).zfill(2): #zfill me permet de d'avoir deux valeurs sinon ca bloque a cause des valeurs dans le csv
            for valeur in rte[i - 1][4]:
                if valeur.isdigit():
                    # ici en raison d'un problème avec la dernière valeur il ma fallut rajouter une verification sur les trois valeurs
                    valeur_4 = int(rte[i + 1][4]) if rte[i + 1][4].isdigit() else 0
                    valeur_5 = int(rte[i + 1][5]) if rte[i + 1][5].isdigit() else 0
                    valeur_10 = int(rte[i + 1][10]) if rte[i + 1][10].isdigit() else 0
                    #calcul de la somme
                    Resultat[0] += valeur_4
                    Resultat[1] += valeur_5
                    Resultat[2] += valeur_10
    return Resultat
#initialisation du graphique

moist = list(range(1, 13))
valeur = {'Value 1': [], 'Value 2': [], 'Value 3': []}

for mois in moist:
    Resultat = filtre(mois)
    print(f"resultat du mois {mois}: ", Resultat)
    for i, label in enumerate(['Value 1', 'Value 2', 'Value 3']):
        valeur[label].append(Resultat[i])

for label in valeur:
    plt.plot(moist, valeur[label], marker='o', label=label) # marker me permet d'afficher les points sur le graphique

plt.xlabel('Mois')
plt.ylabel('Consommation sur 1 mois')
plt.title('Graphique de consommation energétique')
plt.grid(True) # pour voir les grilles
plt.show()