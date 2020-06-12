preguntas=input("Ingrese el total de preguntas: ")
preguntas=int(preguntas)
respuestas=input("Ingrese el total de respuestas correctas: ")
respuestas=int(respuestas)
if 100 / preguntas*respuestas >= 90:
    print("Excelente")
elif 100 / preguntas*respuestas >= 70:
    print("Bueno")
elif 100 / preguntas*respuestas >= 60:
    print("Aprobado")
elif 100 / preguntas*respuestas < 60:
    print("No Alcanzó")