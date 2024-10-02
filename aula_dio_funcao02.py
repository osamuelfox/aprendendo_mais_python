# Argumentos não nomeados *args
# Argumentos nomeados **kwargs

#O *args é usado para receber uma lista de argumentos de comprimento variável sem a palavra-chave (keyword) na função.

def função_com_argumentos_variaveis(arg, *args):
    print("Primeiro argumento:", arg)
    
    for argumento in args:
        print("Argumento de *args", argumento)

função_com_argumentos_variaveis('primeiro_arg', 'arg2', 'arg3', 'arg3')
'''
Primeiro argumento: primeiro_arg
Argumento de *args: arg2
Argumento de *args: arg3
Argumento de *args: arg3
'''

#O **kwargs possibilita verificarmos os parâmetros nomeados da função, isto é, aqueles parâmetros que são passados com um nome!

def concatena (**kwargs):
    print(f'Valores recebidos: {kwargs}')
    resultado = ""

    for valor in kwargs.values():
        resultado += f'{valor} '
    return resultado

print(concatena(a="Python", b="Academy",  c="Rules!"))
print()
print(concatena(a="Python", b="é", c="na", d="Python", e="Academy!"))
'''
Valores recebidos: {'a': 'Python', 'b': 'Academy', 'c': 'Rules!'}
Python Academy Rules! 

Valores recebidos: {'a': 'Python', 'b': 'é', 'c': 'na', 'd': 'Python', 'e': 'Academy!'}
Python é na Python Academy!
'''

#Os parametros antes da / nao sao obrigatorios colocar o nome das variaveis, já os que vem apos sao obrigatorios
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Todos os parametros apos o * sao obrigatorios colocar o nome da varial
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano= 1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Temos o hibrido que podemos usar os dois, onde marca pode ser definido com os dois modos
def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")