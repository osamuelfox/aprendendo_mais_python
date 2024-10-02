curso = "pYtHon"

#Maiusculo
print(curso.upper())
#minusculo
print(curso.lower())
#Primeira letra maiuscula
print(curso.title())

curso = "  Python  "

#Elimina todos os espaços em banco do texto
print(curso.strip())
#Elimina todos os espaços do lado esquerdo
print(curso.lstrip())
#Elimina todos os espaços do lado direito
print(curso.rstrip())

curso = "Python"

#Ira centralizar a string e preencher os espaços
print(curso.center(10, '#'))
print(curso.center(10))

#Ira colocar um ponto a cada item da sua string
print(".".join(curso))