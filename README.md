SIMULACRO PRR

Autor: Maria Arroba Gomezjover

DESCRIPCION

Aplicacion cliente-servidor TCP desarrollada en Python.

El servidor lee frases desde un fichero llamado "frases" y atiende peticiones de clientes.

COMANDOS SOPORTADOS

FRASE
Devuelve una frase aleatoria del fichero.

TOTAL
Devuelve el numero total de frases y lineas.

Cualquier otro comando
Devuelve ERROR.

PUERTO

11041

ARCHIVOS

mensaje.py
Implementa la logica de los mensajes.

test_mensaje.py
Contiene los tests unitarios desarrollados con TDD.

servidor.py
Servidor TCP.

cliente.py
Cliente TCP.

frases
Fichero de frases utilizado por el servidor.

Makefile
Automatiza la ejecucion de pruebas y programas.

DESARROLLO TDD

Se han realizado pruebas unitarias para:

* Comando desconocido devuelve ERROR.
* TOTAL devuelve el numero de frases.
* TOTAL devuelve el numero de lineas.
* FRASE devuelve una frase valida.

CODIFICACION

UTF-8

SISTEMA OPERATIVO

Linux / Ubuntu

HERRAMIENTAS

Python 3
Git
Visual Studio Code

EJECUCION

1. Abrir un terminal y ejecutar:

make servidor

El servidor quedará esperando conexiones en el puerto 11041.

2. Abrir un segundo terminal y ejecutar:

make cliente

3. Introducir la direccion del servidor:

127.0.0.1

4. Introducir uno de los siguientes comandos:

FRASE

Devuelve una frase aleatoria.

TOTAL

Devuelve el numero de frases y lineas.

Cualquier otro texto, por ejemplo:

HOLA

Devuelve:

ERROR

5. Para finalizar el servidor utilizar Ctrl+C.

PRUEBAS

Ejecutar:

make test

para lanzar todos los tests unitarios.

