filmes = ['The Perfume','Avengers']
while True:
    print(f'A sua lista de filmes é:\n{filmes}\n')
    x = input(str('Adiciona filmes à tua lista de filmes: \nOu escreve "sair" para terminar o programa\n'))
    if x.lower() == 'sair':
        print(f'A tua lista de filmes é: \n{filmes}')
        break
    filmes.append(x)
    filmes.sort(key = str.lower)