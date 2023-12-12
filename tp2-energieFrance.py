
import csv
import matplotlib.pyplot as plt
mois = []
moyennes_consommation = []
for courbe in range(12):
    mois.append('')
    moyennes_consommation.append([])
with open('/home/Etudiants/RT/BUT-RT-1/tb259067/Téléchargements/RTE_2020.csv', newline='') as csvfile:
    lecteur = csv.reader(csvfile, delimiter=',')
    next(lecteur)
    
    for ligne in lecteur:
        if ligne and len(ligne) >= 5:
            date_str = ligne[2]
            if ligne[4].isdigit():
                consommation = int(ligne[4])
            else:
                consommation = None
            try:
                annee, mois_num, courbe = map(int, date_str.split('-'))
                if annee == 2020 and 1 <= mois_num <= 12:
                    index = mois_num - 1
                    mois[index] = f"{mois_num} {annee}"
                    if consommation is not None:
                        moyennes_consommation[index].append(consommation)
            except ValueError:
                print(f"courbe date: {date_str}")
moyennes = []                                    #faire la moyenne avec une boucle for
for consommations in moyennes_consommation:
    if consommations:
        moyenne = sum(consommations) / len(consommations)
    else:
        moyenne = 0
    moyennes.append(moyenne)
plt.figure(figsize=(10, 6))                   #code pour representer la courbe 
plt.plot(mois, moyennes)
plt.title('Consommation moyenne par mois en 2020')
plt.xlabel('Mois')
plt.ylabel('Consommation moyenne')
plt.tight_layout()
plt.show()





