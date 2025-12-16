# Conjunto não-ordenado de chave:valor, sendo as chaves únicas, os valores podem ser qualquer objeto.
# A chave obrigatoriamente precisa ser um objeto imutável

# Forma de declarar
pessoa = {"nome": "Edu", "idade": 20}
# Ou
pessoa = dict(nome="Edu", idade=20)
# incluir uma nova chave:valor em um dict já existente
pessoa["curso"] = "Python - DIO"

print(pessoa)  # {'nome': 'Edu', 'idade': 20, 'curso': 'Python - DIO'}

print(pessoa["curso"])  # Python - DIO
print(pessoa["nome"])  # Edu

# É possível reatribuir o valor de uma chave
pessoa["nome"] = "Let"
print(pessoa["nome"])  # Let

# É possível aninhar dicionários
# ------------------------------------------------------------------

# copy, cria uma cópia do dicionário
copia = pessoa.copy()
print(copia)  # {'nome': 'Let', 'idade': 20, 'curso': 'Python - DIO'}

# fromkeys, cria um dicionário somente com chaves, ou então com chave + um valor padrão
dicionario = dict.fromkeys(["nome", "idade"], "vazio")
print(dicionario)  # {'nome': 'vazio', 'idade': 'vazio'}

# método get, busca no dicionário pela chave e retorna o valor,caso não encontre pode colocar um retorno padrão
print(copia.get("nome", "Não encontrado"))


# método .clear, esvazia o dicionário
pessoa.clear()  # {}
