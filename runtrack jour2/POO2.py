class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getPages(self):
        return self.__pages
    def setTitres(self,titre):
        self.__titre = titre
    def setAuteur(self,auteur):
        self.__auteur = auteur
    def setPages(self,pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Le nombre de pages doit être un entier positif.")
        
init = Livre("Ubu Roi","Alfred Jarry",234)
print("l'auteur de",init.getTitre(),"est",init.getAuteur(),"son nombre de pages est",init.getPages())
init.setAuteur("Albert Camus")
init.setTitres("L'étranger")
init.setPages(159)
print("l'auteur de",init.getTitre(),"est",init.getAuteur(),"son nombre de pages est",init.getPages())