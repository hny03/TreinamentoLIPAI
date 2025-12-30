""" Aula 02 - Atributos de classe e de instância """

# Classe pessoa possui atributos de instancia: nome e email
class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa("Maria da Silva", "maria@email.com")
pessoa1.especie = "Mutante"  # Modificando atributo de classe para a instância pessoa1

pessoa2 = Pessoa("João Souza", "joao@email.com")

Pessoa.especie = "Alienigenas do passado" # Modificando atributo de classe para todas as instâncias

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)