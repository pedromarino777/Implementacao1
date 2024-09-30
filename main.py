import re

class Scanner:

    padroes_tokens = [
        ('NUMERO', r'\d+'),                         #Números inteiros
        ('VARIAVEL', r'[a-zA-Z_][a-zA-Z_0-9]*'),    #Identificadores
        ('ATRIBUIR', r'='),                         #Operador de atribuição
        ('SOMA', r'\+'),                            #Operador de adição
        ('SUBTRAI', r'-'),                          #Operador de subtração
        ('MULTIPLICA', r'\*'),                      #Operador de multiplicação
        ('DIVIDE', r'/'),                           #Operador de divisão
        ('IGUALDADE', r'=='),                       #Comparação de igualdade
        ('DIFERENTE', r'!='),                       #Comparação de diferença
        ('MENOR_QUE', r'<'),                        #Comparação de menor que
        ('MAIOR_QUE', r'>'),                        #Comparação de maior que
        ('ABRE_PARENTESES', r'\('),                 #Parêntese esquerdo
        ('FECHA_PARENTESES', r'\)'),                #Parêntese direito
        ('CONDICAO_SE', r'if'),                     #Palavra reservada 'if'
        ('CONDICAO_SENAO', r'else'),                #Palavra reservada 'else'
        ('ABRE_CHAVE', r'\{'),                      #Chave esquerda
        ('FECHA_CHAVE', r'\}'),                     #Chave direita
        ('FINALIZA', r';'),                         #Ponto e vírgula
        ('ESPACO', r'\s+'),                         #Espaços em branco
    ]

    def analisar_codigo(self, codigo):
        tokens_encontrados = []
        posicao_atual = 0

        while posicao_atual < len(codigo):
            correspondencia = None
            for tipo_token, expressao in self.padroes_tokens:
                padrao = re.compile(expressao)
                correspondencia = padrao.match(codigo, posicao_atual)
                if correspondencia:
                    valor_token = correspondencia.group(0)
                    if tipo_token != 'ESPACO':
                        tokens_encontrados.append((tipo_token, valor_token))
                    posicao_atual = correspondencia.end(0)
                    break
            if not correspondencia:
                raise ValueError(f"Erro Léxico: Símbolo inválido na posição {posicao_atual}")

        return tokens_encontrados

codigo_teste = """
x = 10;
y = 5;
resultado = (x * y) + 20 / (y - 2);
if (x > y) {
    resultado = resultado + 1;
} else {
    resultado = resultado - 1;
}
"""

scanner = Scanner()
tokens_gerados = scanner.analisar_codigo(codigo_teste)
for token in tokens_gerados:
    print(token)