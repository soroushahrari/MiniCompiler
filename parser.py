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
        print('#1#', self.symstack, '\n')
        return p.statements

    @_("")
    def block(self, p):
        print('#2#', self.symstack, '\n')
        return []

    @_('statement')
    def statements(self, p):
        print('#3#', self.symstack, '\n')
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        print('#4#', self.symstack, '\n')
        p.statements.append(p.statement)
        return p.statements

    @_('var_declaration')
    def statement(self, p):
        print('#5#', self.symstack, '\n')
        return p.var_declaration

    @_('assign_statement')
    def statement(self, p):
        print('#6#', self.symstack, '\n')
        return p.assign_statement

    @_('if_statement')
    def statement(self, p):
        print('#7#', self.symstack, '\n')
        return p.if_statement

    @_('while_statement')
    def statement(self, p):
        print('#8#', self.symstack, '\n')
        return p.while_statement

    @_('IF "(" expr ")" "{" block "}" ELSE "{" block "}"')
    def if_statement(self, p):
        print('#9#', self.symstack, '\n')
        return ('if_statement', p.expr, ('branch', p.block0, p.block1))
    
    @_('IF "(" expr ")" "{" block "}"')
    def if_statement(self, p):
        print('#10#', self.symstack, '\n')
        return ('if_statement', p.expr, ('branch', p.block))
    
    @_('WHILE expr "{" block "}"')
    def while_statement(self, p):
        print('#11#', self.symstack, '\n')
        return ('while_loop', ('while_loop_setup', p.expr), p.block)
    
    @_('TYPE IDENTIFIER ASSIGN expr ";"')
    def var_declaration(self, p):
        print('#12#', self.symstack, '\n')
        if (p.TYPE != p.expr[0]):
            return f'ERROR: Value does not match the type at line {p.lineno}'
        return ('var_declaration', p.IDENTIFIER, p.expr)
    
    @_('TYPE IDENTIFIER ";"')
    def var_declaration(self, p):
        print('#13#', self.symstack, '\n')
        return ('var_declaration', p.IDENTIFIER)

    @_('IDENTIFIER ASSIGN expr ";"')
    def assign_statement(self, p):
        print('#14#', self.symstack, '\n')
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
        print('#15#', self.symstack, '\n')
        return (p[1], p.expr0, p.expr1)

    @_('"(" expr ")"')
    def expr(self, p):
        print('#16#', self.symstack, '\n')
        return p.expr

    @_('IDENTIFIER')
    def expr(self, p):
        print('#17#', self.symstack, '\n')
        return p.IDENTIFIER
    
    @_('literal')
    def expr(self, p):
        print('#18#', self.symstack, '\n')
        return p.literal

    @_('INTEGER')
    def literal(self, p):
        print('#19#', self.symstack, '\n')
        return ('int', p.INTEGER)
    
    @_('FLOAT')
    def literal(self, p):
        print('#20#', self.symstack, '\n')
        return ('float', p.FLOAT)

    @_('STRING')
    def literal(self, p):
        print('#21#', self.symstack, '\n')
        return ('str', p.STRING)
    
    @_('BOOLEAN')
    def literal(self, p):
        print('#22#', self.symstack, '\n')
        return ('bool', p.BOOLEAN)
    
    def error(self, token):
        print(f'SYNTAX ERROR near character "{token.value}" at line {token.lineno}')