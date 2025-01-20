"""" on utilise MSG0="\nLa commande'{command_word}'ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1="\nLa commande'{command_word}'prend 1 seul paramètre.\n"
"""
from player import Player
# Description: The actions module.

#The actions module contains the functions that are called when a command is executed.
#Each function takes 3 parameters:
# -game: the game object
# -list_of_words: the list of words in the command
# -number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
# The error message is stored in the MSG0 and MSG1 variables and formatted.
# The MSG0 variable is used when the command does not take any parameter.
MSG0="\nLa commande'{command_word}'ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1="\nLa commande'{command_word}'prend 1 seul paramètre.\n"
""" 
on définit la class action pour mettre les mouvement pouvant etre effectuer 
"""
class Actions:
    """
        définition des actions effectuers
            
    
        """
    # pylint: disable=no-self-argument :
    def go(game, list_of_words, number_of_parameters):
        """
        Déplace le joueur dans la direction spécifiée par le paramètre.
        Le paramètre doit être une direction cardinale (N, E, S, O).

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        Exemples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False
        """
        player = game.player
        l = len(list_of_words)

        # Si le nombre de paramètres est incorrect, afficher un message d'erreur et retourner False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Obtenir la direction de la liste des mots.
        direction = list_of_words[1].upper()
        if direction == 'NORD':
            direction = 'N'
        elif direction == 'SUD':
            direction = 'S'
        elif direction == 'EST':
            direction = 'E'
        elif direction == 'OUEST':
            direction = 'O'
        valideok = {'N', 'S', 'E', 'O', 'U', 'D', 'SUD', 'OUEST', 'EST', 'NORD'}

        if direction not in valideok:
            print("Direction invalide, veuillez entrer une nouvelle commande.")
            return False  # Retourner False si la direction est invalide.

        # Déplacer le joueur dans la direction spécifiée par le paramètre.
        player.move(direction)
        # Si le joueur est dans la salle "tunnel", ouvrir le portail correspondant.
        if player.current_room.name == 'tunnel':
            game.portails[player.scan_status].open_status = True
            player.scan_status += 1
        return True  # Retourner True si tout se passe bien

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    def back(game, list_of_words, number_of_parameters):
        """
        Déplace le joueur dans la derniere salle
            
    
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        y=game.player.history
        # Revenir à la pièce précédente
        if len(y) == 0:
            print("Impossible de revenir en arrière, aucun historique.")
            return False

        # Revenir à la pièce précédente dans l'historique
        player=game.player
        if game.portails[player.scan_status-1].open_status is False :
            print("\nLa Salle menant à cette direction est bloquée\n")
            return False
        player.history=y.pop()
        player.current_room = player.history[-1]
        print("Vous êtes de retour dans ", player.current_room.name)
        return True

    def look(game, list_of_words, number_of_parameters):
        """
        regarde les objets de la salle
            
    
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        y= game.player.current_room.get_object_lieu()
        print(y)
        game.player.has_looked = True
    def take(game, list_of_words, number_of_parameters):
        """
        Prend l'objet  avec un argument nécessaire
            
    
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if not game.player.has_looked:
            print("Vous devez d'abord faire 'look' avant de pouvoir prendre un objet.")
            return False
        # if  True:
        #     print(f"Tentative de prise de l'objet {list_of_words[1]}")
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        else:
            if list_of_words[1] in game.player.current_room.objet.keys():
                item_name1 = list_of_words[1]
                itemfrom = game.player.current_room.objet[item_name1]
                game.player.inventory[item_name1] = itemfrom
            # print(game.player.inventory)
                del game.player.current_room.objet[list_of_words[1]]
                if 'pass' in game.player.inventory:
                    print('\nBravo vous êtes devenus un véritable hunter')
                    game.finished=True
                    return True
            else:
                print("Entrez un objet Valide")

    def drop(game, list_of_words, number_of_parameters):
        """
        Dépose l'objet  avec un argument nécessaire
            
    
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        else:
            if list_of_words[1] in game.player.inventory.keys():
                item_name = list_of_words[1]
                item_from_inventory = game.player.inventory[item_name]

                game.player.current_room.objet[item_name] = item_from_inventory
                print(f"Vous avez jetté {list_of_words[1]}.")
                del game.player.inventory[list_of_words[1]]
            else:
                print("Entrez un objet valide")
    def combat(self, characters):
        """ Méthode pour le combat avec un ennemi. """
        print(f"Vous êtes face à {characters.name}! Une chance sur 3 de survivre si vous attaquez.")
        
        # Demande à l'utilisateur d'attaquer.
        action = input("Que voulez-vous faire ? (Écrivez 'attack' pour attaquer) ").strip().lower()

        if action == "attack":
            # Génère un nombre aléatoire pour déterminer si le joueur survit (1 chance sur 3).
            chance = random.randint(1, 3)  # Génère un nombre entre 1 et 3

            if chance != 3 :
                print("Vous avez réussi à vaincre l'ennemi ! Vous pouvez continuer vers la prochaine salle.")
                return True  # Le joueur gagne, il peut passer à la prochaine salle
            else:
                print("C'est perdu. L'ennemi vous a vaincu.")
                return False  # Le joueur perd
        else:
            print("Vous avez choisi de ne pas attaquer. Vous avez perdu votre chance.")
            return False  # Le joueur n'attaque pas et perd le combat

    def talk(game, list_of_words, number_of_parameters):
        """
        Parle au PNJ avec un argument nécessaire
        """
        player = game.player
        l = len(list_of_words)

        # Vérifier que la commande a bien un seul paramètre (le nom du PNJ)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"\nLa commande '{command_word}' prend 1 paramètre.\n")
            return False

        # Récupérer le nom du personnage à qui parler
        character_name = list_of_words[1]

        # Chercher le personnage dans la pièce actuelle du joueur
        player_room = game.player.current_room

        if character_name in player_room.characters:
            character = player_room.characters[character_name]

            # Cas spécifique pour Mamie
            if character_name == 'Mamie':
                # Vérifier si la conversation est déjà terminée
                if hasattr(character, 'conversation_done') and character.conversation_done:
                    print("Mamie ne souhaite plus discuter. Elle a terminé sa conversation.")
                    return True  # La conversation est terminée, donc on ne refait rien

                print(f"Le joueur parle à {character_name}")
                character.get_msg()  # Afficher le message du personnage
                response = input("\nQuelle est votre réponse?: ")

                # Si la réponse est vide, débloque un portail et marque la conversation comme terminée
                if response == "":
                    print("Bravo, vous avez donné la bonne réponse, allez au nord.")
                    game.portails[player.scan_status].open_status = True
                    character.conversation_done = True  # Marquer que la conversation est terminée
                    return True
                else:
                    print("Ce n'est pas la bonne réponse. Mamie vous met un mawashi geri\nGameOver")
                    game.finished = True  # Mettre fin au jeu si la réponse est incorrecte
                    return False

            # Cas pour Hisoka (le combat)
            elif character_name == 'Hisoka':
                print(f"Le joueur parle à {character_name}")
                character.get_msg()  # Afficher le message du personnage
                response = input("\nQuelle est votre réponse?: ")

                if response == "oui":
                    print("Hisoka a très mal pris cette défiance.")
                    print(f"Un combat s'engage avec Hisoka!")

                    action = input("Voulez-vous attaquer ? (Tapez 'attack' pour attaquer, ou autre pour fuir) : ").lower()

                    if action == "attack":
                        # Si l'utilisateur tape 'attack', lancer le combat
                        if not game.player.combat(character):  # Si le combat échoue, on ne déplace pas le joueur.
                            print("Vous avez perdu le combat et ne pouvez pas avancer.")
                            return False  # Si le joueur perd le combat, il ne peut pas continuer
                    else:
                        print("Vous avez choisi de fuir l'ennemi.")
                        return False  # Si le joueur choisit de fuir, rien ne se passe

                else:
                    print("Hisoka vous met un mawashi geri\nGameOver")
                    game.finished = True
                    return False

            else:
                # Pour tout autre personnage, afficher son message
                print(f"Le joueur parle à {character_name}")
                character.get_msg()  # Appeler la méthode get_msg() du personnage

            return True
        else:
                print(f"\nIl n'y a pas de personnage nommé '{character_name}' ici.\n")
                return False
    def get_inventory(game,list_of_words, number_of_parameters):
        """
        regarde l'inventaire du joueur
            
    
        """
        inventory=game.player.inventory
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        if not inventory:
            print("Votre inventaire est vide.")
        else:
            inventory_description = "Vous disposez des items suivants :\n"
            for name,item in inventory.items():
                inventory_description += f"  - {item}\n"
            print(inventory_description)

    def get_history(game,list_of_words, number_of_parameters):
        """
        regarde toutes les salles visitées
            
    
        """
        room = game.rooms
        history=game.player.history
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        if not history:
            print("Aucune pièce visitée pour le moment.")
        else:
            history_s="vous avez visité "
            for idx, room in enumerate(history):
                history_s += f"{room.name}"
                if idx < len(history) - 1:  # Ajoute une virgule sauf après le dernier élément
                    history_s += ", "
            print(history_s)
