fila = []
contador = 0
while True:
    print('[ 1 ] Adiciona pessoas à fila\n[ 2 ] Chamar a proxima pessoa da fila\n[ 3 ] Verificar quantas pessoas estão à espera\n[ 4 ] Ver quem é o próximo na fila\n[ 5 ] para sair')
    menu = int(input('Opção: '))
    if menu == 1:
        contador += 1 
        fila.append(contador)
        print(fila)
    elif menu == 2:
        print(f'A proxima pessoa é {fila[0]}')
        x = fila[0]
        fila.remove(x)
    elif menu == 3:
        print(fila)
    elif menu == 4:
        print(fila[0])
    else:
        break           
   