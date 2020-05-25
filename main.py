from lexer import MyLexer
from symbolTable import SymTable


# Read source code from file
def filereader(filename):
    with open (filename) as f:
        data = f.read()
    return data

if __name__ == "__main__":
    data = filereader('test/test.txt')
    lexer = MyLexer()
    mySymboleTable = SymTable()
    tokens = lexer.tokenize(data)

    # Insert identifiers into symbol table
    for token in tokens:
        if token.type == 'IDENTIFIER':    
            mySymboleTable.insert(token)