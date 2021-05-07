""" Implémentation simple du rendu monnaie (pas de limite de nombre de pièces/billets)
"""

def RenduMonnaie(p,a,pieces):
    """
    Algorithme permettant de résoudre un problèmle de rendu monnaie

    PARAMETRES :
        - p : int
            - prix
        - a : int
            - argent donné par le client
        - pieces : list/tuple (iterable)
            - liste des pieces/billets possibles pour le rendu
    
    SORTIE :
        - rendu : list
            - liste des pièces/billets rendus (le - possible)
    """
    rendu = []
    # vérif si prix égal ou inférieur au prix (pas de rendu)
    r = a-p
    if r<=0: return rendu
    # sinon calcule le rendu
    plist = sorted(pieces,reverse=True)
    while sum(rendu)<r: # boulce d'ajout des pieces
        for i in plist:
            if i<=r-sum(rendu):
                rendu.append(i)
                break
    
    return rendu

if __name__=='__main__': # test
    prix = int(input("prix : "))
    argent = int(input("Argent donné par le client : "))
    pieces = [1, 2, 5, 10, 20, 50, 100, 200, 500]

    rendu = RenduMonnaie(prix, argent, pieces)

    print(f"Pieces à rendre : {rendu}")