#Utilizando break no While

while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)

#Utilizando break no For

for numero in range(100):

    if numero == 11:
        break
    print(numero, end=" ")

print()

#Utilizando o continue / Exibe todos os numero menos o informado no if, irá pular a condicao

for numero in range(100):

    if numero == 11:
        continue
    print(numero, end=" ")

print()

#Exibindo apenas numeros impares

for numero in range(100):

    if numero % 2 == 0:
        continue
    print(numero, end=" ")