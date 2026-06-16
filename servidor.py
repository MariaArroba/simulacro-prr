import socket
from mensaje import procesar

PUERTO = 11041


def cargar_frases():
    with open("frases", encoding="utf-8") as fichero:
        return [linea.strip() for linea in fichero if linea.strip()]


def main():
    frases = cargar_frases()

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("", PUERTO))
    servidor.listen()

    print(f"Servidor escuchando en puerto {PUERTO}")

    try:
        while True:
            conexion, direccion = servidor.accept()

            datos = conexion.recv(1024).decode("utf-8")

            respuesta = procesar(datos, frases)

            conexion.sendall(respuesta.encode("utf-8"))

            conexion.close()

    except KeyboardInterrupt:
        print("\nServidor detenido")

    servidor.close()


if __name__ == "__main__":
    main()
