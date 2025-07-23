import random

playlist = ['musica1','musica2','musica3','musica4','musica5','musica6']

while True:
    print('''
[ 1 ] - Adicionar música
[ 2 ] - Remover música
[ 3 ] - Fazer Shuffle
[ 4 ] - Mostra a primeira música 
[ 5 ] - Terminar programa
''')
    
    a = int(input('Opção: '))
    if a == 5:
        print('\nPlaylist final')
        print(playlist)
        break

    elif a == 1:
        nova = str(input('Introduza a música: '))
        playlist.append(nova)
        print('\nA música {} foi adicionada à lista'.format(nova))

    elif a == 2:
        print(playlist)
        remover = input('Escolha uma musica para remover da lista: ').lower().strip()
        if remover in playlist:
            playlist.remove(remover)
            print('A música {} foi removida da playlist'.format(remover))
        else:
            print('\nA música {} não está presenta na playlist'.format(remover))
    elif a == 3:
        random.shuffle(playlist)
        print('A playlist foi baralhada.')
    elif a == 4:
        print('\nA proxima música a tocar será a {}'.format(playlist[0]))
