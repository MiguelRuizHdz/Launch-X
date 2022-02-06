# program.py

# Ejecutar programa con el comando en la consola
# python program.py
sum = 1 + 2
print(sum)

# Impresión en pantalla 
print('Hola desde la consola')

# Variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True # boolean
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# distancia_a_alfa_centauri = 4.367 # Parece un decimal flotante
# Saber el tipo de una variable con la función:type()
# type(distancia_a_alfa_centauri)
# Declaramos la variable
distancia_a_alfa_centauri = 4.367
# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# Operadores
left_side = 10
right_side = 5
# Division
left_side / right_side # 2

# Operadores aritméticos
# +	Operador de adición que suma dos valores juntos	
# 1 + 1
# -	Operador de resta que quita el valor del lado derecho del lado izquierdo
# 1 - 2
# /	Operador de división que divide el lado izquierdo tantas veces como especifique el lado derecho
# 10 / 2
# *	Operador de multiplicación
# 2 * 2

# Operadores de asignación
# =	
# x = 2
# x ahora contiene 2.
# +=
# x += 2
# x incrementado en 2. Si antes contenía 2, ahora tiene un valor de 4.
# -=
# x -= 2
# x decrementado por 2. Si antes contenía 2, ahora tiene un valor de 0.
# /=
# x /= 2
# x dividido por 2. Si antes contenía 2, ahora tiene un valor de 1.
# *=
# x *= 2
# x multiplicado por 2. Si antes contenía 2, ahora tiene un valor de 4.


# Fechas
# Importamos la biblioteca 
from datetime import date
# Obtenemos la fecha de hoy
date.today()
# Mostramos la fecha en la consola
print(date.today())

# Conversión de tipos de datos
print("Today's date is: " + str(date.today()))

# Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))