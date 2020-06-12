contraseña=0
while contraseña<5:
    contraseña=contraseña +1
    clave=input("ingrese su clave")
    if str(clave)=="Info2020":
        print("CLAVE CORRECTA")
        break
    else:
        print("CLAVE INCORRECTA")
        if contraseña==5:
            print("CUENTA BLOQUEADA")
