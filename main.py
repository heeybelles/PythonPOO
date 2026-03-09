class  Pessoa:
    total_pessoas = 0
 
    def __init__(self,nome,idade): #construtor do python
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1
    def __str__(self):
        print(f'Nome: {self.nome} - Idade: {self.idade}')
 
    def total(self):
        print(f'Total de pessoas: {Pessoa.total_pessoas}')
 
class Aluno(Pessoa): #herança
    #pass ou ... #classe sem atributos e metodos
    def __init__(self,nome,idade,matricula,curso):
        super().__init__(nome, idade) #permite acessar metodos da classe pai
        self.matricula = matricula
        self.curso = curso
    def __str__(self):
        print(f'Aluno: {self.nome} - Idade: {self.idade} - Matrícula: {self.matricula} - Curso: {self.curso}')
 
 
a1 = Aluno("Ana Paula", 16, "001", "DSM")
a1.__str__()
 
p1 = Pessoa("Ana", 26)
p2 = Pessoa("Ana Maria", 62)
print(p1.nome)
print(p1.idade)
print(Pessoa.total_pessoas)
p1.__str__()
p1.total()
 