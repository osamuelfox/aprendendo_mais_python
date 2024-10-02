carros = ["Gol", "Celta", "Palio"]

#For para pecorrer a lista
for carro in carros:

    print(carro)

#Funcao enumerate, mostra em qual posicao esta cada elemento
for indice, carro in enumerate(carros):

    print(f"{indice}: {carro}")



numeros = [1, 30, 21, 2 ,9 , 65, 34]
pares = []

#Filtro 01, ira armazenar todos os itens da lista que forem pares

for numero in numeros:

    if numero % 2 == 0:

        #append é uma funcao para adicionar novos valores
        pares.append(numero)

print(pares) # [30, 2, 34]

#Filtro 02, uma forma diferente de fazer o filtro
impar = [numero for numero in numeros if numero % 2 != 0]

print(impar) # [1, 21, 9, 65]

#Modificando valores 01, eleva ao quadrado todos os valor de numeros e armazena em quadrado
quadrado = []

for numero in numeros:

    quadrado.append(numero ** 2)

print(quadrado) # [1, 900, 441, 4, 81, 4225, 1156]

#Modificando valores 01, eleva ao cubo todos os valor de numeros e armazena em cubo
cubo = [numero ** 3 for numero in numeros]

print(cubo) # [1, 27000, 9261, 8, 729, 274625, 39304]