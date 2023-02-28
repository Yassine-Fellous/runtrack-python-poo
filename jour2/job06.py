class Commande:

    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats_commandes = []
        self.__statut = "En cours"

    def get_num_commande(self):
        return self.__num_commande

    def get_plats_commandes(self):
        return self.__plats_commandes

    def get_statut(self):
        return self.__statut

    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande

    def set_plats_commandes(self, plats_commandes):
        self.__plats_commandes = plats_commandes

    def set_statut(self, statut):
        self.__statut = statut