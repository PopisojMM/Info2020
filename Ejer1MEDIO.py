ventas1=input("Ingrese las ventas del dia 1 :")
ventas1=int(ventas1)
ventas2=input("ingrese las ventas del día 2 :")
ventas2=int(ventas2)
if ventas1 > ventas2:
    print("El día 1 se vendió más")
elif ventas1 < ventas2:
    print("El día 2 se vendió más")
elif ventas1 == ventas2:
    print("Se vendió lo mismo en ambos días")