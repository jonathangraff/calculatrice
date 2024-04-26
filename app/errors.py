class InvalidString(Exception):

    def __init__(self, calculation=''):
        self.message = f"The string '{calculation}' is not a valid string in Reverse Polish Notation"
        super().__init__()

    def __str__(self):
        return self.message


class InvalidCharacter(Exception):

    def __init__(self, character):
        self.message = f"The character '{character}' is invalid."
        super().__init__()

    def __str__(self):
        return self.message