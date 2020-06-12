nombre=input('Ingrese un nombre')
nombre=str(pedro)
edad=input('Ingrese Edad')
edad=int(edad)
print(f"Mi nombre es {nombre}, tengo {edad} años")
if edad > 18:
    print("Y soy mayor de edad")
elif edad < 18:
    print("Y soy menor de edad")
elif edad == 18:
    print("y acabo de ser mayor de edad")