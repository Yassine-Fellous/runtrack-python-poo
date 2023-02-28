class Point:
    def __init__(self):
        self.x = 132
        self.y = 164

    def afficherLespoint(self):
        print(" x =",self.x,"et y =",self.y)

    def afficherx(self):
        print(" x =",self.x)

    def affichery(self):
        print(" y =",self.y)

    def changerx(self, x):
        self.x = x

    def changery(self, y):
        self.y = y





Point1 = Point()
Point1.afficherLespoint()
Point1.changerx(564)
Point1.changery(664)
Point1.afficherx()
Point1.affichery()


