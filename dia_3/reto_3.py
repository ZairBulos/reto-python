"""
  Para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

  Estas funcionalidades son las siguientes:

    1. Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. 
    Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
  
    2. Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. 
    Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.
"""

MIN_LEN_STR = 5
MAX_LEN_STR = 50
MIN_LEN_NUM = 10

users_amount = int(input('¿Cúantos usuarios desea ingresar?: '))
users = []

# Registro Usuarios
for user in range(users_amount):
    print(f'----- REGISTRO DE USUARIO Nº{user + 1} -----')

    # Nombre
    while True:
        name = input('Ingrese nombre: ')

        if not (MIN_LEN_STR <= len(name) <= MAX_LEN_STR):
            print('El nombre debe tener entre 5 y 50 caracteres.')
        else:
            break

    # Apellido
    while True:
        last_name = input('Ingrese apellido: ')

        if not (MIN_LEN_STR <= len(last_name) <= MAX_LEN_STR):
            print('El apellido debe tener entre 5 y 50 caracteres.')
        else:
            break

    # Número de teléfono
    while True:
        phone = input('Ingrese número de teléfono: ')

        if not (len(phone) == MIN_LEN_NUM):
            print('El número de teléfono debe tener 10 dígitos.')
        else:
            break

    # Correo electrónico
    while True:
        email = input('Ingrese correo electrónico: ')

        if not (MIN_LEN_STR <= len(email) <= MAX_LEN_STR):
            print('El correo electrónico debe tener entre 5 y 50 caracteres.')
        else:
            break

    # Lista de IDs
    users.append(user + 1)

print('\n----- IDENTIFICADORES ÚNICOS DE USUARIOS REGISTRADOS -----')

# Imprimir Identificadores Únicos de Usuarios Registrados
print(users)