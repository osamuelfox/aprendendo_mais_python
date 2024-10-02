# Usando o set para remover itens duplicados de uma lista, podemos pegar uma lista e transformar em set ou criar uma com {} chaves

set([1 ,2 ,3 ,1 , 3 ,4]) # {1, 2, 3, 4}

# O Set nao garante a ordem

set("abacaxi") # {'x', 'i', 'c', 'a', 'b'}

linguagens = set(['python', 'js', 'c', 'Java', 'csharp', 'python']) # {'Java', 'python', 'js', 'csharp', 'c'}

# Criando um set
numeros = {1 ,2 ,3 , 2}

#Nao podemos acessar um set, devemos transformar em lista
#print(numeros[0])
''' print(numeros[0])
          ~~~~~~~^^^
TypeError: 'set' object is not subscriptable'''

numeros = list(numeros)
print(numeros[0])

#Mas podemos percorrer um set, mas nao podemos confiar na ordem
carros = {"Gol", "Celta", "Palio"}

for carro in carros:

    print(carro)