class Personnage:

    plateau = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        if self.y > 0 and self.plateau[self.x][self.y - 1] == 0:
            self.y -= 1

    def droite(self):
        if self.y < 2 and self.plateau[self.x][self.y + 1] == 0:
            self.y += 1

    def bas(self):
        if self.x > 0 and self.plateau[self.x - 1][self.y] == 0:
            self.x -= 1


    def haut(self):
        if self.x < 2 and self.plateau[self.x + 1][self.y] == 0:
            self.x += 1

    def position(self):
        pos = (self.x, self.y)
        print(pos)


p = Personnage()
p.droite()
p.gauche()
p.haut()
p.bas()
p.position()