"""File Item"""
class Item:
    """
    Class Initalizing methods of Item
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, name, description, weight):
        """
        Initializing Method Init and attributes
        """
        self.name = name
        self.description = description
        self.weight = weight
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"


if __name__ == "__main__":
    sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
print("hello world")