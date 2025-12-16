# Tuplas se parecem com listas, mas são imutáveis, portanto, após criar uma Tupla não é possível modificá-la
# Recomenda-se colocar uma vírgula ao final de uma declaração, para evitar erros do Python.

frutas = ("Laranja", "uva", "maca",)  # Tupla declarada usando parênteses

letras = tuple("Python")  # Ou via classe Tuple

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

# Slicing funciona da mesma forma que na lista

print(frutas[0])  # Laranja

# É possível aninhar Tuplas, assim como listas

matriz = (
    ("Laranja", "Uva",),
    (1, 2,),
    (15, 20,)
)

print(matriz[-1][0])  # 15
