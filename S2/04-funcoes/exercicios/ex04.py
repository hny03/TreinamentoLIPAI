def soma(*args):
    return sum(args)

numeros = input("Entre com quaisquer numeros separados por espaço: ")

numeros = numeros.split()

numeros = [float(numero) for numero in numeros]

print("Soma = ", soma(*numeros))