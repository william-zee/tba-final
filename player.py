"Fichier Player" 
import random

class Player():
    "Classe Player qui définit toutes les méthodes et les attributs du joueur"
    # Define the constructor.
    def __init__(self, name,starting_room=None):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.has_looked = False
        self.recuperer=False
        self.scan_status=0

        if starting_room is not None:
            self.history.append(starting_room)
    # Define the move method.
    def can_move_to(self, next_room,direction):
        """
        Vérifie si le joueur peut se déplacer vers la salle donnée en fonction des objets
        ou conditions spéciales requises.

        Arguments:
            next_room (Room): La salle vers laquelle le joueur souhaite se déplacer.

        Retourne:
            bool: True si le joueur peut se déplacer, False sinon.
        """
        next_room = self.current_room.exits[direction]
        if self.current_room.name == 'ile' and next_room.name=='Tour aux astuces':
            # Exemple pour la salle 'ile' : le joueur doit posséder une canne à pêche.
            if not any(item == "canapeche" for item in self.inventory):
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
        next_room = self.current_room.get_exit(direction)
        # Si la pièce suivante est None, afficher une erreur.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Vérifie si le joueur peut se déplacer vers la prochaine salle.
        if not self.can_move_to(next_room, direction):
            print("Vous ne pouvez pas vous déplacer vers cette salle pour le moment.")
            return False

        # Si la pièce actuelle est "ruelle", vérifie si la direction mène à une salle bloquée.
        if self.current_room.name == 'ruelle' and \
            hasattr(next_room, 'portails') and \
            next_room.portails.open_status is False:
            print("\nLa Salle menant à cette direction est bloquée depuis 'ruelle'.\n")
            return False

        # Ajoute la pièce actuelle à l'historique.
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
        "Méthode permettant de voir son historique"
        if not self.history:
            return "Aucune pièce visitée pour le moment."
        history_s="vous avez visité"
        for room in self.history:
            history_s+= f"{room.description}"
        return history_s


# la aussi changer
    def combat(self, characters):
        """ Méthode pour le combat avec un ennemi. """
        print(f"Vous êtes face à {characters.name}! Une chance sur 3 de survivre si vous attaquez.")

        # Demande à l'utilisateur d'attaquer.
        action = input("(Écrivez 'attack' pour attaquer) ou autre pour fuir: ").strip().lower()

        if action == "attack":
            # Génère un nombre aléatoire pour déterminer si le joueur survit (1 chance sur 3).
            chance = random.randint(1, 3)  # Génère un nombre entre 1 et 3

            if chance != 3 :
                print("Vous avez réussi à vaincre l'ennemi ! Allez vers la prochaine salle.")
                print("Vous avez réussi à vaincre Hisoka, la canapeche est à vous.")
                self.recuperer=True
                return True  # Le joueur gagne, il peut passer à la prochaine salle

            print("C'est perdu. L'ennemi vous a vaincu.")
            return False  # Le joueur perd

        print("Vous avez choisi de ne pas attaquer. Vous avez perdu votre chance.")
        return False  # Le joueur n'attaque pas et perd le combat
