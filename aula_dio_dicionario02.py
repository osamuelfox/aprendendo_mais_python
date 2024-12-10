contatos = { 
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, 
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", },
}

#clear vai apagar todos os dados do dicionario

contatos.clear()

#copy vai copiar os dados do dicionario / Usado quando você nao quer usar os dados do dicionario original
contato = { 
   "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, 
}
copia = contato.copy()

copia["guilherme@gmail.com"] = {"nome": "Gui"}

#dict.fromkeys usado criar um dicionario com valores vazios
dict.fromkeys (["nome", "telefone"]) # {"nome": None, "telefone": None} 
dict.fromkeys (["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

#get para retornar se o dicionario existe 
contato.get("chave") # None 
contato.get("chave", {}) # {}
contato.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}


#items - retorna os itens do dicionario 
contato.items() # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

#keys retorna as chaves do dicionario 
contato.keys() 

#pop remove do dicionario e pode retornar um valor
contato.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-2221'} 
contato.pop("guilherme@gmail.com", {}) # {}


#setdefault irá adicionar uma chave caso ela nao exista, caso exista, ele nao altera o valor 
contato.setdefault("nome", "Giovanna") # "Guilherme" 
print(contato) #nome': 'Guilherme', 'telefone': '3333-2221'} 

contato.setdefault("idade", 28)# 28
print(contato) #nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28)

#update ira alterar o dicionario com outro dicionario

contato = { "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} }
contato.update({"guilherme@gmail.com": {"nome": "Gui"}}) 
contato # {'guilherme@gmail.com': {'nome': 'Gui'}} 


contato.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) 
contato # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

#Retorna todos os valores

contatos.values() # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])

#in forma de verificar se uma chave existe no dicionario

"guilherme@gmail.com" in contatos # True 
"megui@gmail.com" in contatos # False
"idade" in contatos ["guilherme@gmail.com"] # False 
"telefone" in contatos ["giovanna@gmail.com"] # True

#del remove o que for declarado
del contatos ["guilherme@gmail.com"]["telefone"] 
del contatos ["chappie@gmail.com"] 
contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}