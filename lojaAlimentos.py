class Produto:
    def __init__(self, nome:str, cod:int, valor:float, qtd:int):
        self.__nome = nome
        self.cod = cod
        self.__valor = valor
        self.__qtd = qtd
    
    def exibirInfor(self):
         return(f'Nome: {self.__nome}| Código: {self.cod}| Valor: R${self.__valor}| Quantidade: {self.__qtd}')

    
    def adicionar(self, qtd:int=1):
        self.__qtd += qtd

    def remover(self, qtd:int=1):
        self.__qtd -= qtd


class Alimento(Produto):
    def __init__(self, nome, cod, valor, qtd, validade:float, peso:float):
        super().__init__(nome, cod, valor, qtd)
        self.__validade = validade
        self.__peso = peso

    def exibirInfor(self):
        return(f'Nome: {self.__nome}| Código: {self.cod}| Valor: R${self.__valor}| Quantidade: {self.__qtd}| Validade: {self.__validade}| Peso: {self.__peso}')

    


class Bebida(Produto):
    def __init__(self, nome, cod, valor, qtd, alcoolica:bool, ml:float):
        super().__init__(nome, cod, valor, qtd)
        self.acoolica = alcoolica
        self.ml = ml
        
    def exibirInfor(self):
        return(f'Nome: {self.__nome}| Código: {self.cod}| Valor: R${self.__valor}| Quantidade: {self.__qtd}| Alcoolica: {self._alcoolica}| ML: {self.__ml}')
    
class Estoque:
    def ___init__(self,listaProdutos = []):
        self.__listaProdutos = listaProdutos
    
    def adicionar(self, produto):
        self.__listaProdutos.append(produto)

    def remove(self, codProduto):
        for produto in self.__Produtos:
            if codProduto == produto.cod:    
                self.__listaProdutos.remove(produto)
