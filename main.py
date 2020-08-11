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
    # fileName = input('Enter your file Address: ex: test/test.txt\n')
    # data = filereader(fileName)
    mySymbolTable = SymTable()
    lexer = MyLexer()
    parser = MyParser()
    # tokens = lexer.tokenize(data)
    list_of_tokens = []

    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python3 -m main.py filename \n')
        raise SystemExit(1)

    text = filereader(sys.argv[1])
    result = parser.parse(lexer.tokenize(text))

    for item in result:
        print(item)

    # while True:
    #     try:
    #         text = input('test > ')
    #     except EOFError:
    #         break

    #     if text:
    #         tokens = lexer.tokenize(text)
    #         res = parser.parse(tokens)
    #         print(res)
    #         parser.log
    #         print(parser.symstack)

    # print(parser.symstack)
        # text = input('comp > ')
    
    # Insert identifiers into symbol table
    # for token in tokens:
    #     list_of_tokens.append(token)
    #     if token.type == 'IDENTIFIER':    
    #         mySymbolTable.insert(token)

    # print('Symbol Table =>', mySymbolTable.symbols)
    # print('-----------------------------')
    # print('List of All tokens\n')
    # for token in list_of_tokens:
    #     print(token)

    