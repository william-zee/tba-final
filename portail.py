
""" Module qui définit la classe Portail. """

class Portail:
    """Classe représentant un portail avec un statut d'ouverture."""

    def __init__(self, open_status):
        """Initialise le portail avec un statut d'ouverture."""
        self.open_status = open_status

    def ouvrir(self):
        """Ouvre le portail."""
        self.open_status = True

    def fermer(self):
        """Ferme le portail."""
        self.open_status = False
