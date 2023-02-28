class Student:
    def __init__(self, nom, prenom, num_etu):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etu = num_etu
        self.__credit = 0
        self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credit >= 90:
            return "excelent"
        elif self.__credit >= 80:
            return "tres bien"
        elif self.__credit >= 70:
            return "bien"
        elif self.__credit >= 60:
            return "passable"
        elif self.__credit < 60:
            return "insuffisant"


    def studenInfo(self):
        print("Nom =", self.__nom, "\n",
              "prenom =", self.__prenom, "\n",
              "id =", self.__num_etu, "\n",
              "Niveau =", self.__level)

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_num_etu(self):
        return self.__num_etu

    def get_credit(self):
        return self.__credit

    def set_credit(self, credit):
        if credit > 0:
            self.__credit = credit
            self.__level = self.__studentEval()
        else:
            print("les crédit négatif ne sont pas disposible")

etudiant1 = Student("John", "Doe", 145)
print("le nombre de crédits de", etudiant1.get_nom(), etudiant1.get_prenom(), "est de", etudiant1.get_credit())
etudiant1.set_credit(100)
print("le nombre de crédits de", etudiant1.get_nom(), etudiant1.get_prenom(), "est de", etudiant1.get_credit())
etudiant1.studenInfo()