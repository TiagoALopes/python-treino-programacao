class Piloto:

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    def aumento(self, valoraumento):
        valoraumento = valoraumento/100
        return self.salario * (1 + valoraumento)

    def email(self):
        return (f'{self.nome}.{self.sobrenome}@email.com.br')
    
    def nomecompleto(self):
        return (f'{self.nome} {self.sobrenome}')
        