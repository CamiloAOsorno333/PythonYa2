"""
1. Realizar un programa que solicite la carga por teclado de dos números, si el primero 
es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y
 la división del primero respecto al segundo.

2. Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje
 "Promocionado".

3. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje 
indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

"""

#Solución 

# 1
print("Por favor ingrese dos números, para saber cual es el mayor")

num1=int(input("Ingrese el primer número= "))

num2=int(input("Ingrese el segundo número= "))

if num1 > num2:
    sum=print("La suma de los dos números es " + str(num1 + num2))
    diferencia=print("La diferencia de los dos números es " + str(num1 - num2))
elif num2 > num1:
    producto=print("El producto de los dos números es " + str(num1 * num2))
    division=print("La division de los dos números es " + str(num1 / num2))
else:
    print("Los números son iguales, por favor intentelo de nuevo") 

"""
Nota= En lugar de hacer conversión de datos con str(numero), podermos utilizar la f, de la siguiente manaera
        print(f" La suma de los números es= {num1 - num2}") y así con todas las operaciones
"""