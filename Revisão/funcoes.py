# Funções são blocos de códigos que podem ser executados com parâmetros(argumentos) ou não

def mensagem_boas_vindas():
    print('Seja bem-vindo(a)')


mensagem_boas_vindas()


def mensagem_personalizada(nome):
    print(f"Seja bem-vindo(a) {nome}")


mensagem_personalizada("Eduardo")

# Se nenhum argumento nome for passado antes, utiliza o "Desconhecido" como default


def mensagem_padrão(nome="Desconhecido"):
    print(f"Seja bem-vindo(a) {nome}")


mensagem_padrão()
# --------------------------------------------------------------------------------------
# Podemos passar argumentos de duas formas, nomeadas ou posicionais

# Exemplo de argumento posicional

print("=" * 100)


def exemplo_1(titulo, titulo2):
    print(
        f"O elemento posicional é colocado puramente por posição. \nArgumento 1: {titulo}, argumento 2: {titulo2}")


exemplo_1("Esse será o primeiro argumento", "Esse será o segundo elemento")


def exemplo_2(primeiro_numero, segundo_numero):
    print(
        f"Nos argumentos nomeados, a ordem não importa, \npois o usuário ou desenvolvedor vai manualmente especificar qual argumento quer incluir o valor, \nesse é o segundo argumento '{segundo_numero}' e esse o primeiro '{primeiro_numero}'")


exemplo_2(primeiro_numero=1, segundo_numero=20)


print("=" * 100)
# É possível "forçar" qual o tipo do argumento a ser recebido, se é posicional ou nomeado
# todos os argumentos ANTES da '/' são obrigatóriamente posicionais, todos após o '*' devem ser nomeados


def argumentos_posicionais_e_nomeados(posicional_1, posicional_2, /, ambos_1, ambos_2, *, nomeado_1, nomeado_2):
    print(
        f"""
Tudo que está antes da barra é posicional, portanto, a ordem que é incluso
ao chamar a função importa, como os {posicional_1, posicional_2}.

Já os parâmetros que estiverem entre a barra e o asterísco podem ser qualquer tipo:
Como é o caso do {ambos_1, ambos_2}.

E por último, tudo que está após o asterísco é obrigatóriamente nomeado,
como é o caso do {nomeado_1, nomeado_2}
    """
    )


argumentos_posicionais_e_nomeados(
    1, 2, 3, ambos_2=4, nomeado_1=5, nomeado_2=6)

# --------------------------------------------------------------------------------------
# Args e Kwargs, os args são objetos do tipo tupla (separados por vírgula) e Kwargs são argumentos chave-valor (Dicionario)
# São reconhecidos por *args e **kwargs, mas pode ter qualquer nome, contanto que tenha os asteriscos antes

print("=" * 100)


def escreve_frase(data_extenso, *argumentos, **kargumentos):
    texto = "\n".join(argumentos)
    dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kargumentos.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{dados}"
    print(mensagem)


escreve_frase("16 de Dezembro, 2025",
              "Seja bem-vindo(a)",
              "Esse é um exemplo de frase que pode ser escrita.",
              "A primeira linha é considerada o primeiro parâmetro.",
              "Que é a data por extenso.",
              "Porém o Python reconhece que essas linhas após a data são ARGs.",
              "Por se tratar de strings separadas por vírgula.",
              "E que estão dentro de um parênteses.",
              "E como strings são objetos imutáveis, acabam gerando tuplas.",
              "Que é o tipo de dado dos *args.",
              autor="Eduardo",
              idade=20)
