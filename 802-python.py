class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # def dados_pessoa (self):
       # print(nome, idade)

class Medico(Pessoa):
    def __init__ (self, nome, idade, crm):
        super().__init__(nome, idade)
        self.crm = crm

    # def dados_medico (self):
       # print(nome, idade, crm)

class Paciente(Pessoa):
    def __init__(self,nome,idade,infermidade):
        super().__init__(nome,idade)
        self.infermidade = infermidade
    

pessoa = Pessoa('Lucas', 19)
medico = Medico('Larissa', 15, 3723)
paciente = Paciente('matheus', 15, 'colesterol')
print (medico.nome, medico.idade, medico.crm)
print(pessoa.nome, pessoa.idade)
print(paciente.nome, paciente.idade, paciente.infermidade)
