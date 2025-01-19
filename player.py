"Fichier Player"
class Player():
    "Classe Player qui définit toutes les méthodes et les attributs du joueur"
    # Define the constructor.
    def __init__(self, name,starting_room=None):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.has_looked = False
        self.scan_status = 0

        if starting_room is not None:
            self.history.append(starting_room)
    # Define the move method.
    def can_move_to(self, next_room):
        """
        Vérifie si le joueur peut se déplacer vers la salle donnée en fonction des objets
        ou conditions spéciales requises.

        Arguments:
            next_room (Room): La salle vers laquelle le joueur souhaite se déplacer.

        Retourne:
            bool: True si le joueur peut se déplacer, False sinon.
        """
        if self.current_room.name == 'ile':
            # Exemple pour la salle 'ile' : le joueur doit posséder une canne à pêche.
            if not any(item == "canapeche" for item in self.inventory):
                print("Vous devez avoir une canne à pêche pour accéder à cette direction depuis 'île'.")
                return False

    # Ajouter ici d'autres vérifications pour d'autres salles et conditions
        return True

    def move(self, direction):
        "Méthode permettant de faire déplacer le joueur"

        # Vérifie si le joueur est dans une pièce.
        if self.current_room is None:
            print("Vous n'êtes dans aucune pièce pour commencer.")
            return False

        # Vérifie si la direction existe dans les sorties de la pièce actuelle.
        if direction not in self.current_room.exits:
            print(f"\nAucune porte dans cette direction : {direction} !\n")
            return False

        # Récupère la pièce suivante à partir des sorties.
        next_room = self.current_room.exits[direction]

        # Si la pièce suivante est None, afficher une erreur.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        #Vérifie si il peut accéder à la prochaine room en ayant l'item en question
        if not self.can_move_to(next_room):
            return False
        # Si la pièce actuelle est "ruelle", vérifie si la direction mène à une salle bloquée.
        if self.current_room.name == 'ruelle':
            if hasattr(next_room, 'portails') and next_room.portails.open_status is False:
                print("\nLa Salle menant à cette direction est bloquée depuis 'ruelle'.\n")
                return False
        
        # Si tout est ok, ajoute la pièce actuelle à l'historique.
        self.history.append(self.current_room)

        # Déplace le joueur dans la nouvelle pièce.
        self.current_room = next_room

        # Affiche la description détaillée de la nouvelle pièce.
        print(self.current_room.get_long_description())
        return True

    def get_inventory(self):
        "Méthode permettant de regarder son inventaire"
        # sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        # self.inventory["sword"] = sword
        if not self.inventory:
            return "Votre inventaire est vide."
        inventory_description = "Vous disposez des items suivants :\n"
        for name,item in self.inventory.items():
            inventory_description += f"  - {name} : {item}\n"
        return inventory_description
    def get_history(self):
        "Méthode permettant de voir son"
        if not self.history:
            return "Aucune pièce visitée pour le moment."
        history_s="vous avez visité"
        for room in self.history:
            history_s+= f"{room.description}"
        return history_s
