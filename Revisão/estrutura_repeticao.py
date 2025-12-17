# For, funciona bem quando sabemos a quantidade exata de repetições ou
# quando o usuário determina uma quantidade de alguma forma

texto = ""
VOGAIS = "AEIOU"  # Case sensitive

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Quebra de linha

# Range, para iterar corretamente, é necessário transformar em tipo List

# print(list(range(1, 11)))

for numero in range(1, 11):
    print(numero, end=" ")

# Exibindo uma tabuada (5), o primeiro argumento é o número inicial,
# O segundo é o número máximo,
# O terceiro é de quanto em quanto o número "pula", nesse caso de 5 em 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

# ----------------------------------------------
# while, funciona bem quando não sabemos quantas vezes nosso código deve repetir!

opcao = -1

while opcao != 0:
    opcao = int(input('\n[1]Sacar \n[2]Extrato \n[0]Sair \nDigite a opção:'))

    if opcao == 1:
        print("Sacando o valor...")
    elif opcao == 2:
        print('Extrato da conta: ')
    else:
        print("Opção escolhida não é válida")
        break
        # continue segue dentro do loop
else:
    print("Obrigado por escolher nosso sistema!")
