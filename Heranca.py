#Classe base

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def cumprimentar(self):
        print(f'Olá! Tudo bem? Me chamo {self.nome}')

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf

    

# instância de um objeto da classe pessoa

pessoa = Pessoa('Tim Maia', '010.200.300-44')

print(pessoa.nome)
print(pessoa.getCpf())

pessoa.nome = 'Dercy Gonçalves'
