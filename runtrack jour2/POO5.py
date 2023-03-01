class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50
        
    def set_marque(self, marque):
        self._marque = marque
        
    def get_marque(self):
        return self._marque
    
    def set_modele(self, modele):
        self._modele = modele
        
    def get_modele(self):
        return self._modele
    
    def set_annee(self, annee):
        self._annee = annee
        
    def get_annee(self):
        return self._annee
    
    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage
        
    def get_kilometrage(self):
        return self._kilometrage
    
    def demarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True
        else:
            print("Le réservoir est presque vide, veuillez faire le plein avant de démarrer.")
            
    def arreter(self):
        self._en_marche = False
        
    def _verifier_plein(self):
        return self._reservoir
        
voiture1 = Voiture("BMW", "i8", 2022, 0)
print("Marque :", voiture1.get_marque())
print("Modèle :", voiture1.get_modele())
print("Année :", voiture1.get_annee())
print("Kilométrage :", voiture1.get_kilometrage())

voiture1.demarrer()
print("La voiture est en marche :", voiture1._en_marche)
voiture1.arreter()
print("La voiture est en marche :", voiture1._en_marche)