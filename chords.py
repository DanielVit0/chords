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
    if nota == 'E' :
        if i == 1:
            acorde = 'E'
        elif i == 2:
            acorde = 'F#m'
        elif i == 3:
            acorde = 'G#m'
        elif i == 4:
            acorde = 'A'
        elif i == 5:
            acorde = 'B'
        elif i == 6:
            acorde = 'C#m'
        elif i == 7:
            acorde = 'D#º'
    if nota == 'F' :
        if i == 1:
            acorde = 'F'
        elif i == 2:
            acorde = 'Gm'
        elif i == 3:
            acorde = 'Am'
        elif i == 4:
            acorde = 'Bb'
        elif i == 5:
            acorde = 'C'
        elif i == 6:
            acorde = 'Dm'
        elif i == 7:
            acorde = 'Eº'
    if nota == 'G' :
        if i == 1:
            acorde = 'G'
        elif i == 2:
            acorde = 'Am'
        elif i == 3:
            acorde = 'Bm'
        elif i == 4:
            acorde = 'C'
        elif i == 5:
            acorde = 'D'
        elif i == 6:
            acorde = 'Em'
        elif i == 7:
            acorde = 'F#º'
    if nota == 'A' :
        if i == 1:
            acorde = 'A'
        elif i == 2:
            acorde = 'Bm'
        elif i == 3:
            acorde = 'C#m'
        elif i == 4:
            acorde = 'D'
        elif i == 5:
            acorde = 'E'
        elif i == 6:
            acorde = 'F#m'
        elif i == 7:
            acorde = 'G#º'
    if nota == 'B' :
        if i == 1:
            acorde = 'B'
        elif i == 2:
            acorde = 'C#m'
        elif i == 3:
            acorde = 'D#m'
        elif i == 4:
            acorde = 'E'
        elif i == 5:
            acorde = 'F#'
        elif i == 6:
            acorde = 'G#m'
        elif i == 7:
            acorde = 'A#º'
        
    print(f'{i} > {acorde}')
    i += 1
