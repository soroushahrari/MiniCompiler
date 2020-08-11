from sly import Lexer
class MyLexer(Lexer):
    def __init__(self):
        self.nesting_level = 0

    # List of valid tokens
    tokens = {
        INTEGER, FLOAT, STRING, BOOLEAN,
        IF, ELSE, FOR, WHILE, SWITCH, CASE,
        AND, OR, NOT, TYPE, IDENTIFIER,
        EQUAL, LEQUAL, GEQUAL, NEQUAL, GREATERT, LESST, ASSIGN,
        PLUS, MINUS, DIVIDE, TIMES,  
    }

    # literal characters
    literals = {
        '(', ')', '{', '}', ';'
    }

    # Ignore whitespaces, tabs and single line comments
    ignore = '[ \t]'
    ignore_comments = r'\/\/.*'
    
    # Basic operations
    PLUS = r'\+'
    MINUS = r'\-'
    DIVIDE = r'\/'
    TIMES = r'\*'

    # Relation operations
    EQUAL =  r'\=\='
    NEQUAL = r'\!\='
    GEQUAL = r'>='
    LEQUAL = r'<='
    GREATERT = r'>'
    LESST =  r'<'
    ASSIGN =  r'\='

    # Logical operators
    AND = r'\&\&'
    OR = r'\|\|'
    NOT = r'\!(?!\W)'

    # String literals
    STRING = r'(\".*\")|(\'.*\')'

    # Floating point numbers
    @_(r'-?\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    # Integer numbers
    @_(r'-?\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    # left and right braces
    # nesting level => level of nested scope created by braces
    # @_(r'\{')
    # def lbrace(self, t):
    #     t.value = '{'
    #     self.nesting_level +=1
    #     return t
    
    # @_(r'\}')
    # def rbrace(self, t):
    #     t.value = '}'
    #     self.nesting_level -= 1
    #     return t

    # Identifiers and keywords
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

    # Ignore new lines and count line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # specify number of column for characters
    def find_column(self, text, token):
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    # Simple error handling
    def error(self, t):
        print(f'ERROR! Line {self.lineno}: Bad Character {t.value[0]}')
        # Move on to next characters
        self.index += 1
    