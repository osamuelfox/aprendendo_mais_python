pessoa = {"nome": "Samuel", "idade": 28, "telefone": "34 984422478"}

pessoa["telefone"] #34 984422478

pessoa["nome"] #Samuel

#Alterando valores do dicionario

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "34 9999-7777"

#Dicionario Anilhado

contatos = { 
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, 
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}
           #Primeira chave       #segunda chave
contatos ["giovanna@gmail.com"]["telefone"] # "3443-2121"

telefone = contatos ["giovanna@gmail.com"]["telefone"]

print(telefone)


                #Primeira chave  #segunda chave  #terceira chave
extra = contatos ["melaine@gmail.com"]["extra"]["a"]
print(extra) #1

#Forma de mostrar todos os valores do dicionario

for chave, valor in contatos.items(): 
    print(chave, valor)



