# Eliminando espaços em branco

curso = "   Python "

print(curso.strip())  # remove todos os espaços em branco
print(curso.lstrip())  # remove todos à esquerda da string
print(curso.rstrip())  # remove todos à direita da string

# Colocar algo entre a string ou centralizar
nome = "Eduardo"

print(nome.center(11, "$"))

print("_".join(nome))
