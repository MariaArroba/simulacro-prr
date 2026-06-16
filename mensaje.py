def procesar(comando, frases):
    comando = comando.strip()

    if comando == 'TOTAL':
        lineas = len(frases)
        return f'TOTAL: {len(frases)} FRASES {lineas} LINEAS'

    return 'ERROR'
