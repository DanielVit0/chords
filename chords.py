print("=== Campo Harmônico Maior ===")
nota = input('Digite uma nota(C,D,E,F,G,A,B): ')

i = 1
print(f'O Campo harmônico maior de {nota}, possue as seguintes notas:')
while i <= 7:
    if nota == 'C' :
        if i == 1:
            acorde = 'C'
        elif i == 2:
            acorde = 'Dm'
        elif i == 3:
            acorde = 'Em'
        elif i == 4:
            acorde = 'F'
        elif i == 5:
            acorde = 'G'
        elif i == 6:
            acorde = 'A'
        elif i == 7:
            acorde = 'Bº'
    if nota == 'D' :
        if i == 1:
            acorde = 'D'
        elif i == 2:
            acorde = 'Em'
        elif i == 3:
            acorde = 'F#m'
        elif i == 4:
            acorde = 'G'
        elif i == 5:
            acorde = 'A'
        elif i == 6:
            acorde = 'Bm'
        elif i == 7:
            acorde = 'Cº'
        
    print(f'{i} > {acorde}')
    i += 1
