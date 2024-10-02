nome = "Samuel Santos de Souza"
idade = 22
profissao = "Programador"
linguagem = "Python"
saldo = 45.3453

#f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho, como {profissao} e estou matriculado no curso de linguagem {linguagem}, o saldo em minha conta é: {saldo:.2f}.")

PI = 3.14159

#Formata o numero de casas decimais
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

#Fatiamento de String
nome[0] #S
nome[:6] #Samuel
nome[17:] #Souza
nome[6:17] #Santos de
nome[:: -1] #azuoS ed sotnaS leumaS
nome[6:17:2] # atsd

print(nome[:])#Samuel Santos de Souza

#Usando triplas aspas simples o texto fica com a formatacao original
mensagem = f''' 
    Olá meu nome é {nome},
 Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.


'''
print(mensagem)