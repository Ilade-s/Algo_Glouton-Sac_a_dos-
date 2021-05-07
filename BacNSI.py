"""
Programmes du sujet du Bac 2021 NSI
"""

def convertir(T):
    """T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. 
    Renvoie l'écriture décimale de l'entier positif dont la représentation binaire 
    est donnée par le tableau T
    
    PARAMETRES :
        - T : list
            - liste des bits représantant le nombre non signé
    
    SORTIE :
        - n : int
            - entier décimal de T
    """
    n = 0
    for ib in range(len(T)):
        n += 2**(len(T)-ib-1)*T[ib]
    
    return n

def tri_insertion(L):
    """
    Algorithme de tri insertion à compléter
    """
    n = len(L)
    # cas du tableau vide
    if n==0:
        return L
    for j in range(1,n):
        e = L[j]
        i = j
        # A l'étape j, le sous-tableau L[0,j-1] est trié
        # et on insère L[j] dans ce sous-tableau en déterminant
        # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
        while i > 0 and L[i-1] > L[j] and i <= j:
            i = i+1
        # si i != j, on décale le sous tableau L[i,j-1] d’un cran
        # vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j,i,-1):
                L[k] = L[k-1]
            L[i] = L[j]
        print(L)
    return L

def main():
    print("conversion binaire/décimal :")
    # 83
    T = [1, 0, 1, 0, 0, 1, 1]
    n = convertir(T)
    print(f"binaire : {T}")
    print(f"nombre : {n}")
    # 130
    T = [1, 0, 0, 0, 0, 0, 1, 0]
    n = convertir(T)
    print(f"binaire : {T}")
    print(f"nombre : {n}")

if __name__=='__main__': # test
    #main()
    sl = tri_insertion([2,5,-1,7,0,28])
    print(f"Liste triée : {sl}")