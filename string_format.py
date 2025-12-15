# Eliminando espaços em branco

curso = "   Python "

print(curso.strip())  # remove todos os espaços em branco
print(curso.lstrip())  # remove todos à esquerda da string
print(curso.rstrip())  # remove todos à direita da string

# Colocar algo entre a string ou centralizar
nome = "Eduardo"

print(nome.center(11, "$"))

print("_".join(nome))

# --------------------------------------------------------------------------------
# Interpolação de strings, 3 formatos
nome = "Eduardo"
idade = 20
# -------------------------------------------
# Versão antiga, não utilizada.

# print("Olá, me chamo %s e tenho %s anos." % (nome, idade))
# -------------------------------------------

# Versão format, utilizada com menos frequência
# Não é necessário botar as variáveis na ordem, basta escolher o índice
print("Olá, me chamo {1} e tenho {0} anos!".format(idade, nome))

print("Olá, me chamo {nome} e tenho {idade} anos".format(nome="Gui", idade=15))

pessoa = {
    "nome": "Victor",
    "idade": 37
}

print("Olá, me chamo {nome} e tenho {idade} anos".format(**pessoa))
# -------------------------------------------
# Versão f-string, muito mais moderna e utilizada com mais frequência.
print(f'Olá, me chamo {nome} e tenho {idade} anos!!')

# formatar casa decimal na string
PI = 3.141592

print(f"O número de PI é: {PI:.2f}")
