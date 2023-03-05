class factorielle:
    def __init__(self, entier):
        self.entier = entier

    def calcul_fact(self):
        n = self.entier
        if n == 0:
            return 1
        else:
            return n * factorielle(n - 1).calcul_fact()

fact1 = factorielle(5)
print(fact1.calcul_fact())