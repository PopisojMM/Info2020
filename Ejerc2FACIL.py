i=0
while i<5:
    i=i +1
    clave=input("ingrese su clave")
    if str(clave)=="Info2020":
        print("CLAVE CORRECTA")
        break
    else:
        print("CLAVE INCORRECTA")
        if i==5:
            print("CUENTA BLOQUEADA")