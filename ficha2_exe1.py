lista_de_compras = [] 
while True:
    print()
    a = input("Escreva sair para imprimir a lista\nOu insira novo item:  ")
    if a.lower() == 'sair':
        print(lista_de_compras)
        break
    lista_de_compras.append(a)
    print(f'{a} foi adicionado a lista de compras com sucesso',lista_de_compras)

while True:
    b = input('Escreva os items que já comprou para os retirar da lista, ou escreva (sair) para terminar: ')
    if b.lower () == 'sair':
        print()
        print(f'Faltam comprar: {len(lista_de_compras)} itens\n', lista_de_compras)
        break
    elif b in lista_de_compras:
        lista_de_compras.remove(b)
        print(f'{b} foi removido da lista de compras: ')
    else:
        print(f'{b} não está na lista de compras: ')

    if not lista_de_compras:
        print('Todos os itens foram comprados. Lista vazia!')
        break