class SymTable:
    # Initialize a empty dictionary for storing identifiers
    def __init__(self):
        self.symbols = {}

    # Insert tokens into symbols dictionary
    def insert(self, token):
        self.symbols[token.value] = {'type':token.type, 'lineNumber':token.lineno, 'index':token.index}