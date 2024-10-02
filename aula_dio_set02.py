conjunto_a = {1, 2}
conjunto_b = {3, 4}

# O union ira fundir os dois conjuntos
conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

############################################

conjunto_c = {1, 2 ,3}
conjunto_d = {2, 3, 4}

# O intersection  ira pegar os valores  iguais dos dois conjuntos
conjunto_c.intersection(conjunto_d) # {2, 3}

############################################

conjunto_e = {1, 2 ,3}
conjunto_f = {2, 3, 4}

# O difference mostra os valor que esta presente somente em um conjunto que nao esta no outro
conjunto_e.difference(conjunto_f) # {1}
conjunto_f.difference(conjunto_e) # {4}

############################################

# O symmetric_difference retorna os valores que nao estao no outro
conjunto_e.symmetric_difference(conjunto_f) # {1, 4}

############################################

conjunto_g = {1, 2 , 3}
conjunto_h = {4, 1, 2, 5, 6, 3}

# O issubset ira verificar se os elementos de conjunto_g estão em conjunto_h
conjunto_g.issubset(conjunto_h) # True

# O issubset ira verificar se os elementos de conjunto_h estão em conjunto_g
conjunto_h.issubset(conjunto_g) # False

############################################

# O issuperset ira verificar se os elementos de conjunto_h estão em conjunto_g
conjunto_g.issuperset(conjunto_h) # False

# O issuperset ira verificar se os elementos de conjunto_g estão em conjunto_h
conjunto_h.issuperset(conjunto_g) # True

############################################

conjunto_1 = {1, 2, 3, 4, 5} 
conjunto_2 = {6, 7, 8, 9} 
conjunto_3 = {1,0} 

# O isdisjoint ira verificar se os conjuntos nao se tocam
conjunto_1.isdisjoint(conjunto_2) # True 
conjunto_1.isdisjoint(conjunto_3) # False

############################################

# O add ira adicionar um elemento caso ele já nao esteja dentro de sorteio
sorteio = {1, 23} 
sorteio.add(25) # (1, 23, 25) 
sorteio.add(42) # (1, 23, 25, 42) 
sorteio.add(25) # (1, 23, 25, 42)

############################################

#Ira limpar o sorteio
sorteio = {1, 23} 
sorteio # {1,23)
sorteio.clear() 
sorteio # {}

############################################

#Ira fazer uma copia do set
sorteio = {1, 23} 
sorteio # {1, 23) 
sorteio.copy() 
sorteio # {1, 23)

############################################

#ira descartar o valor mas sem dar erro se nao tiver o valor
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} 
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9,0) 
numeros.discard(1)
numeros.discard(45) 
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}

############################################

#Ira tirando o valor da frente
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} 
numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
numeros.pop() #0 
numeros.pop() #1 
numeros # {2, 3, 4, 5, 6, 7, 8, 9}

############################################

#O remove você tem que informa o indice que ira remover, mas se voce colocar um valor que nao existe, ira dar erro - diferente do discart
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} 
numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 
numeros.remove(0) #0 
numeros #{1, 2, 3, 4, 5, 6, 7, 8, 9)

############################################

#Ira contar os elementos do set, somente os que nao estao duplicados
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} 
len (numeros) # 10

############################################

# O in ira verificar se meste item esta dentro do set
1 in numeros # True
10 in numeros # False