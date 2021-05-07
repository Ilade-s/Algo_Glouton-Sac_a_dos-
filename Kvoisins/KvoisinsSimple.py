"""
Implémentation simple (2D/carac) d'un algo des k plus proches voisins
"""
from math import sqrt


def KVoisins(ano, database: list[list], K=3, typeindex=0):
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
    SORTIE :
        - retval : (iD,prob)
            - iD : type identifié de la donnée ano
            - prob : probabilité que le type identifié soit correct (en %)
    """
    def GetKey(e):
        return e[1]
    iD = ""
    distances = [[item[typeindex], sqrt(sum(
        [(ano[i]-float(item[i]))**2 for i in range(len(ano)) if i != typeindex]))] 
            for item in database]
    kvList = sorted(distances,key=GetKey)[:K]
    dictt = {}
    typeList = list(set([kv[0] for kv in kvList]))
    vmax = 0
    tot = 0
    print(typeList)
    for t in typeList:
        v = len([i for i in kvList if i[0] == t])
        dictt[t] = v
        tot += v
        if dictt[t] > vmax:
            iD = t
            vmax = dictt[t]
    prob = round(vmax/tot*100, 3)

    return (iD, prob)


if __name__ == '__main__':  # test
    db = [
        ["H", 178, 72],
        ["H", 174, 72],
        ["F", 163, 55],
        ["F", 168, 58],
        ["H", 181, 98],
        ["F", 170, 60],
        ["H", 184, 78],
        ["F", 171, 59]
    ]
    ano = [169, 65]
    retval = KVoisins(ano, db)
    (iD, prob) = retval
    print(f"type de donnée : {iD}")
    print(f"Probabilité : {prob}%")
