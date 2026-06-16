import random

def procesar(comando, frases):
    comando = comando.strip()

    if comando == 'TOTAL':
        lineas = len(frases)
        return f'TOTAL: {len(frases)} FRASES {lineas} LINEAS'

    elif comando == 'FRASE':
        return 'FRASE: ' + random.choice(frases)

    return 'ERROR'
