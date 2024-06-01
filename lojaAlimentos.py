class Produto:
    def __init__(self, nome: str, cod: int, valor: float, qtd: int):
        self.nome = nome
        self.cod = cod
        self.valor = valor
        self.qtd = qtd
    
    def exibirInfor(self):
        return f'Nome: {self.nome}| Código: {self.cod}| Valor: R${self.valor}| Quantidade: {self.qtd}'
    
    def adicionar(self, qtd: int = 1):
        self.qtd += qtd

    def remover(self, qtd: int = 1):
        if self.qtd >= qtd:
            self.qtd -= qtd
        else:
            print("Quantidade insuficiente em estoque!")

class Alimento(Produto):
    def __init__(self, nome, cod, valor, qtd, validade: str, peso: float):
        super().__init__(nome, cod, valor, qtd)
        self.validade = validade
        self.peso = peso

    def exibirInfor(self):
        return f'Nome: {self.nome}| Código: {self.cod}| Valor: R${self.valor}| Quantidade: {self.qtd}| Validade: {self.validade}| Peso: {self.peso}'

class Bebida(Produto):
    def __init__(self, nome, cod, valor, qtd, alcoolica: bool, ml: float):
        super().__init__(nome, cod, valor, qtd)
        self.alcoolica = alcoolica
        self.ml = ml
        
    def exibirInfor(self):
        alcoolica_str = 'Sim' if self.alcoolica else 'Não'
        return f'Nome: {self.nome}| Código: {self.cod}| Valor: R${self.valor}| Quantidade: {self.qtd}| Alcoólica: {alcoolica_str}| ML: {self.ml}'

class Estoque:
    def __init__(self):
        self.listaProdutos = []
    
    def adicionar(self, produto):
        self.listaProdutos.append(produto)

    def remover(self, codProduto):
        for produto in self.listaProdutos:
            if codProduto == produto.cod:
                self.listaProdutos.remove(produto)
                break

    def exibirDisponivel(self):
        for produto in self.listaProdutos:
            if produto.qtd >= 1:
                print(produto.exibirInfor())

    def exibirIndisponivel(self):
        for produto in self.listaProdutos:
            if produto.qtd == 0:
                print(produto.exibirInfor())

    def exibirTodosProdutos(self):
        for produto in self.__listaProdutos:
                print(produto.exibirInfor())


# Correção na criação dos objetos
bebida1 = Bebida("Achocolatado", 1, 20, 20.20, False, 250.500)
alimento1 = Alimento("Arroz", 2, 20, 20.20, 6, 30.30)
estoque = Estoque()
estoque.adicionar(bebida1)
estoque.adicionar(alimento1)

print("Produtos disponíveis:")
estoque.exibirDisponivel()

bebida1.remover(20)
print("\nProdutos indisponíveis:")
estoque.exibirIndisponivel()

estoque.remover(1)
print("\nProdutos após remoção:")
estoque.exibirDisponivel()

