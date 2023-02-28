class cercle:

    def __init__(self):
        self.rayon = 0
        self.recirc = 0
        self.air = 0
        self.diam = 0

    def changerRayon(self, rayon):
        self.rayon = rayon

    def aire(self):
        self.air = 3.14 * self.rayon ** 2

    def diametre(self):
        self.diam = self.rayon * 2

    def ciconférence(self):
        self.recirc = 2 * 3.14 * self.rayon

    def afficherinfos(self):
        self.aire()
        self.diametre()
        self.ciconférence()
        print("rayon =", self.rayon, "circonférence =", self.recirc, "air =", self.air, "diametre =", self.diam)


cercle1 = cercle()
cercle1.changerRayon(4)
cercle1.afficherinfos()