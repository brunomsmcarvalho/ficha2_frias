lista = ['bola','carrinho','toalha','boia']
while True:
    print('')
    print('O seu stock atual é: \n\033[31m{}\033[m'.format(lista))
    print('''
[ 1 ] Adiciona produtos novos 
[ 2 ] Remove produtos vendidos
[ 3 ] Verificar de um produto está disponivel
    ''')
    x = int(input('Opção:'))
    if x == 1:
        lista.append(input('Item: '))
    elif x == 2:
        item = input('Item: ')
        if item in lista:
            lista.remove(item) 
    elif x == 3:
        procura = input('Search: ')
        if procura in lista:
            print('O item {} está disponivel para venda'.format(procura))
    else:
        break            
