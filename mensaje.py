def procesar(comando, frases):
    if comando == 'TOTAL':
        return f'TOTAL: {len(frases)} FRASES'

    return 'ERROR'
