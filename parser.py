from sly import Parser
from lexer import MyLexer

class MyParser(Parser):

    # Get token list form Lexer
    tokens = MyLexer.tokens
    
    debugfile = 'parser.out'

    precedence = (
        ('nonassoc', EQUAL, LEQUAL, GEQUAL, NEQUAL, GREATERT, LESST),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    @_("statements")
    def block(self, p):
        return p.statements

    @_("")
    def block(self, p):
        return []

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        p.statements.append(p.statement)
        return p.statements

    @_('var_declaration')
    def statement(self, p):
        return p.var_declaration

    @_('assign_statement')
    def statement(self, p):
        return p.assign_statement

    @_('if_statement')
    def statement(self, p):
        return p.if_statement

    @_('while_statement')
    def statement(self, p):
        return p.while_statement

    @_('IF "(" expr ")" "{" block "}" ELSE "{" block "}"')
    def if_statement(self, p):
        return ('if_statement', p.expr, ('branch', p.block0, p.block1))
    
    @_('IF "(" expr ")" "{" block "}"')
    def if_statement(self, p):
        return ('if_statement', p.expr, ('branch', p.block))
    
    @_('WHILE expr "{" block "}"')
    def while_statement(self, p):
        return ('while_loop', ('while_loop_setup', p.expr), p.block)
    
    @_('TYPE IDENTIFIER ASSIGN expr ";"')
    def var_declaration(self, p):
        # print(self.symstack, '\n')
        # print(self.statestack)
        return ('var_declaration', p.IDENTIFIER, p.expr)
    
    @_('TYPE IDENTIFIER ";"')
    def var_declaration(self, p):
        
        return ('var_declaration', p.IDENTIFIER)

    @_('IDENTIFIER ASSIGN expr ";"')
    def assign_statement(self, p):
        # print('this is =>>>>>>>>>>>', self.symstack)
        return ('var_assignment', p.IDENTIFIER, p.expr)

    @_('expr PLUS expr',
        'expr MINUS expr',
        'expr TIMES expr',
        'expr DIVIDE expr',
        'expr LESST expr',
        'expr LEQUAL expr',
        'expr GREATERT expr',
        'expr GEQUAL expr',
        'expr EQUAL expr',
        'expr NEQUAL expr',
        'expr AND expr',
        'expr OR expr')
    def expr(self, p):
        return (p[1], p.expr0, p.expr1)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('IDENTIFIER')
    def expr(self, p):
        
        return p.IDENTIFIER
    
    @_('literal')
    def expr(self, p):
        return p.literal

    @_('INTEGER')
    def literal(self, p):
        return ('int', p.INTEGER)
    
    @_('FLOAT')
    def literal(self, p):
        return ('float', p.FLOAT)

    @_('STRING')
    def literal(self, p):
        return ('str', p.STRING)
    
    @_('BOOLEAN')
    def literal(self, p):
        return ('bool', p.BOOLEAN)
    
    def error(self, token):
        print(f'SYNTAX ERROR near character "{token.value}" at line {token.lineno}')

    # def sym(self, token):
    #     print(token)