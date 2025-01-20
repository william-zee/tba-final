"""
importer le module random pour faire une réaslisation aléatoire
    """
import random
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
class Characters:
    """
    Représente un personnage dans un jeu. Chaque personnage a un nom, une description,
    un message qu'il peut dire, et un historique des messages qu'il a dits. Il peut se déplacer
    entre les salles et répéter ses messages lorsqu'il n'en a plus à dire.
    
    Attributes:
        name (str): Le nom du personnage.
        description (str): La description du personnage.
        current_room (Room): La salle dans laquelle se trouve le personnage.
        msg (list): Liste des messages que le personnage peut dire.
        msg_history (list): Historique des messages déjà affichés.
    """
    def __init__(self, name, description,current_room,msg,status):
        """
        Initialise un personnage avec un nom, une description, une salle et un messages.
        
        Arguments:
            name (str): Le nom du personnage.
            description (str): La description du personnage.
            current_room (Room): La salle où se trouve le personnage.
            msg (list): Liste des messages que le personnage peut dire.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msg = msg
        self.msg_history = []
        self.status= status
    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du personnage,
        avec son nom, sa description et son message actuel.
        
        Retourne:
            str: Une chaîne formatée représentant le personnage.
        """
        return f"{self.name} : {self.description} ({self.msg}, {self.status})"

    def move(self):
        """
        Permet au personnage de se déplacer aléatoirement dans une salle adjacente, 
        si une telle salle existe. Si aucune salle adjacente n'est disponible, 
        il reste dans sa salle actuelle.
        """

        l = ["Reste", "Deplace"]
        resultat = random.choice(l)


        if resultat == "Deplace":
            adjacent_rooms = [room for room in self.current_room.exits.values() if room is not None]

            if adjacent_rooms:
                next_room = random.choice(adjacent_rooms)
                del self.current_room.characters[self.name]
                self.current_room = next_room
                self.current_room.characters[self.name] = self
                print(f"{self.name} s'est déplacé dans {self.current_room.name}.")
            else:
                print(f"{self.name} ne peut pas se déplacer, aucune sortie disponible.")
        else:
            print(f"{self.name} ne se déplace pas.")
    # def follow(self,game):
    #     """
    #     Permet au personnage de se déplacer aléatoirement dans une salle adjacente,
    #     si une telle salle existe. Si aucune salle adjacente n'est disponible,
    #     il reste dans sa salle actuelle.
    #     """
    #     next_room = game.player.next_room
    #     del self.current_room.characters[self.name]
    #     self.current_room = next_room
    #     self.current_room.characters[self.name] = self
    #     print(f"{self.name} s'est déplacé dans {self.current_room.name}.")
    def get_msg(self):
        """
        Permet au personnage de dire un message. Le message est retiré de la liste `msg` et 
        ajouté à l'historique des messages. Si tous les messages ont été dits, l'historique 
        est réinitialisé et les messages recommencent depuis le début.
        """
        if len(self.msg) > 0:
        # Récupérer et afficher le premier message
            msg = self.msg.pop(0)  # pop(0) retire et retourne le premier message
            self.msg_history.append(msg)  # Ajouter à l'historique des messages affichés
            print(f"{self.name} dit : {msg}")
            return msg  # Retourne le message

    # Si tous les messages ont été affichés, recommencer
        print(f"{self.name} n'a plus rien à dire, les messages vont recommencer.")
        self.msg = self.msg_history.copy()  # Recommencer à partir de l'historique des messages
        self.msg_history = []  # Réinitialiser l'historique
        return self.get_msg()  # Relancer la méthode pour afficher le premier message à nouveau
