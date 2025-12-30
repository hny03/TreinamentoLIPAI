# arq = open("S3/06-arquivos/file_aula02.txt", "w")

# arq.write("Linha 1\n", "Linha 2\n", "Linha 3\n")

# x = ["Linha 1\n", "Linha 2\n", "Linha 3\n"]
# arq.writelines(x)

# arq.close()

with open("S3/06-arquivos/file_aula02.txt", "w") as arq: # já fecha o arquivo automaticamente
    arq.write("Linha 1\n")
    arq.write("Linha 2\n")
    arq.write("Linha 3\n")