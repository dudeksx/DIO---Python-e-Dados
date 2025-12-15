MAIOR_IDADE = 18


try:
    idade = int(input('Digite a sua idade: '))

    if idade <= 0:
        print('Idade inválida!')
    elif idade >= MAIOR_IDADE:
        print('Pode tirar a CNH!')
    elif idade < MAIOR_IDADE:
        print('Você é muito novo!')
except ValueError:
    print('O valor digitado não é um número ou não é suportado!')


# Ifs aninhados

if idade >= MAIOR_IDADE:
    if idade <= 100:
        print('Idade válida!')
    else:
        print('Idade Inválida')

# IF Ternário
maior = 'Sim' if idade >= MAIOR_IDADE else 'Não'
print(f'O resultado é: {maior}')
