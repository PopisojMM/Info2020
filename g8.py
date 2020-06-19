''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    N estudiantes toman K manzanas y las distribuyen entre ellas de manera uniforme. 
    La parte restante (la indivisible) permanece en la cesta. 
    ¿Cuántas manzanas obtendrá cada estudiante? 
    ¿Cuántas manzanas quedarán en la canasta?
    El programa lee los números N y K. 
    Debe imprimir las dos respuestas para las preguntas anteriores.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

#n = float(input("Cúantos estudiantes son?: "))
#k = float(input("Cúantas manzanas tienen?: "))
#division = k // n
#division2 = k % n
#respuesta = print("Cada estudiante obtendrá ", division, " manzanas y sobran ", division2)

'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Escriba un programa que pregunte primero si se quiere calcular 
    el área de un triángulo o la de un círculo. Si se contesta que se 
    quiere calcular el área de un triángulo (escribiendo T o t), el 
    programa tiene que pedir entonces la base y la altura y escribir el área. 
    Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), 
    el programa tiene que pedir entonces el radio y escribir el área.
    Se recuerda que el área de un triángulo es base por altura dividido 
    por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

    Por ejemplo:
    Elija una figura geométrica:
    a) Triángulo
    b) Círculo
    ¿Qué figura quiere calcular (Escriba T o C)? T
    Escriba la base: 3
    Escriba la altura: 5.5
    Un triángulo de base 3.0 y altura 5.0 tiene un área de 8.25
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea


#pregunta = str(input("Sobre que figura desea calcular?\n \033[1;36m T = Triangulo \n \033[1;33m C = Circulo \033[1;37m \n Ingrese la opción: "))
#preguntaMayusculas = pregunta.upper()
#
#if preguntaMayusculas == "T":
#    altura = float(input("Ingrese la altura del triangulo: "))
#    base = float(input("Ingrese la base del triangulo: "))
#    print ("\033[1;36m El área del triángulo es: ", base * altura / 2)
#elif preguntaMayusculas == "C":
#    radio = float(input("Ingrese el radio del circulo: "))
#    print ("\033[1;33m el área del círculo es: ", 3.141592 * radio ** 2)
'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Escribir un programa el cual lea dos valores enteros. 
    Si el primero es menor que el segundo, que imprima el mensaje 
    ``Arriba''. Si el segundo es menor que el primero, que imprima 
    el mensaje ``Abajo''. Si los números son iguales, que imprima el 
    mensaje ``igual''. Si alguno de los datos ingresados es igual a 0, 
    que imprima un mensaje conteniendo la palabra ``Error''.
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea

print("\033[1;37mBienvenidos a ¿Donde está el valor más bajo?\n")
valor1 = int(input("Ingrese un primer valór: "))
valor2 = int(input("Ingrese un segundo valór: "))

while (valor1 == 0 or valor2 == 0):
    print ("\n\033[1;31mError, solo puede ingresar números mayores a 0\033[1;37m\n") 
    print("Por favor, vuelva a ingresar los valores\n")
    valor1 = int(input("Ingrese un primer valór: "))
    valor2 = int(input("Ingrese un segundo való"": "))
else:
    if valor1 == valor2:
        print("\n\033[1;32m¡Ambos números son iguales!\033[1;37m\n")
#        int(input("Ingrese un primer valór: "))
#        int(input("Ingrese un segundo valór: "))
    if valor1 > valor2:
        print("\n\033[1;32m¡Arriba!\033[1;37m\n")
#        int(input("Ingrese un primer valór: "))
#        int(input("Ingrese un segundo valór: "))
    if valor1 < valor2:
        print("\n\033[1;32m¡Abajo!\033[1;37m\n")
#        int(input("Ingrese un primer valór: "))
#        int(input("Ingrese un segundo valór: "))
'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Solicitar al usuario que ingrese números enteros positivos y, 
    por cada uno, imprimir la suma de los dígitos que lo componen. 
    La condición de corte es que se ingrese el número -1. Al finalizar, 
    mostrar cuántos de los números ingresados por el usuario fueron 
    números pares.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea
