"""
Ce module définit la classe Room, utilisée pour représenter une pièce dans un jeu.
Chaque pièce peut avoir un nom,une description,des sorties,des objets,des personnages.
"""
from characters import Characters

class Room:
    """
        Cette classe représente une pièce dans le jeu.
Une pièce a un nom, une description, des sorties, des objets, des personnages,.
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.objet= {}
        self.characters= {}
        self.portails=None

    # Define the get_exit method.
    def get_exit(self, direction):
        """
    Retourne la salle dans la direction donnée si elle existe.
    
    Arguments:
        direction (str): La direction à vérifier pour une sortie (par exemple, 'nord', 'sud', etc.).
    
    Retourne:
        Room ou None: La salle dans la direction donnée ou None si aucune sortie n'existe.
    """

        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        return None
    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties de la salle.

        Retourne:
            str: Une chaîne listant toutes les sorties disponibles dans la salle.
        """
        exit_string = "Sorties: "
        exits = []  # Créer une liste pour stocker les sorties

        # Itérer directement sur le dictionnaire des sorties
        for exit_key in self.exits:
            if self.exits.get(exit_key) is not None:
                exits.append(exit_key)  # Ajouter la sortie à la liste

        # Joindre les sorties avec une virgule et un espace, puis ajouter cela à exit_string
        exit_string += ", ".join(exits)

        return exit_string
    # Return a long description of this room including exits.
    def get_long_description(self):
        """
    Retourne une description longue de la salle incluant ses sorties et ses personnages.
    
    Retourne:
        str: Une description longue de la salle avec ses sorties et ses personnages.
    """
        return f"Vous êtes dans{self.description}\n{self.get_exit_string()}\n{self.personnages()}"

    def add(self,item):
        """
    Ajoute un objet à la salle.
    
    Arguments:
        item (Item): L'objet à ajouter à la salle.
    """
        self.objet[item.name]= item

    def get_object_lieu(self):
        """
    Retourne une chaîne décrivant les objets dans la salle.
    
    Retourne:
      list tous les objets dans la salle ou un message indiquant que la salle est vide.
    """
        if not self.objet:
            return "Votre salle est vide."
        object_string = "Il y a les items suivants :\n"
        items = [f"  - {item}" for item in self.objet.values()]  # Utilisation d'une liste pour stocker les items
        object_string += "\n".join(items)  # Utilisation de str.join pour concaténer les éléments
        return object_string
        

    def personnages(self):
        if not self.characters:
            return "il n'y a pas de pnj"
        else:
            pnj = "il y a les personnages :\n"
            for characters in self.characters.values():
                pnj += f"\n  - {characters.name}  {characters.description} , personnage {characters.status}"
            return pnj