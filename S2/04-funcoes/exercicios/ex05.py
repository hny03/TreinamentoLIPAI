def calcular_imc(individuo):
    imc = individuo["peso"]/pow(individuo["altura"], 2)
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        print("Baixo peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso normal")
    elif 25 <= imc <= 29.9:
        print("Excesso de peso")
    elif 30 <= imc <= 34.9:
        print("Obesidade de Classe 1")
    elif 35 <= imc <= 39.9:
        print("Obesidade de Classe 2")
    elif imc >= 40:
        print("Obesidade de Classe 3")

def situacao_individuo(imc):
    if imc < 18.5 : print("Ganhar peso")
    elif imc < 25 : print("Normal")
    elif imc >= 25 : print("Perder peso")

peso = float(input("Indique o seu peso: "))
altura = float(input("Indique a sua altura: "))

individuo = {
    'altura' : altura,
    'peso' : peso
}

imc = calcular_imc(individuo)
print(imc)
obter_classificacao(imc)
situacao_individuo(imc)
