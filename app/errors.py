class StringInvalid(Exception):

    def __init__(self, calculation=''):
        self.message = f"The string '{calculation}' is not a valid string in Reverse Polish Notation"
        super().__init__()

    def __str__(self):
        return self.message
