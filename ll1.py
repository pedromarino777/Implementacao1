import main

class ParserLL1:
    def __init__(self, tokens):
        self.tokens = tokens
        self.indice = 0
        self.token_atual = self.tokens[self.indice]

    def avancar(self, esperado):
        if self.token_atual[0] == esperado:
            print(f"Token consumido: {self.token_atual}")
            self.indice += 1
            if self.indice < len(self.tokens):
                self.token_atual = self.tokens[self.indice]
        else:
            raise SyntaxError(f"Erro Sintático: esperado {esperado}, mas obtido {self.token_atual[0]}")

    def analisar_programa(self):
        print("Iniciando análise do código...")
        while self.token_atual[0] in ['VARIAVEL', 'CONDICAO_SE']: 
            self.analisar_comando()
        print("Análise completa do programa.")

    def analisar_comando(self):
        if self.token_atual[0] == 'VARIAVEL':
            self.analisar_atribuicao()
        elif self.token_atual[0] == 'CONDICAO_SE':
            self.analisar_condicional()
        else:
            raise SyntaxError(f"Erro Sintático: Comando inválido na posição {self.indice}")

    def analisar_atribuicao(self):
        print("Analisando comando de atribuição...")
        self.avancar('VARIAVEL')      
        self.avancar('ATRIBUIR')
        self.analisar_expressao()    
        self.avancar('FINALIZA')

    def analisar_condicional(self):
        print("Analisando estrutura condicional...")
        self.avancar('CONDICAO_SE')
        self.avancar('ABRE_PARENTESES')
        self.analisar_condicao()
        self.avancar('FECHA_PARENTESES')
        self.avancar('ABRE_CHAVE')
        self.analisar_bloco_comandos()
        self.avancar('FECHA_CHAVE')

        if self.token_atual[0] == 'CONDICAO_SENAO':
            self.avancar('CONDICAO_SENAO')
            self.avancar('ABRE_CHAVE')
            self.analisar_bloco_comandos()
            self.avancar('FECHA_CHAVE')

    def analisar_bloco_comandos(self):
        print("Analisando bloco de comandos...")
        while self.token_atual[0] in ['VARIAVEL', 'CONDICAO_SE']:
            self.analisar_comando()

    def analisar_condicao(self):
        print("Analisando expressão condicional...")
        self.analisar_expressao()
        if self.token_atual[0] in ['IGUALDADE', 'DIFERENTE', 'MENOR_QUE', 'MAIOR_QUE']:
            self.avancar(self.token_atual[0])
        else:
            raise SyntaxError(f"Erro Sintático: Operador relacional inválido na posição {self.indice}")
        self.analisar_expressao()

    def analisar_expressao(self):
        print("Analisando expressão matemática...")
        self.analisar_termo()
        while self.token_atual[0] in ['SOMA', 'SUBTRAI']:
            self.avancar(self.token_atual[0])
            self.analisar_termo()

    def analisar_termo(self):
        print("Analisando termo...")
        self.analisar_fator()
        while self.token_atual[0] in ['MULTIPLICA', 'DIVIDE']:
            self.avancar(self.token_atual[0])
            self.analisar_fator()

    def analisar_fator(self):
        print("Analisando fator...")
        if self.token_atual[0] == 'NUMERO':
            self.avancar('NUMERO')
        elif self.token_atual[0] == 'VARIAVEL':
            self.avancar('VARIAVEL')
        elif self.token_atual[0] == 'ABRE_PARENTESES':
            self.avancar('ABRE_PARENTESES')
            self.analisar_expressao()  
            self.avancar('FECHA_PARENTESES')  
        else:
            raise SyntaxError(f"Erro Sintático: Fator inválido encontrado na posição {self.indice}")

codigo_teste = """
x = 10;
y = 5;
resultado = (x + y) * (x - y) / 3;
if (x > y) {
    resultado = resultado + 2;
} else {
    resultado = resultado - 2;
}
"""

analisador_lexico = Lexico.lexer
tokens = analisador_lexico.lexico(codigo_teste)
analisador_sintatico = ParserLL1(tokens)
analisador_sintatico.analisar_programa()