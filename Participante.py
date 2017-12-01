class Participante():
    def __init__(self, nome, nascimento, email):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

    def __str__(self):
        return "Nome: %s\nNascimento: %s\nE-mail: %s " %(self.nome, self.nascimento, self.email)

    def __eq__(self, other):
        return  self.nome == other.nome and self.nascimento == other.nascimento and self.email == other.email
