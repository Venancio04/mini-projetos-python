from random import randint
cont = 0 #CONTADOR DE VITÓTIAS
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}.')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu.')
            cont += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu.')
            cont += 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente.')
print(f'Você ganhou {cont} vezes.')
