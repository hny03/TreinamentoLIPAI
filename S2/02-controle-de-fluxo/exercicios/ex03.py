codigo = input("Digite um código: ")

tamanho_correto = (len(codigo) == 7)
comeco_correto = (codigo[0:2] == "BR")
numero_correto = codigo[2:len(codigo)-1].isdigit()
final_correto = codigo.endswith("X")

if tamanho_correto and comeco_correto and numero_correto and final_correto:
    print("Identificador válido")
else:
    print("Identificador inválido")