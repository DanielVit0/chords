notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
escala_maior = [0, 2, 4, 5, 7, 9, 11] # intervalo da escala maior

print("=== Campo Harmônico Maior ===")
nota = input('Digite uma nota(C - C# - D - D# - E - F - F# - G - G# - A - A# - B): ').upper()

if nota in (notas):
    indice_base = notas.index(nota) # Mostra em qual indice está a nota 
    print(f'O campo harmônico de {nota}:')

    for posicao, intervalo in enumerate(escala_maior):
        indice = (indice_base + intervalo)%12
        if posicao in [1,2,5]: # 2º, 3º e 6º graus são menores
            print(notas[indice] + 'm', end=' ') 
        elif posicao in [6]: # 7º grau é diminuto
            print(notas[indice] + '°', end=' ')
        else:
            print(notas[indice], end=' ')
else:
    print('Nota inválida')