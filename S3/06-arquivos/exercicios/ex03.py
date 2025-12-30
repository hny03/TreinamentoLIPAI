def linha_para_dict(linha, chaves):
    valores = linha.split(",")
    dic = dict(zip(chaves, valores))
    return dic

dic = linha_para_dict(" SP000001,Maria da Silva,maria@email.com", ['prontuario', 'nome', 'email'])

print(dic)