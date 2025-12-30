def carregar_dados_alunos(nome_arquivo):

    tupla = ()

    with open(nome_arquivo, "r") as arq:
        
        for dados in arq: 
            prontuario, nome, email = dados.split(",")

            dic = {
                "prontuario" : prontuario,
                "nome" : nome,
                "email" : email
            }

            tupla = tupla + (dic,)

    return tupla

dados = carregar_dados_alunos("S3/06-arquivos/exercicios/file_ex01.txt")

print(dados)