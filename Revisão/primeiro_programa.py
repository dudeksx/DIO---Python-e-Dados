print('Olá Mundo!')

# Variáveis
nome = 'Eduardo '
idade = 20
print(nome, idade)
nome = 'Let '
idade = 23
print(nome, idade)
# -------------

# Constantes (variáveis que não alteram do inicio ao fim da aplicação)
PAIS = 'Brasil'
print(PAIS)
# -------------


# ----------------------------
# Operador Lógico

saldo = 1000
limite = 100
saque = 100
# saque = int(input('Digite o valor do Saque: '))

if saque > saldo:
    print('Saldo insuficiente!')
elif saque <= saldo and saque <= limite:
    saldo -= saque
    print(f'Saque realizado! Restante: {saldo}')
elif saque <= saldo and saque >= limite:
    print('Saldo suficiente, porém o saque ultrapassa o limite')
else:
    print('Erro!')

# Operador de identidade
# Verifica se as variáveis ocupam a mesma região da memória

nome = 'Edu'
sobrenome = 'Almeida'

valor, numero = 10, 10

print(nome is sobrenome)  # Falso
print(valor is numero)  # Verdadeiro

# Operador de Associação

curso = 'Curso de Python'
frutas = ['maçã', 'uva', 'morango']

print('Python' in curso)  # Verdadeiro
print('uVa' in frutas)  # Falso, IN é case-sensitive
print('Python' not in curso)  # Falso, pois NOT inverte o booleano final
