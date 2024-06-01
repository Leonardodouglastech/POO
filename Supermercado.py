class Produto:
    def __init__(self, nome, codigo, valor, qtd):
        self.nome = nome
        self.codigo = codigo
        self.valor = valor
        self.qtd = qtd


class Alimento(Produto):
    def __init__(self, nome, codigo, valor, qtd, validade, peso):
        super().__init__(nome, codigo, valor, qtd)
        self.validade = validade
        self.peso = peso

class Bebidas(Produto):
    def __init__(self, nome, codigo, valor, qtd, alcoolica, ml):
        super().__init__(nome, codigo, valor, qtd)
        self.acoolica = alcoolica
        self.ml = ml
        
   