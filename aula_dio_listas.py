#Lista simples
frutas = ["laranja", "maca", "uva"]
print(frutas)

#Posso declarar uma lista vazia
frutas = []
print(frutas)

#Podemos declarar uma palavra como lista separando como letra
letras = list("python")
print(letras)

#Podemos usar o range para criar uma lista de numeros de 0 ate 9
numeros = list(range(10))
print(numeros)

#Podemos fazer uma lista com atributos mistos
carro = ["Ferrari", "F8", 42000000,2020,2900,"São Paulo", True]
print(carro)

#A lista começa sempre no local 0
#             [0]     [1]     [2]    [3]  [4]     [5]       [6]
#carro = ["Ferrari", "F8", 42000000,2020,2900,"São Paulo", True]
print(carro[1])

#####################################################################

#Fatiando listas

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ['t', 'h', 'o', 'n']

lista[:2] # ['p', 'y']

lista[1:3] # ['y', 't']

# o 2 significa que ira pular uma casa, fomos de 0 a 3 e pulamos o "y"
lista[0:3:2] # ['p', 't']

lista[::] # ['p', 'y', 't', 'h', 'o', 'n']

#Inverte a sequencia
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']
