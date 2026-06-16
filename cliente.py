import socket

PUERTO = 11041

def main():
    direccion = input("Dirección del servidor: ")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((direccion, PUERTO))

        mensaje = input("Comando: ")

        cliente.sendall(mensaje.encode("utf-8"))

        respuesta = cliente.recv(1024).decode("utf-8")

        print("Respuesta:", respuesta)

        cliente.close()

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor")

if __name__ == "__main__":
    main()
