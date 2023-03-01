class Student:
    def __init__(self,nom,prenom,num_etu,credits=0):
        self.__nom = nom
        self.__prenom = prenom 
        self.__num_etu = num_etu
        self.__credits = credits
        self.__level = self._studentEval()
    def add__credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self._studentEval()
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")
    def get_credits(self):
        return self.__credits
    def _studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Id :", self.__num_etu)
        print("Niveau :", self.__level)

john_doe = Student("Doe", "John", 145)
john_doe.add__credits(65)
john_doe.studentInfo()

john_doe.add__credits(20)
john_doe.studentInfo()

john_doe.add__credits(5)
john_doe.studentInfo()

