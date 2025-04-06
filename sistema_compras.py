print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
totcompra = totproduto = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    cont += 1
    totcompra += preço #Soma todos os preços
    # Verifica o menor preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        totproduto += 1 #Acumula a quantidade de produtos < 1000
    confirmaçao = ' '
    while confirmaçao not in 'SN':
        confirmaçao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if confirmaçao == 'N': #Termina o programa
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra deu {totcompra:.2f}')
print(f'Temos {totproduto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

