# Loops e Listas
# --------------------------------------------------------
lista = list(range(1, 11))

for i in lista:
    if i != 5:
        if i != 9:
            print(i)

# --------------------------------------------------------

opcao = -1
saldo = 1000
while opcao != 0:

    print(
        """
    ==========MENU==========

    1 - Sacar

    0 - Sair

    ========================
    """
    )
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print(
            f"""
    ==========MENU==========

    Seu saldo é: R$ {saldo}

    ========================
    """
        )
        saque = int(input("Digite o valor a ser retirado: "))
        if saque <= saldo and saque > 0:
            print(f"Saque realizado, saldo restante: {saldo - saque}")
        else:
            print('Saldo insuficiente ou saque inválido')

# --------------------------------------------------------

# Matriz

pessoa = [
    ["Edu", 20],
    ["Let", 23],
    ["Gab", 22]
]
print(pessoa[1])  # Imprime o segundo registro inteiro
print(pessoa[-1][-1])  # Imprime o último objeto do último registro
# --------------------------------------------------------

# Fatiamento
nome = "Eduardo Porto"
print(nome[8:])  # Porto
# --------------------------------------------------------
