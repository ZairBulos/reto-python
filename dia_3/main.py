"""
  Día 3 - Listas
"""

# Índices     0          1         2       3           4
#            -5          -4       -3       -2         -1
courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails'] 

# Último elemento
last_index = len(courses) - 1
last_index = courses[-1]

# Sublistas - start:stop:skips
python_courses = courses[:3]
ruby_courses = courses[-2:]
random_courses = courses[::2]
inverse_courses = courses[::-1]

# Asignar nuevos valores a índices
courses[-1] = 'JavaScript'

# Métodos
courses.append('TypeScript')

courses.insert(3, 'Data Analytics')

new_courses = ['Java', 'Spring Boot', 'Docker']
courses.extend(new_courses)

courses.remove('Python')

courses.count('Python')

is_ruby_in_courses = 'Ruby' in courses

ruby_index = courses.index('Ruby')

# Iterar listas
for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(f'Índice {index}, valor {course}')