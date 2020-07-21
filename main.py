from lexer import MyLexer
from symbolTable import SymTable


# Read source code from file
def filereader(filename):
    with open (filename) as f:
        data = f.read()
    return data

if __name__ == "__main__":
    fileName = input('Enter your file Address: ex: test/test.txt\n')
    data = filereader(fileName)
    lexer = MyLexer()
    mySymbolTable = SymTable()
    tokens = lexer.tokenize(data)
    list_of_tokens = []

    # Insert identifiers into symbol table
    for token in tokens:
        list_of_tokens.append(token)
        if token.type == 'IDENTIFIER':    
            mySymbolTable.insert(token)

    print('Symbol Table =>', mySymbolTable.symbols)
    print('-----------------------------')
    print('List of All tokens\n')
    for token in list_of_tokens:
        print(token)