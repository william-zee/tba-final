"Importation des autres fichiers pour lancer le jeu"
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from characters import Characters
from portail import Portail

class Game:
    """
        Initializes the Game class with default values:
        - The game is not finished.
        - Empty lists for rooms and portals.
        - Empty dictionaries for commands, inventory, and characters.
        - No player initialized.
        """
      # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.inventory={}
        self.characters={}
        self.portails = []
    # Setup the game
    def setup(self):
        """
        Configure the initial game commands.

        This method initializes the game's available setup.
        """
        self.setup_commands()
        self.setup_rooms()
    # Setup commands
    def setup_commands(self):
        """"
        This method initializes the game's available commands by creating 
        instances of the Command, adding them to the `self.commands` dictionary.
        """
        aider = Command("aider", " : afficher cette aide", Actions.help, 0)
        self.commands["aider"] = aider
        quiter = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quiter
        go = Command("go","<direction>:se déplacer dans une direction (N, E, S, O)",Actions.go,1)
        self.commands["go"] = go
        back=Command("back"," : retourne en arrière",Actions.back, 0)
        self.commands["back"] = back
        look=Command("look"," :regarde il y a :",Actions.look, 0)
        self.commands["look"] = look
        take=Command("take"," : prend l'object :",Actions.take, 1)
        self.commands["take"] = take
        drop=Command("drop"," : dépose l'object :",Actions.drop, 1)
        self.commands["drop"] = drop
        talk=Command("Talk"," : tu peux discuter avec le personnage :",Actions.talk, 1)
        self.commands["talk"] = talk
        get_history=Command("get_history"," : tu peux voir ton historique :",Actions.get_history, 0)
        self.commands["get_history"] = get_history
        get_inventory=Command("get_inventory",":voir ton inventaire:",Actions.get_inventory,0)
        self.commands["get_inventory"] = get_inventory
        #Setup Room
    def setup_rooms(self):
        """"
        This method initializes the game's available rooms by creating 
        instances of the Command, adding them to the `self.rooms` dictionary.
        """
        forest = Room("Forest", " Une forêt avec une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tunnel = Room("tunnel", " un tunnel sinueux,seule ta détermination te sortira indemne.")
        self.rooms.append(tunnel)
        escalier= Room("escalier", " un escalier mystérieux qui s'élève ou s'enfonce dans l'obscurité.")
        self.rooms.append(escalier)
        toura = Room("Tour aux astuces", "un défi où chaque étage cache des pièges, des énigmes")
        self.rooms.append(toura)
        swamp = Room("Swamp", " un marécage sombre et ténébreux,les abords sont vaseux.")
        self.rooms.append(swamp)
        ile = Room("ile", " une île isolée, l’épreuve de cuisine")
        ruelle = Room("ruelle", " une ruelle sombre et sans issue.")
        self.rooms.append(ruelle)

    #SETUP OBJECTS

        canapeche=Item("canapeche","La canne à pêche: la meilleur arme",3)
        ile.add(canapeche)
        passhunter=Item("pass","Titre de Hunter: La récompense ultime",3)
        toura.add(passhunter)

    #SETUP Personnage
        mamie=Characters(
            "Mamie",
            "Une vieille accompagnée de gardes",
            ruelle,
            ["Voici l'énigme: Qui souhaites tu sauver entre ta bien-aimée et ta mère"]
            )
        ruelle.characters[mamie.name] = mamie
        examinateur =Characters(
            "Examinateur",
            "Il vous surveille",
            toura,
            ["Regarde autour de toi"])
        toura.characters[examinateur.name] = examinateur
    # Create exits for rooms
        forest.exits = {"N" : None, "E" : swamp, "S" : None, "O" : None,"U" : escalier,"D" :None}
        toura.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"U" : None,"D" :ile}
        ile.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"U" : toura,"D" :escalier}
        swamp.exits = {"N" : None, "E" : None, "S" : None, "O" : forest,"U" : None,"D" :None}
        escalier.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"U" : ile,"D" :forest}
        ruelle.exits = {"N" : tunnel, "E" : None, "S" : None, "O" : None,"U" : None,"D" : None }
        tunnel.exits = {"N" : escalier, "E" : None, "S" : None, "O" : None,"U" : None,"D" :None}

    #Setup time warps
        salle2 = Portail(False)
        self.portails.append(salle2)
    #Create time warps for rooms
        tunnel.portails = salle2
        #escalier.portails = Salle3
        #forest.portails= Salle4
        #ile.portails = Salle5
    # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = ruelle

    # Play the game

    def play(self):
        "Fais appel aux méthodes setup et print_welcome"
        self.setup()
        self.print_welcome()
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        "Permet détecter si une commande est autorisée ou non"
        if not command_string:
            return None
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}'non reconnue. Entrez 'help'.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
        return "Commande traitée"
    # Print the welcome mesage
    def print_welcome(self):
        "Fonction permettant d'accueillir le joueur avec un message"
        print(f"\nBienvenue {self.player.name}, à l'Examen des Hunters!")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description()) 
def main():
    "Fonction main permettant d'éxécuter le jeu"
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
