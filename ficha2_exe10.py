pratos = ['bacalhau','bolonhesa','pizza','robalo','bitoque','amburguer']
conta = []
preco = 10

print('=-'*30)
print('  Bem vindo ao restaurante do Manel, este é o nosso menu!!')
print('=-'*30)

for i in range(len(pratos)): 
    print('{}.{}'.format(i+1,pratos[i]))
print('\033[31m7.Terminar\033[m')
print('=-'*30)

while True:
    escolha = int(input('Escolha os pratos: '))

    if escolha == 7:
        print('\n  -=Conta final=-')
        print('------------------')
        total = len(conta) * preco
        for item in conta:
            print('1-{}'.format(item))#imprime os pratos escolhidos no loop
        print('------------------')
        print('Tem a pagar {}€\n'.format(total))
        break

    elif 1 <= escolha <=6:#intervalo de escolhas 
        conta.append(pratos[escolha-1])
        print('{} - Foi adicionado à sua conta'.format(pratos[escolha-1]))

    else:
        print('Opção inválida. Escolha um número entre 1 a 7.')
        print('Até agora adicionou{}'.format(conta))
        continue #permite que o programa nao acabe caso um numero errado seja introduzido
