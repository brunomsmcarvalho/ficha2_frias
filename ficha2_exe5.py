frase = str(input('Digite uma frase: '))
palavras = frase.split()
qntdd = len(palavras)
print('\nA sua frase tem {} palavras'.format(qntdd))
maior = palavras[0] #comeca na primeira palavra
for a in palavras:
    if len(a) > len(maior):
        maior = a
print('\nA maior palavra é {} com {} letras'.format(maior,len(maior)))