# tupla sao imutaveis já as listas podem ser modificadas
# Sao muito parecidas com uma lista, principais mudancas no codigo sao a utilizacao de () ao inves de [] e a virgula "," no ultimo item

frutas = ("laranja", "pera", "uva",)
frutas[0] # laranja
frutas[2] # uva

letras = tuple("python") # ('p', 'y', 't', 'h', 'o', 'n')

numeros = tuple([1, 2, 3, 4]) # (1, 2, 3, 4)

pais = ("Brasil",) # ('Brasil',)


#Tentando modificar um item de uma tupla
#tup = (1, 3)

#tup[0] = 2

''' tup[0] = 2
    ~~~^^^
TypeError: 'tuple' object does not support item assignment'''

#Funcao enumerate, mostra em qual posicao esta cada elemento

carros = ("Gol", "Celta", "Palio",)
for indice, carro in enumerate(carros):

    print(f"{indice}: {carro}")


#O count conta quantos daquele valor tem dentro da lista
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1


#O index mostrar onde foi a primeira ocorrencia deste valor
linguagens = ('python', 'js', 'c', 'Java', 'csharp',)
linguagens.index("Java") # 3
linguagens.index("python") # 0

# O len ler o tamanho da lista
len(linguagens) # 5
