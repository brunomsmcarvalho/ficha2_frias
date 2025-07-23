jogadores = ['joao','afonso','bruno','lucas','bairrada','miguel']
print(jogadores)
print('')
x = len(jogadores) // 2
jogadores1 = jogadores[:x]
jogadores2 = jogadores[x:]
print('Dividindo as equipas a meio ficamos com:')
print('Equipa 1',jogadores1)
print('Equipa 2',jogadores2)
print('')
while True:
    menu=str(input('Deseja trocar jogadores entre as equipas? s/n ')).strip().lower()
    if menu =='s':
        a = int(input('Escolha da equipa 1 ou equipa 2: '))
        if a == 1:
            print(jogadores1)
            print('Escolha o jogador 1, 2 ou 3 para trocar: ')
            b=int(input('Opção: ')) -1
            print(jogadores2)
            print('Escolha um jogador da equipa 2 para substituir, 1, 2 ou 3')
            d = int(input('Opção: '))-1
            if 0 <= b < len(jogadores1) and 0 <= d < len(jogadores2):
                jogador1 = jogadores1.pop(b)
                jogador2 = jogadores2.pop(d)
                jogadores2.append(jogador1)
                jogadores1.append(jogador2)
                print('=-As equipas ficaram organizadas assim-=')
                print('Equipa1',(jogadores1))
                print('Equipa2', (jogadores2))
            else:
                 print('Jogador Inválido')
        elif a == 2:
             print(jogadores2)
             print('Escolha um jogador da equipa 2 para substituir, 1, 2 ou 3')
             c = int(input('Opção: '))-1#-1 porque a posicao das listascomeça em 0
             print(jogadores1)
             print('Escolha um jogador da equipa 1 para substituir, 1, 2 ou 3')
             e = int(input('Opção: ')) - 1
             if 0 <= c < len(jogadores2) and 0 <= e < len(jogadores1):
                jogador1 = jogadores2.pop(c)
                jogador2 = jogadores1.pop(e)
                jogadores2.append(jogador1)
                jogadores1.append(jogador2)
                print('=-As equipas ficaram organizadas assim-=')
                print('Equipa1', (jogadores1))
                print('Equipa2', (jogadores2))
    elif menu == 'n':
        print('Melhor assim, as equipas ficam como estao!!')
        break
    else:
        print('Opção inválida. Escolha "s" ou "n"')
    