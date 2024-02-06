"""
  Día 2 - Estructuras de control
"""

# Condicionales
color = 'green'

if color == 'green':
    print('Puede continuar')
elif color == 'yellow':
    print('Alto parcial')
elif color == 'red':
    print('Alto total')
else:
    print('El color no es valido')

# match (switch)
match color:
    case 'green':
        print('Puede continuar')
    case 'yellow':
        print('Alto parcial')
    case 'red':
        print('Alto total')
    case _:
        print('El color no es valido')

# Ciclos
title = 'Estructuras de control'

for caracter in title:
    print(caracter)

for number in range(1, 101):
    print(number)


number = 1

while number < 101:
    print(number)
    number += 1

# Ejemplo
random, number, attends = 5, 0, 0

while number != random and attends < 5:
    number = int(input('Adivina el número: '))
    attends += 1
else:
    if number == random:
        print('Felicidades encontraste el número!')
    else:
        print('Lo sentimos, no encontraste el número')