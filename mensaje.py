import random

def procesar(comando, frases):
    comando = comando.strip()

    if comando == 'TOTAL':
        lineas = len(frases)
        return f'TOTAL: {len(frases)} FRASES {lineas} LINEAS'

    if comando == 'FRASE':
        return 'FRASE: ' + random.choice(frases)

    return 'ERROR'
