"""
  Día 1 - Instalación y tipos de datos
"""

# String
first_name = 'Zair'
last_name = 'Bulos'
full_name = first_name + ' ' + last_name;

# int, float, bool
age = 22
score = 8.51
active = True

# Conocer tipo de dato
print(type(age))

# No existen constantes
VERSION = 1.0

# Ingreso de datos por teclado
input_result = input('Ingresa tu nombre: ')

# Conversión de tipos
name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))
score = float(input('Ingresa tu calificación: '))
active = input('El usuario se encuentra activo ? (si/no): ') == 'si'