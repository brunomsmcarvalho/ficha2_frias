y = 0#contador de dias
w = 0#somatorio de temperaturas
temperaturas = []
while True:
    entrada = input('Deseja introduzir temperaturas? S ou N: ').lower().strip()
    
    if entrada == 's':
        print('Indique ´quantas temperaturas quer registar')
        x = int(input('Quantidade: '))
        
        for u in range(x):
            y += 1
            temps = float(input('Temperatura dia {} foi de: '.format(y)))
            temperaturas.append((y, temps))  # guarda tuplo (dia, temperatura)
            w += temps
        
        media = w/y
        print('A média das temperaturas registadas é {:.2f}'.format(media))
    
    elif entrada == 'n':
        break
    else:
        print("Entrada inválida. Introduza 'S' ou 'N'.")

# Após a introdução dos dados, fazer os cálculos adicionais:
if temperaturas:
    dia_mais_quente = max(temperaturas, key=lambda x: x[1])
    dia_mais_frio = min(temperaturas, key=lambda x: x[1])
    dias_acima_20 = sum(1 for dia, temp in temperaturas if temp > 20)
    
    print('\nResumo:')
    print('Dia mais quente: Dia {} com {:.2f}°C'.format(dia_mais_quente[0], dia_mais_quente[1]))
    print('Dia mais frio:   Dia {} com {:.2f}°C'.format(dia_mais_frio[0], dia_mais_frio[1]))
    print('Número de dias com temperatura acima de 20 °C:', dias_acima_20)
else:
    print('\nNenhuma temperatura foi registada.')