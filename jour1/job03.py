class Opération:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        print(self.nombre1 + self.nombre2)




Opération1 = Opération(1, 2)
Opération1.addition()