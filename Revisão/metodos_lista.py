# Append, inclui um bojeto no final da lista
lista = []

lista.append(10)
lista.append("Edu")
lista.append([1, 2, 3])

print(lista)  # [10, 'Edu', [1, 2, 3]]
# -------------------------------------------

# Copy, cria uma cópia da lista
lista2 = lista.copy()
lista2.append("Esse é um objeto")
print(lista2)

# -------------------------------------------

# Count, conta quantas vezes um objeto aparece dentro da lista
print(lista.count(10))  # 1

# -------------------------------------------

# Extend, concatena duas listas
lista.extend(lista2)
print(lista)

# -------------------------------------------

# index, retorna o índice da primeira ocorrência de um objeto
print(lista.index([1, 2, 3]))  # 2

# -------------------------------------------

# pop, remove o objeto no índice escolhido, ou o último se nada for especificado

lista.pop()  # 'Esse é um objeto'
lista.pop(2)  # [1, 2, 3]

# Remove, funciona de forma parecida com pop, mas utiliza o objeto em sí

lista.remove("Edu")
print(lista)  # [10, 10, 'Edu', [1, 2, 3]]
# -------------------------------------------

# Reverse, inverte a lista
lista.reverse()
print(lista)  # [[1, 2, 3], 'Edu', 10, 10]
# -------------------------------------------

# Sort, ordena de forma alfabética ou ascendente
alfabeto = ["d", "c", "b", "a", "e"]

alfabeto.sort()
print(alfabeto)  # ['a', 'b', 'c', 'd', 'e']
# -------------------------------------------

# Len, retorna quantos elementos existem na lista

print(len(alfabeto))  # 5 objetos

# -------------------------------------------
# Clear, esvazia a lista
lista.clear()
print(lista)  # []
