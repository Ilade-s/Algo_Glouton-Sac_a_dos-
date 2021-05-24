"""
Implémentation simple (2D/carac) d'un algo des k plus proches voisins
Taux de réussite : 60.49% (1087/1797)
"""
from math import sqrt
import csv
from os import getcwd
import random

def KVoisins(ano, database=[[]], K=3, typeindex=0, csvfile="", readlimit=None):
    """
    Donne le type de la nouvelle valeur selon les données preétablies

    PARAMETRES :
        - doivent avoir le même nombre de paramètres
        - ano : tuple | list
            - donnée anonyme à identifier
        - database : list[list]
            - tableau 2D des données identifiées 
        - K : int
            - nombre de plus proches voisins à exploiter
            - default = 3
        - typeindex : int
            - index des données de titre
            - default = 0
        - csvfile : str
            - nom (sans extension) du fichier csv à exploiter entièrement
            - si vide, sera ignoré et database sera utilisé
        - readlimit : int | None
            - limites de lecture du fichier csv si demandé

    SORTIE :
        - retval : (iD,prob)
            - iD : type identifié de la donnée ano
            - prob : probabilité que le type identifié soit correct (en %)
    """
    if csvfile!="": # Ouverture d'un fichier csv si donné
        with open(f"{getcwd()}\\Kvoisins\\{csvfile}.csv", 'r', encoding="utf-8", newline='') as file:
            dbR = csv.reader(file, delimiter=",")
            if readlimit==None:   
                database = [i for i in dbR][1:]
            else:
                database = [i for i in dbR][1:]
                database = database[:readlimit]

    def GetKey(e):
        return e[1]
    iD = ""
    distances = [[item[typeindex], sqrt(sum(
        (int(float(ano[i]))-int(float(item[i])))**2 for i in range(len(ano)) if i != typeindex))] 
            for item in database]
    kvList = sorted(distances,key=GetKey)[:K]
    dictt = {}
    typeList = list(set([kv[0] for kv in kvList]))
    vmax = 0
    tot = 0
    for t in typeList:
        v = len([i for i in kvList if i[0] == t])
        dictt[t] = v
        tot += v
        if dictt[t] > vmax:
            iD = t
            vmax = dictt[t]
    prob = round(vmax/tot*100, 3)

    return (iD, prob)

def main():
    ano = [0,0,0,12,13,5,0,0,0,0,0,11,16,9,0,0,0,0,3,15,16,6,0,0,0,7,15,16,16,2,0,0,0,0,1,16,16,3,0,0,0,0,1,16,16,6,0,0,0,0,1,16,16,6,0,0,0,0,0,11,16,10,0,0]
    retval = KVoisins(ano, csvfile="digits", typeindex=0, K=5)
    (iD, prob) = retval
    print(f"type de donnée : {iD}")
    print(f"Probabilité : {prob}%")

def verif(csvfile,readlimit=1797):
    nC = 0
    with open(f"{getcwd()}\\Kvoisins\\{csvfile}.csv", 'r', encoding="utf-8", newline='') as file:
        dbR = csv.reader(file, delimiter=",")
        dball = [i for i in dbR]
        random.shuffle(dball)
        db = dball[:readlimit]
        for element in db:
            trueValue = element[0]
            ano = element[1:]
            retval = KVoisins(ano, dball, typeindex=0, K=5)
            (iD, prob) = retval
            if iD==trueValue:
                nC += 1
            print(db.index(element))
    print(f"Taux de réussite : {round(nC/len(db)*100, 3)}% ({nC}/{len(db)})")

if __name__ == '__main__':  # test
    #main()
    verif("digits",50)
