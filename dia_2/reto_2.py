"""
    Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

    Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

    Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

    Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

    Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

    Así mismo el número de teléfono será a 10 dígitos.

    Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.
"""

users = int(input('¿Cúantos usuarios desea ingresar?: '))

for user in range(users):
    print(f'----- USUARIO {user + 1} -----')

    # Nombre
    name = input('Ingrese nombre: ')
    while not (5 <= len(name) <= 50):
        print('El nombre debe tener entre 5 y 50 caracteres.')
        name = input('Ingrese nombre: ')

    # Apellido
    last_name = input('Ingrese apellido: ')
    while not (5 <= len(last_name) <= 50):
        print('El apellido debe tener entre 5 y 50 caracteres.')
        last_name = input('Ingrese apellido: ')

    # Número de teléfono
    phone = input('Ingrese número de teléfono: ')
    while not (len(phone) == 10):
        print('El número de teléfono debe tener 10 dígitos.')
        phone = input('Ingrese número de teléfono: ')

    # Correo electrónico
    email = input('Ingrese correo electrónico: ')
    while not (5 <= len(email) <= 50):
        print('El correo electrónico debe tener entre 5 y 50 caracteres.')
        email = input('Ingrese correo electrónico: ')