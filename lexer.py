from sly import Lexer

class MyLexer(Lexer):
    tokens = {
        INTEGER, FLOAT, STRING, BOOLEAN,
        IF, ELSE, FOR, WHILE, SWITCH, CASE,
        AND, OR, NOT, TYPE, IDENTIFIER,
        EQUAL, LEQUAL, GEQUAL, NEQUAL, GREATERT, LESST, ASSIGN,
        PLUS, MINUS, DIVIDE, TIMES,  
    }

    literals = {
        '(', ')', '{', '}', ';'
    }

    ignore = '[ \t]'
    ignore_comments = r'\/\/.*'
    

    PLUS = r'\+'
    MINUS = r'\-'
    DIVIDE = r'\/'
    TIMES = r'\*'

    EQUAL =  r'\=\='
    NEQUAL = r'\!\='
    GEQUAL = r'>='
    LEQUAL = r'<='
    GREATERT = r'>'
    LESST =  r'<'
    ASSIGN =  r'\='

    AND = r'\&\&'
    OR = r'\|\|'
    NOT = r'\!(?!\W)'

    STRING = r'(\".*\")|(\'.*\')'

    @_(r'-?\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'-?\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    IDENTIFIER = r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    IDENTIFIER['if'] = IF
    IDENTIFIER['else'] = ELSE
    IDENTIFIER['for'] = FOR
    IDENTIFIER['while'] = WHILE
    IDENTIFIER['switch'] = SWITCH
    IDENTIFIER['case'] = CASE
    IDENTIFIER['int'] = TYPE
    IDENTIFIER['float'] = TYPE
    IDENTIFIER['str'] = TYPE
    IDENTIFIER['bool'] = TYPE
    IDENTIFIER['true'] = BOOLEAN
    IDENTIFIER['false'] = BOOLEAN

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f'ERROR! Line {self.lineno}: Bad Character {t.value[0]}')
        self.index += 1
    

if __name__ == "__main__":
    data = 'xif if else != >>= = 4 + 5.4 bool true falsef //hello \n yes : hello switch case""' 
    lexer = MyLexer()

    for token in lexer.tokenize(data):
        print(token)