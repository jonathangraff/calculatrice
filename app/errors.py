class LastCaracterNotOperation(Exception):

    def __init__(self, last_character):
        self.message = f"Last character is not a valid operation : '{last_character}'"
        super().__init__()

    def __str__(self):
        return self.message


class TooManyOperands(Exception):

    def __init__(self, calculation):
        self.message = f"There are too many operands in the string '{calculation}'"
        super().__init__()

    def __str__(self):
        return self.message


class NotEnoughOperands(Exception):

    def __init__(self, calculation):

        self.message = f"There is not enough operands in the string '{calculation}'"
        super().__init__()

    def __str__(self):
        return self.message
