"""
Algorithme de résolution approchée du problème du sac à dos :
    - ne donnera pas toujours la solution optimale, mais une solution acceptable
"""
from random import randint

def Solution(objets, W):
    """
    Selon une liste d'objets avec une valeur et un poids, renvoie une solution approchée permettant la plus grande valeur possible dans le sac (avec un poids donné)
    
    PARAMETRES :
        - objets : list[list[poids: int, valeur: int]]
            - liste des objets disponibles
        - W : int
            poids maximal du sac

    SORTIE : 
        - solution : list[list[poids: int, valeur: int]]
            - liste d'objets à mettre dans le sac
    """
    # Evalution rapport valeur/poids
    def Getkey(obj):
        return (obj[1]/obj[0])
    objs = sorted(objets,key=Getkey,reverse=True)
    # boucle d'ajout des objets
    iW = 0
    solution = []
    for obj in objs:
        (w,p) = obj
        if w+iW<=W:
            iW += w
            solution.append(obj)
        else:
            return solution
    
    return solution

def main():
    objets = [[12,4],[2,2],[1,1],[4,10],[1,2]]
    W = 15

    nobjets = int(input("nombre d'objets : "))
    objets = [[randint(1,20),randint(1,20)] for i in range(nobjets)]
    W = int(input("poids maximal : "))
    print(objets)
    print("poids maximal :",W)

    sol = Solution(objets,W)

    print("Solution :",sol)

    vtotale = sum([i[1] for i in sol])
    pfinal = sum([i[0] for i in sol])

    print("Valeur totale :",vtotale)
    print("poids final :",pfinal)



if __name__=='__main__': # test
    main()