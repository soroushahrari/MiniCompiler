from lexer import MyLexer

if __name__ == "__main__":
    data = '''
        int x = 0;
        while (x < 10) {
            x = x + 2
        }
    ''' 
    lexer = MyLexer()

    for token in lexer.tokenize(data):
        print(MyLexer.find_column(data, token), token.type, token.value, f'nesting level: {lexer.nesting_level}')
        # print(token)
