"""
    Día 5 - Funciones
"""

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


# Ejemplo
def set_scores():
    scores = []

    for option in range(0, 5):
        score = int(input('Ingresa una calificación: '))
        scores.append(score)

    return scores


def average(numbers):
    return sum(numbers) / len(numbers)


def show_message(average)
    match average:
        case 10:
            print('Muchas felicidades, aprobaste la materia')
        case 9 | 8:
            print('Aprobaste la materia')
        case 7:
            print('Aprobaste la materia, necesitas practicas más')
        case _:
            print('Lo sentimos, no aprobaste la materia')


scores = set_scores()
avg = average(scores)
show_message(avg)