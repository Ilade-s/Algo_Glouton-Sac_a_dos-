"""
Implémentation simple (2D/carac) d'un algo des k plus proches voisins
"""
from math import sqrt

def KVoisins(ano, database:list[list], K=3):
    """
    Donne le type de la nouvelle valeur selon les données preétablies

    PARAMETRES :
        - doivent avoir le même nombre de paramètres
        - ano : tuple | list
            - donnée anonyme à identifier
        - database : dict{list}
            - dictionnaire des données identifiées (clés = type ; data = carac)
        - K : int
            - nombre de plus proches voisins à exploiter
    SORTIE :
        - iD : any
            - type identifié de la donnée ano
    """
    iD = ""
    distances = [[item[0],sqrt(sum([(ano[i]-item[i+1])**2 for i in range(len(ano))]))] for item in database]
    kvList = sorted(distances)[:K]
    dictt = {}
    typeList = list(set([kv[0] for kv in kvList]))
    vmax = 0
    for t in typeList:
        dictt[t] = len([i for i in typeList if i[0]==t])
        if dictt[t]>vmax:
            iD = t
            vmax = dictt[t]

    return iD


if __name__=='__main__': # test
    db = [
        ["H",178,72],
        ["H",174,72],
        ["F",163,55],
        ["F",168,58],
        ["H",181,98],
        ["F",170,60],
        ["H",184,78],
        ["F",171,59]
    ]
    ano = [169,65]
    iD = KVoisins(ano, db)
    print(f"type de donnée : {iD}")