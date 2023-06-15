class Pessoa:
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def __str__(self):
        return f'My name is {self.firstname} {self.secondname}'

class Professor(Pessoa):
    def __init__(self, firstname, secondname):
        super().__init__(firstname, secondname)

class Aluno(Pessoa):
    def __init__(self, firstname, secondname, serie):
        self.serie = serie
        Pessoa.__init__(self, firstname, secondname)

    def __str__(self):
        return f'Meu nome é {self.firstname} {self.secondname} e estou no {self.serie}° ano'

print(Pessoa('Jadson', 'Lucas'))
print(Professor('Joane', 'Amorim'))
print(Aluno('Davi', 'Enzo', 3))