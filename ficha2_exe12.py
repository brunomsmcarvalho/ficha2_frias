dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
minutos = []
for i in dias_semana:
    c = float(input('Quantos minutos de exercico fez {}?'.format(i)))
    minutos.append(c)
#total_minutos = minutos.split()
total_minutos = sum(minutos)
print('Nesta semana fizeste o total de {} minutos de exercicio'.format(total_minutos))
maximo = max(minutos)
indice_max = minutos.index(maximo)
dia_max = dias_semana[indice_max]
print('O dia com mais exercício foi {} com {} minutos.'.format(dia_max, maximo))
if all(m > 0 for m in minutos):
    print('Fizeste exercício todos os dias. PARABENS ')
else:
    for i, m in enumerate(minutos):
        if m == 0:
            print('Nao fizeste erxercicio {}.'.format(dias_semana[i]))
            