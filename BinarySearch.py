"""
Algorithme de recherche dichotomique : Binary Search

PRINCIPE :
----------
    - Donné un tableau 1D (liste) trié
    - recherche d'un élément précis
"""

def BinarySearch(t,e,ot):
    """
    Recherche d'un élément dans un tableau

    PARAMETRES :
        - t : list
            - tableau dans lequel se situe l'élément
        - e : int
            - élément dont on veut trouver la position
        - ot : list
            - copie du tableau initial, sera utilisé cpour trouver l'index absolu de l'élément
        
    SORTIE :
        - index : int
            - index de l'élément dans le tableau
    """
    # Vérifs (t vide ou e pas dans t)
    if e not in t:
        return -1
    if t==[]:
        return -1

    mid = len(t)//2

    if t[mid]==e:
        return ot.index(t[mid])
    
    elif t[mid]>e:
        return BinarySearch(t[:mid],e,ot)
    
    else:
        return BinarySearch(t[mid:],e,ot)

if __name__=='__main__': # test
    import random as rnd

    r = int(input("longueur tableau : "))
    t = [i for i in range(r)]
    #t.sort()
    print(t)

    e = int(input("élément à chercher : "))
    
    index = BinarySearch(t, e, t)

    print("Position trouvée de l'élément :",index)
