class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""


    def age_a(self):
        print("l'age de l'animal", self.age,"ans")

    def viellir(self):

        self.age += 1

    def nommer(self, nom):
        self.nom = nom
        print("l'animal se nomme", self.nom)


Animal1 = Animal()
Animal1.age_a()
Animal1.viellir()
Animal1.nommer("Abdel")
Animal1.age_a()
