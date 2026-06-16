def procesar(comando, frases):
    comando = comando.strip()

    if comando == 'TOTAL':
        return f'TOTAL: {len(frases)} FRASES'

    return 'ERROR'
