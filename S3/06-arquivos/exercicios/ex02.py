def carregar_dados_projetos(nome_arquivo):

    tupla = ()

    with open(nome_arquivo, "r", encoding="utf-8") as arq:
        
        for dados in arq: 
            codigo, titulo, responsavel = dados.split(",")

            dic = {
                "codigo" : int(codigo),
                "titulo" : titulo,
                "responsavel" : responsavel
            }

            tupla = tupla + (dic,)

    return tupla

dados = carregar_dados_projetos("S3/06-arquivos/exercicios/file_ex02.txt")

print(dados)    