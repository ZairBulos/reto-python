"""
  Día 4 - Tuplas y diccionarios
"""

# Tuplas
settings = ('localhost', 3306, 'root', 'password', 'database')

## Desempaquetado de tuplas
host, port, username, password, database = settings
host, port, *_ = settings
host, port, *_, database = settings

## Tuplas anidadas
numbers = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

# Diccionarios
user = {
    'name' : 'Zair',
    'age': 22
}

user_name = user['name']
user_age = user['age']

## Llave == Objecto inmutable

## Validar llave en diccionario
if 'email' in user:
    # do something
    pass

## Obtener el valor de una llave
user_email = user.get('email', 'Default value')

## Obtener llaves de un diccionario
user_keys = list( user.keys() )

## Obtener valores de un diccionario
user_values = list( user.values() )