from math import fsum
notas = []
while True:
    a = input('Qaundo terminar escreva "fim"\nIntroduza a sua nota: ')
    if a.lower() == 'fim':
        break
    try:
        nota = float(a)
        notas.append(nota)
    except ValueError:
        print("Valor inválido. Por favor, introduza um número ou 'fim' para terminar.")
if notas:
    b = fsum(notas) / len(notas)
    c = max(notas)
    d = min(notas)
    print('A sua maior nota foi {:.2f} valores\nA sua menor nota foi: {:.2f} valores'.format(c,d))
    if b < 10:
        print(f'Reprovado, a sua nota final é de: {b:.2f}')
    else:
        print(f'Está aprovado, a sua nota final é de: {b:.2f}')
else:
    print('Nao foram introduzidas notas.')