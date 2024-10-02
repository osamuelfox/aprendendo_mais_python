
def exibir_mensagem():
    print("Olá mundo!!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!!!")

def exibir_mensagem_3(nome="Monica"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Samuel")
exibir_mensagem_3()
exibir_mensagem_3(nome="Ilton")


#Função para converter Fahrenheit em Celsius 
def fahr_to_celsius(temp):
    """
    Função que recebe como argumento uma temperatura
    em Fahrenheit e converte ela para Celsius 
    """
    return ((temp - 32) * (5/9))

temperatura = float(input("Digite a temperatura em Fahrenheit: "))

#print(fahr_to_celsius(temperatura))
print(f"{fahr_to_celsius(temperatura):.2f}")
print(fahr_to_celsius(91.76)) # 33.2

celsius = fahr_to_celsius(70.76)
print(celsius) # 21.53333333333334

#funcao que returna a soma dos numeros informados
def calcular_total(numeros):
    return sum(numeros)

#Funcao que retorna o antecessor e o sucessor
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,25]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#formas de passar os parametros para uma funcao
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio",ano= 1999, placa="ABC-1234")
# ** -> Dicionario
salvar_carro(**{"marca":"Fiat", "modelo":"Palio","ano": 1999, "placa":"ABC-1234"})