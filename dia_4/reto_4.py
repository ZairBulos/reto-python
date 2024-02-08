"""
    Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

    Puntualmente 4 nuevas funcionalidades. Aquí van.

        1. Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

        2. Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

        3. Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

        4. Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

    Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

    De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.
"""

MIN_LEN_STR, MAX_LEN_STR = 5, 50
MIN_LEN_NUM = 10

ERROR_LEN_STR = f'El valor debe tener entre {MIN_LEN_STR} y {MAX_LEN_STR} caracteres.'
ERROR_LEN_NUM = f'El valor debe tener {MIN_LEN_NUM} dígitos.'

users = []

while True:
    # MENÚ
    print('--------------- CÓDIGO FACILITO ---------------')
    print('1 - Registrar nuevos usuarios')
    print('2 - Listar IDs de usuarios registrados')
    print('3 - Obtener información de un usuario')
    print('4 - Editar información de un usuario')
    print('5 - Salir')
    print('-----------------------------------------------')

    # OPCIÓN
    while True:
        option = int(input('Ingrese una opción: '))

        if not (0 <= option <= 5):
            print('Lo sentimos, la opción ingresada no es valida.')
        else:
            break

    # REGISTRO
    if option == 1:
        print('\n---------- REGISTRO ----------')

        users_amount = int(input('¿Cúantos usuarios desea ingresar?: '))

        for user_id in range(users_amount):
            # Identificador único
            id = user_id + 1
            
            print(f'----- REGISTRO DE USUARIO Nº{id} -----')

            # Nombre
            while True:
                name = input('Ingrese nombre: ')

                if not (MIN_LEN_STR <= len(name) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Apellido
            while True:
                last_name = input('Ingrese apellido: ')

                if not (MIN_LEN_STR <= len(last_name) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Número de teléfono
            while True:
                phone = input('Ingrese número de teléfono: ')

                if not (len(phone) == MIN_LEN_NUM):
                    print(ERROR_LEN_NUM)
                else:
                    break

            # Correo electrónico
            while True:
                email = input('Ingrese correo electrónico: ')

                if not (MIN_LEN_STR <= len(email) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Usuario registrado
            user = {
                'id': id,
                'name': name,
                'last_name': last_name,
                'phone': phone,
                'email': email
            }

            # Lista de usuarios
            users.append(user)

    # LISTADO
    elif option == 2:
        print('\n-------- LISTADO DE IDs --------')

        users_ids = [ user['id'] for user in users ]
        print(users_ids)
    
    # INFORMACIÓN
    elif option == 3:
        print('\n-------- INFORMACIÓN DE USUARIO --------')

        user_id = int(input('Ingrese ID del usuario a buscar: '))

        found_user = None

        for user in users:
            if user['id'] == user_id:
                found_user = user
                break

        if found_user:
            print(found_user)
        else:
            print(f'Lo sentimos, el usuario con id {user_id} no existe.')

    # EDICIÓN
    elif option == 4:
        print('\n--------- EDICIÓN DE USUARIO --------')

        user_id = int(input('Ingrese ID del usuario a editar: '))

        found_user = None

        for user in users:
            if user['id'] == user_id:
                found_user = user
                break

        if found_user:
            # Nombre
            while True:
                name = input('Ingrese nombre: ')

                if not (MIN_LEN_STR <= len(name) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Apellido
            while True:
                last_name = input('Ingrese apellido: ')

                if not (MIN_LEN_STR <= len(last_name) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Número de teléfono
            while True:
                phone = input('Ingrese número de teléfono: ')

                if not (len(phone) == MIN_LEN_NUM):
                    print(ERROR_LEN_NUM)
                else:
                    break

            # Correo electrónico
            while True:
                email = input('Ingrese correo electrónico: ')

                if not (MIN_LEN_STR <= len(email) <= MAX_LEN_STR):
                    print(ERROR_LEN_STR)
                else:
                    break

            # Usuario editado
            found_user['name'] = name
            found_user['last_name'] = last_name
            found_user['phone'] = phone
            found_user['email'] = email

        else:
            print(f'Lo sentimos, el usuario con id {user_id} no existe.')

    # SALIR
    else:
        break
