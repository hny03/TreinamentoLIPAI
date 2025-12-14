def soma(tupla):
    soma = 0

    for elemento in tupla:
        soma += elemento
    
    return soma

tupla_teste = (13, 45, 60)

print(soma(tupla_teste))