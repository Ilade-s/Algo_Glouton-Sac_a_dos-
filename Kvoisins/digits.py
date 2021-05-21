#
# Module de récupération des nombres manuscrits
#

import matplotlib.pyplot as plt
import csv

#
# fonction de lectures des nombres manuscrits :
#
def lire(file):
    """ fonction de lectures des nombres manuscrits à partir d'un fichier CSV
    chiffre = lire(file)
    Arguments :
    -----------
    file  : string
        mon du fichier CSV contenant les 1797 données
        65 integer par ligne : 
            1er int classe du chiffre (0 à 9)
            64 int suivants codage des pixels formant le chiffre
                image de taille 8X8 pixels et 17 Niveaux de gris (0 à 16)
        
    Sorties:
    --------
    chiffre : list de list de int : format [[int,int, ... ,int],[init,int,init ...], ... , [init,init ...,int]]
        liste des nombres contenu dans le fichier CSV
        chaque élément de la liste représente un nombre :
         [classe,int,init ... init]
            1er élement représente la classe du chiffre 0 à 9
            64 éléments suivants les 8X8 pixels représentant le chiffre en niveaux de gris codés de 0 à 16
    """

    #ouverture en lecture 
    f = open(file,"r",encoding="utf-8")
    lecteur = csv.reader(f,delimiter=",")
    liste = []
    #Pour chaque digit, recuperer le nombre en int et 
    for digit in lecteur:
        num = [int(i) for i in digit]
        liste.append(num)
    f.close
    return liste

#
# fonction de dessin d'un chiffre manuscrit
#
def plot(image_digit) :
    """ affiche dans une fenetre graphique le chiffre représenté dans image_digit
    plot(image_digit)
    Arguments :
    -----------
    imag_digit : list de 65 integer  
            1er int classe du chiffre (0 à 9)
            64 int suivants codage des pixels formant le chiffre
                image de taille 8X8 pixels et 17 Niveaux de gris (0 à 16)
        
    Sorties:
    --------
        Néant
    """

    image =[]
    for i in range(8):
        image.append(image_digit[i*8+1:(i+1)*8+1])
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax = plt.gca()
    ax.set_title('Nombre: %i' % image_digit[0])
    plt.show()
    
if __name__ == "__main__":
    digits = lire("digits.csv")
    print(digits[300])
    plot(digits[300])