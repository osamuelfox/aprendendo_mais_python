#Funcao de primeira classe
def somar(a, b):
    return a + b

def subtrair(a ,b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a ,b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)


#Escolo local e global

salario = 2000

def salario_bonus(bonus):
    #global salario
    global salario

    #Local lista
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)