""" Aula 01 - Debug"""

def somar(n1, n2, n3):
    return n1 + n2 + n3

def calcular_media(n1, n2, n3):
    total = somar(n1, n2, n3)
    quantidade = 3
    return total / quantidade


nota01 = 10.0
nota02 = 3.0
nota03 = 5.5

breakpoint()  # Ponto de interrupção para depuração

media = calcular_media(nota01, nota02, nota03)
print(f'A média das notas é: {media}')