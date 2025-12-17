# declaração de lista

lista = list("Eduardo")  # ['E', 'd', 'u', 'a', 'r', 'd', 'o']
print(lista)

# OU

lista = ['E', 'd', 'u', 'a', 'r', 'd', 'o']
print(lista)
# ---------------------------------------------------
# Listas podem conter qualquer objeto, inclusive outras listas

matriz = [
    ["Edu", 20],
    ["Let", 23],
    ["Gabi", 22]
]
print(matriz[0])  # ['Edu', 20]

print(matriz[-1][1])  # 22

# Fatiamento de Listas

print(lista[0:4])  # ['E', 'd', 'u', 'a']
# ---------------------------------------------------
# Iteração em listas

carros = ["Gol", "Celta", "Uno"]
# Para descobrir o índice
for indice, carro in enumerate(carros):
    print(f'O índice do elemento: {carro} é {indice}')

# ---------------------------------------------------
# compreensão de listas
# quando precisamos criar uma lista à partir de outra

numeros = [22, 13, 453, 32, 124, 754, 124, 247, 771, 988]
pares = []

# Forma 1:
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
# Forma 2 (recomendada):
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
