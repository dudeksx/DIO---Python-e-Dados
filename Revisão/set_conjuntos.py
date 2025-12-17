# É um conjunto de objetos não-repetidos, elimina os objetos duplicados

numeros = {1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 10}

# Também funciona com strings ou outros objetos iteráveis
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Essa versão abaixo é mais comumente utilizada do que a declaração direta (exemplo da linha 3)
print(set(("teste", "teste", "carro", "moto")))  # {'teste', 'carro', 'moto'}

# É possível iterar sobre conjuntos através de For
for n in numeros:
    print(n, end=" ")  # 1 2 3 4 5 6 7 8 9 10

# Conjuntos não suportam indexação ou fatiamento, é necessário transformar estes em lista
numeros = list(numeros)
print(numeros[3])  # 4

# -----------------------------------------------------------------------------

# Esses conjuntos são iguais aos conjuntos matemáticos, e possuem métodos como tal
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b))  # {1, 2, 3, 4}
print(conjunto_a.intersection(conjunto_b))  # {2, 3}
print(conjunto_a.difference(conjunto_b))  # {1} O que tem em A mas não em B
print(conjunto_b.difference(conjunto_a))  # {4} O que tem em B mas não em A
# {1, 4}, O que não é comum à ambos
print(conjunto_a.symmetric_difference(conjunto_b))
# -----------------------------------------------------------------------------

conjunto_a = {3, 4, 5}
conjunto_b = {1, 2, 3, 4, 5}

# True, retorna True pois A está contido em B
print(conjunto_a.issubset(conjunto_b))
# False, B não está contido em A
print(conjunto_b.issubset(conjunto_a))
# issuperset, é o contrário, valida se um conjunto é contido em outro
# -----------------------------------------------------------------------------

conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {1, 0}

# isdisjoint serve para validar se dois conjuntos NÃO se interseccionam
# True, pois A e B não possuem valores em comum
print(conjunto_a.isdisjoint(conjunto_b))
# False, pois C intersecciona com A
print(conjunto_a.isdisjoint(conjunto_c))

conjunto_c.add(2)
print(conjunto_c)  # {0, 1, 2}, add adiciona, se não houver repetição
# Discard remove o objeto informado, o POP remove o primeiro elemento do conjunto
conjunto_c.discard(1)
print(conjunto_c)  # {0, 2}
