texto = "Samuel"
VOGAIS = "AEIOU"

#Laço de repeticao para achar vogais em um texto

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    print("Fim do laço")


#range(start, stop, step)

#start é a posição de início da sequência (por padrão é 0);
#stop é o limite (exclusivo) da sequência;
#step é o valor de incremento da sequência (por padrão é 1).

#Imprime um laço de 0 ate 10

for numero in range(0,11):
    print(numero, end=" ")
print()

#Tabuada do 5

for numero in range (0, 51, 5):
    print(numero, end=" ")
print()

#Laço de repeticao usando While

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar o nosso banco, até mais")
