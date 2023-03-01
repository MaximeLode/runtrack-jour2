class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def get_longueur(self):
        return self.__longueur
    def set_longueur(self,longueur):
        self.__longueur = longueur
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self,largeur):
        self.__largeur = largeur
init = Rectangle(10,5)
print("longueur =", init.get_longueur())
print("largeur =", init.get_largeur())
init.set_longueur(15)
init.set_largeur(7)
print("longueur =", init.get_longueur())
print("largeur =", init.get_largeur())