from random import randint
from time import sleep
print('Estou a pensar num numero entre 1 e 10, tenta adivinhar...')
x = list(range(1,11))
y = randint(1,10)
while True:
    try:
        z = int(input('Em que numero pensei? '))
        if z>10 or z<1:
            print('Erro, introduza um numero valido!!')
            continue
    except ValueError:
        print('Erro, introduza um numero valido!!')
        continue
    print('PROCESSASNDO...')
    sleep(1.5)
    if z == y:
            print(f'!!PARABENS!! Voce acertou! {y} era o numero em que estava a pensar!!')
            break
    else:
        print(f'Falhou, o numero {z} nao foi o numero que pensei')
        x.remove(z)
        print(x)
