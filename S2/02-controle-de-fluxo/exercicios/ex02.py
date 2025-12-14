notas = input("Digite todas as notas separadas por espaço: ")

notas_lista = notas.split()

notas_lista = [float(nota) for nota in notas_lista]

media = sum(notas_lista) / len(notas_lista)

print("Média = ",  media)

aprovado = media > 6
recuperacao = 4 <= media <= 6
reprovado = media < 4

if aprovado:
    print("Aprovado")
elif recuperacao:
    print("Recuperação")
elif reprovado:
    print("Reprovado")