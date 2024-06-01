class Produto:
    def __init__(self, nome:str, cod:int, valor:float, qtd:int):
        self.__nome = nome
        self.__cod = cod
        self.__valor = valor
        self.__qtd = qtd
    
    def exibirInfor(self):
         return(f'Nome: {self.__nome}| Código: {self.__cod}| Valor: R${self.__valor}| Quantidade: {self.__qtd}')

    
    def adicionar(self, qtd:int=1):
        self.__qtd += qtd

    def remover(self, qtd:int=1):
        self.__qtd -= qtd


class Alimento(Produto):
    def __init__(self, nome, cod, valor, qtd, validade, peso):
        super().__init__(nome, cod, valor, qtd)
        self.validade = validade
        self.peso = peso

class Bebidas(Produto):
    def __init__(self, nome, cod, valor, qtd, alcoolica, ml):
        super().__init__(nome, cod, valor, qtd)
        self.acoolica = alcoolica
        self.ml = ml
        
   