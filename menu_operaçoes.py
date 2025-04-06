num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ]Somar
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novos números
    [ 5 ]Sair do programa''')
    opção = int(input('Qual das opções você quer: '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}.'.format(num1, num2, soma))
    elif opção == 2:
        multiplicar = num1 * num2
        print('A multiplicação é {}.'.format(multiplicar))
    elif opção == 3:
        if num1 > num2:
            print('O maior é {}.'.format(num1))
        else:
            print('O maior é {}.'.format(num2))
    elif opção == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite um novo número: '))
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
print('Você saiu do programa.')
