codigo = input("Digite um código: ")

erros = []

tamanho_correto = (len(codigo) == 7)
comeco_correto = (codigo[0:2] == "BR")
numero_correto = codigo[2:len(codigo)-1].isdigit()
final_correto = codigo.endswith("X")

if tamanho_correto == False:
    erros.append("O identificador não contém 7 dígitos")

if comeco_correto == False:
    erros.append("O identificador não inicia com 'BR'")

if numero_correto == False:
    erros.append("O identificador não apresenta número inteiro entre 0001 e 9999")

if final_correto == False:
    erros.append("O identificador não finaliza com 'X'")



if tamanho_correto and comeco_correto and numero_correto and final_correto:
    print("Identificador válido")
else:
    for erro in erros: print(erro)