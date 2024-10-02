lista = []

# O append é usando para adicionar novos itens a lista
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

#Limpar a lista
lista.clear()

lista = [1, 'Python', [40, 30, 20]]

#O Copy é usado para nao alterar o valor da lista origial 
l2 = lista.copy()

#Alterei o valor 1 para 2 mas a original permanece com 1
l2[0] = 2
print(l2) # [2, 'Python', [40, 30, 20]]    

#O count conta quantos daquele valor tem dentro da lista
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

#O extend ira adicionar todos os itens que você declarar e colocar ao final da linha
linguagens = ["python", "js", "c"]

print(linguagens) # ['python', 'js', 'c']

linguagens.extend(["Java", "csharp"])

print(linguagens) # ['python', 'js', 'c', 'Java', 'csharp']

#O index mostrar onde foi a primeira ocorrencia deste valor
linguagens.index("Java") # 3
linguagens.index("python") # 0

# O pop ira sempre tirar o ultimo item da pilha, mas podemos informar o indice
# ['python', 'js', 'c', 'Java', 'csharp']

print(linguagens.pop()) # csharp
print(linguagens.pop()) # Java
print(linguagens.pop()) # c
print(linguagens.pop(0)) # python

# O remove tira o item pelo valor, apenas o primeiro
linguagens = ['python', 'js', 'c', 'Java', 'csharp']

linguagens.remove("c") # ['python', 'js', 'Java', 'csharp']

#O reverse inverte a lista assim como [::-1]
linguagens.reverse()
print(linguagens) # ['csharp', 'Java', 'js', 'python']

#O sort ira ordenar a lista, por padrao ira ordenar em ordem alfabetica ou numerica se for numeros
linguagens.sort() # ['Java', 'csharp', 'js', 'python']

#O sorted faz a mesma coisa que o sort mas é uma funcao
sorted(linguagens) # ['Java', 'csharp', 'js', 'python']

# Ira inverter a ordem alfabetica
linguagens.sort(reverse=True)  # ['python', 'js', 'csharp', 'Java']

#Ira mostrar a lista de acordo com o tamanho dos itens
linguagens.sort(key=lambda x : len(x)) # ['js', 'Java', 'python', 'csharp']

#Podemos inverter tambem
linguagens.sort(key=lambda x : len(x), reverse=True) # ['python', 'csharp', 'Java', 'js']

# O len ler o tamanho da lista
len(linguagens) # 4

