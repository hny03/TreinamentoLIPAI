#open("caminho", "r")

#Modes
#'r' - read (leitura) - padrão
#'w' - write (escrita) - apaga o conteúdo anterior
#'a' - append (acrescentar) - mantém o conteúdo anterior
#'x' - create (criar) - cria o arquivo, se já existir, gera erro
#'r+' - leitura e escrita

#arquivo = open("S3/06-arquivos/file_aula01.txt", "r")

#print(arquivo.readable())  # Verifica se o arquivo pode ser lido
#print(arquivo.read()) # Lê todo o conteúdo do arquivo
#print(arquivo.readline())  # Lê a primeira linha do arquivo
#print(arquivo.readline())  # Lê a segunda linha do arquivo

# lista = arquivo.readlines()  # Lê todas as linhas e retorna uma lista

#print(lista)

#print(lista[1])

#arquivo = open("S3/06-arquivos/file_aula01.txt", "a")

#arquivo.write("\nSQL")
#arquivo.write("C++\n")

#arquivo = open("S3/06-arquivos/file2_aula01.txt", "w")

#arquivo.write("SQL\n")
#arquivo.write("C++\n")

#arquivo.close()

import os 
if os.path.exists("S3/06-arquivos/file2_aula01.txt"):
    os.remove("S3/06-arquivos/file2_aula01.txt") # Remove o arquivo (precisa estar fechado)

else:
    print("O arquivo não existe")
