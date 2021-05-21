from collections import Counter
from math import sqrt

def k_plus_proches_voisins(classes, objet, k) :
    """ Retourne les K plus proches voisins de objet dans classes 
    k_voisins = k_plus_proches_voisins(classes, objet, k)
    Arguments :
    -----------
        classe  list
            [classe,xprédictif1,xprédictif2 ... ,xpredictifn] 
        objet : list 
            [xobject1,xobjet2 ... ,xobjetn]  
        k integer
            k plus proches voisins à retenir
    Sorties:
    --------
        K_voisins list
            liste des k classes les plus proches de objet
    """
    # distance_cible : critère de tri des classes -> distance entre classe et objet
    # ici, la distance euclidienne est utilisée
    def distance_cible(classe) :
        distance = sqrt((classe[1]-objet[0])**2+(classe[2]-objet[1])**2)
        return distance

    # sorted avec argument key
    classes_triee = sorted(classes,key= distance_cible)  
    # liste des k classes les plus proches initialisée vide 
    proches_voisins=[]
    for i in range(k):
        proches_voisins.append(classes_triee[i][0])

    #proches_voisins = classes_triee[:k]
    

    return proches_voisins

def classe_majoritaire(k_plus_proches) :
    """ sort un tuple contenant (le nom de classe,nombre) du plus grand nombre d'items """
    cnt = Counter(k_plus_proches).most_common(2)
    return cnt

if __name__ == "__main__":
    liste_personnes =[
    ['H',178,72],
    ['H',174,72],
    ['F',163,55],
    ['F',168,58],
    ['H',181,98],
    ['F',170,60],
    ['H',184,78],
    ['F',171,59],
    ]

    personne = [180,65]
    k=3

    print(k_plus_proches_voisins(liste_personnes,personne,k))