class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getPages(self):
        return self.__pages
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas etait emprunté.")
init = Livre("Ubu Roi","Alfred Jarry",234)
print("l'auteur de",init.getTitre(),"est",init.getAuteur(),"son nombre de pages est",init.getPages(),"le livre est")
print(init.verification()) 
init.emprunter() 
print(init.verification())
init.emprunter() 
init.rendre() 
print(init.verification()) 
init.rendre() 