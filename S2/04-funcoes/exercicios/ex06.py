def calculo_volume(comprimento, altura, largura):
    return (comprimento*altura*largura)/1000

def calculo_potencia(temperatura_desejada, temperatura_ambiente, volume):
    return volume*0.5*(temperatura_desejada-temperatura_ambiente)

def faixa_filtragem(volume):
    return volume*2, volume*3

comprimento = float(input("Indique o comprimento do aquário: "))
altura = float(input("Indique a altura do aquário: "))
largura = float(input("Indique a largura do aquário: "))
temperatura_desejada = float(input("Indique a temperatura desejada: "))
temperatura_ambiente = float(input("Indique a temperatura ambiente: "))


aquario = {
    "comprimento" : comprimento, 
    "altura" : altura, 
    "largura" : largura,
    "temperatura_desejada" : temperatura_desejada,
    "temperatura_ambiente" : temperatura_ambiente,
    "volume" : 0,
    "potencia" : 0,
    "filtragem" : []
}

aquario["volume"] = calculo_volume(aquario["comprimento"], aquario["altura"], aquario["largura"])
aquario["potencia"] = calculo_potencia(aquario["temperatura_desejada"], aquario['temperatura_ambiente'], aquario["volume"])
aquario["filtragem"] = faixa_filtragem(aquario["volume"])

print("\nDados do aquário:")
for chave, valor in aquario.items():
    print(f"{chave}: {valor}")

print(
    f"\nFaixa de filtragem: min = {aquario['filtragem'][0]} "
    f"max = {aquario['filtragem'][1]}"
)