from datetime import datetime

# Pedir el nombre del usuario
nombre = input('¿Cuál es tu nombre? ')
print(f'\n ¡Bienvenid@ a Python, {nombre}!\n')

print('Este es un bucle que imprime del 1 al 10:')
for num in range(1, 11):
    print(f'  ➤ Número: {num}')

# Obtener el día actual en español
dias = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

mensajes = {
    'Lunes': '¡Comenzamos la semana con energía!',
    'Martes': '¡Vamos avanzando con fuerza!',
    'Miércoles': '¡Mitad de semana, buen momento para revisar el progreso!',
    'Jueves': ' ¡Ya casi llegamos!',
    'Viernes': ' ¡Último esfuerzo, el fin de semana se acerca!',
    'Sábado': ' ¡Disfruta tu sábado y recarga energías!',
    'Domingo': ' ¡Hay que pensar que mañana no es Lunes... y listo!'
}

dia_actual = datetime.today().strftime('%A')
dia_traducido = dias.get(dia_actual, 'Día desconocido')

print(f'\n Hoy es: {dia_traducido}')
print(mensajes.get(dia_traducido, ' ¡No tengo un mensaje para este día!'))
