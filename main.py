import sys
from lexer import MyLexer
from parser import MyParser
from symbolTable import SymTable

# Read source code from file
def filereader(filename):
    with open (filename) as f:
        data = f.read()
    return data

if __name__ == "__main__":
    mySymbolTable = SymTable()
    lexer = MyLexer()
    parser = MyParser(mySymbolTable)
    list_of_tokens = []

    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python3 -m main.py filename \n')
        raise SystemExit(1)

    text = filereader(sys.argv[1])
    result = parser.parse(lexer.tokenize(text))

    for item in result:
        print(item)

    # Insert identifiers into symbol table
    # for token in tokens:
    #     list_of_tokens.append(token)
    #     if token.type == 'IDENTIFIER':    
    #         mySymbolTable.insert(token)

    print('Symbol Table =>', mySymbolTable.symbols)
    # print('-----------------------------')
    # print('List of All tokens\n')
    # for token in list_of_tokens:
    #     print(token)

    