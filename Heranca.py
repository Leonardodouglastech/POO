class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def cumprimentar(self):
        print(f'Olá ! Tudo bem? Me chamo {self.nome}')

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf

    def getCpf(self):
        return self.__cpf 


# criação classe mãe que herda atributos e métodos da classe Pessoa

class Mae(Pessoa):
    def __init__(self, nome, cpf, corPele):
        super().__init__(nome, cpf)
        self.corPele = corPele

    def dancar(self):
        print(f'{self.nome} está dançando')

class Pai(Pessoa):
    def __init__ (self, nome, cpf, corCabelo):
        super().__init__(nome, cpf)
        self.corCabelo = corCabelo

mae = Mae("América", "222.333.444-55", "parda")
print(mae.getCpf())

class Filha( Mae, Pai):
    def __init__(self, nome, cpf, corPele, corCabelo):
        Mae.__init__(self, nome, cpf, corPele)
        Pai.__init__(self, nome, cpf, corCabelo)

    def engatinhar(self):
        print(f'{self.nome}, está engatinhando!')

filha1 = Filha('Khatia', '222.222.222-22', 'parda', 'ruivo')
