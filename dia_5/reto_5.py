"""
    Llegamos al reto número 5 de la semana. Nuestro programa ya funciona sumamente bien. Ya podemos crear, listar y editar usuarios.
    
    Nuestro programa ya funciona sumamente bien. Ya podemos crear, listar y editar usuarios.

    Sin embargo, muy probablemente el código que tengamos hasta ahora pueda mejorar significativamente, es por ello que, para el reto de hoy vamos a definir 5 nuevas funciones; esto con la finalidad de poder separar nuestro código y que este sea fácil de leer, comprender y sobre todo mantener.

    Las 5 nuevas funciones serán las siguientes.
        - new_user
        - show_user
        - edit_user
        - delete_user
        - list_users

    Las funciones, como bien sus nombre nos indican, nos permitirán seperar nuestra lógica para poder crear nuevos usuarios, consultarlos, editarlos, eliminarlos (Que es una nueva acción) y listarlos.
    Con Excepción de list_users, cada una de estas funciones deberá recibir como parámetro el ID de usuario con el cual se desea trabajar.
"""

MIN_LEN_STR, MAX_LEN_STR = 5, 50
MIN_LEN_NUM = 10

ERROR_LEN_STR = f'El valor debe tener entre {MIN_LEN_STR} y {MAX_LEN_STR} caracteres.'
ERROR_LEN_NUM = f'El valor debe tener {MIN_LEN_NUM} dígitos.'
ERROR_USER_NOT_FOUND = F'Lo sentimos, el usuario no existe.'

user_id = 0
users = {}


def exists_user(id):
    return id in users


def validate_str(message):
    while True:
        value = input(message)

        if not (MIN_LEN_STR <= len(value) <= MAX_LEN_STR):
            print(ERROR_LEN_STR)
        else:
            return value


def validate_num(message):
    while True:
        value = input(message)

        if not (len(value) == MIN_LEN_NUM):
            print(ERROR_LEN_NUM)
        else:
            return value


def create_user_values():
    name = validate_str('Ingrese nombre(s): ')
    last_name = validate_str('Ingrese apellido(s): ')
    phone = validate_num('Ingrese número de teléfono: ')
    email = validate_str('Ingrese correo electrónico: ')

    return name, last_name, phone, email


def create_id():
    global user_id
    user_id += 1

    return str(user_id)


def new_user():
    id = create_id()
    name, last_name, phone, email = create_user_values()

    users[id] = {
        'id': id,
        'name' : name,
        'last_name' : last_name,
        'phone' : phone,
        'email' : email
    }


def show_user(id):
    if exists_user(id):
        print(users[id])
    else:
        print(ERROR_USER_NOT_FOUND)


def edit_user(id):
    if exists_user(id):
        name, last_name, phone, email = create_user_values()

        users[id] = {
            'id': id,
            'name' : name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }
    else:
        print(ERROR_USER_NOT_FOUND)


def delete_user(id):
    if exists_user(id):
        users.pop(id)
    else:
        print(ERROR_USER_NOT_FOUND)


def list_users():
    if users:
        print(users)
    else:
        print('No hay usuarios registrados.')


menu = {
    '1' : new_user,
    '2' : list_users,
    '3' : show_user,
    '4' : edit_user,
    '5' : delete_user,
    '6' : exit
}


def print_menu():
    print('--------------- CÓDIGO FACILITO ---------------')
    print('1 - Registrar nuevo usuario')
    print('2 - Consultar usuarios registrados')
    print('3 - Obtener usuario registrado')
    print('4 - Editar usuario registrado')
    print('5 - Eliminar usuario registrado')
    print('6 - Salir')
    print('-----------------------------------------------')


def main_menu():
    while True:
        print_menu()
        option = input('Seleccione una opción: ')

        if option in menu:
            # Opciones donde se pide id
            if option == '3' or option == '4' or option == '5':
                id = input('Ingrese el ID del usuario: ')
                menu[option](id)
            
            # Otras opciones
            else:
                menu[option]()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == '__main__':
    main_menu()