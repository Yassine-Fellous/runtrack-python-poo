class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = self.dec()
        self.agios()

    def dec(self):
        if self.__solde < 0:
            return True
        else:
            return False

    def afficher(self):
        print("numéro =", self.__numero, "\n",
              "nom =", self.__nom, "\n",
              "prenom =", self.__prenom, "\n",
              "solde =", self.__solde)

    def afficherSolde(self):
        print("solde =", self.__solde, "\n")

    def versement(self, vers):
        if vers > 0:
            self.__solde = vers + self.__solde

    def retrait(self, ret_integer):
        if ret_integer <= self.__solde:
            self.__solde = self.__solde - ret_integer

    def agios(self):
        if self.dec():
            agio = self.__solde * 0.15
            self.__solde = self.__solde - agio

    def virement(self, mont, dest):
        if mont > 0:
            self.__solde = self.__solde - mont
            dest.versement(mont)


compte = CompteBancaire("12345", "Dupont", "Jean", 1000)
compte.afficher()
compte.afficherSolde()
compte.versement(500)
compte.afficherSolde()
compte.retrait(200)
compte.afficherSolde()

compte2 = CompteBancaire("67890", "Martin", "Marie", -500)

compte.afficherSolde()
compte2.afficher()

compte.virement(500, compte2)

compte.afficherSolde()
compte2.afficher()