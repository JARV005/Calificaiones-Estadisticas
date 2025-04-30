#Tarea 1: Determinar el estado de aprobación:

#Determinar si estudiante aprueba o no
while True:
    try:
        Calificacion=float(input("Ingrese una calificación (0 a 100) "))
        if Calificacion<0 or Calificacion>100:
            print("Ingrese una califiacion entre 0 y 100")

        if Calificacion>=50 and Calificacion<=100: 
            print("Aprobado")
            break
        elif Calificacion<50 and Calificacion>=0:
            print("Reprobado")
            break
        
        
    except ValueError:
        print("Ingrese un valor numerico ")

#Tarea 2: Calcular el promedio:
# Solicitar al usuario la lista inicial de calificaciones
calificaciones = input("Ingresa las calificaciones separadas por comas (0-100): ")
ListaC = []

# Validar la lista inicial de calificaciones
for C in calificaciones.split(','):
    try:
        calificacion = float(C.strip())
        if calificacion>=0 and calificacion<= 100:
            ListaC.append(calificacion)
        else:
            print(f"La calificación {calificacion} no es válida. Debe estar entre 0 y 100.")
    except ValueError:
        print(f"{C} no es un número válido.")

# Bucle para agregar más calificaciones si el usuario desea
while True:
    continuar = input("¿Deseas ingresar más calificaciones? (si/no): ").lower()
    if continuar == 'si':
        nuevasC = input("Ingresa las nuevas calificaciones separadas por comas (0-100): ")
        nuevas = []
        for C in nuevasC.split(','):
            try:
                calificacion = float(C.strip())
                if calificacion>=0 and calificacion<= 100:
                    nuevas.append(calificacion)
                else:
                    print(f"La calificación {calificacion} no es válida. Debe estar entre 0 y 100.")
            except ValueError:
                print(f"{C} no es un número válido.")
        
        # Añadir solo las calificaciones válidas
        ListaC.extend(nuevas)
    elif continuar == 'no':
        break
    else:
        print("Respuesta no válida. Escribe 'si' para sí o 'no' para no.")

# Mostrar lista final
print(F"Lista final de calificaciones: {ListaC}")

#Calcular el promedio
suma=sum(ListaC)
CantidadD=len(ListaC)
prom=suma/CantidadD
print(f"Promedio calificaciones en lista: {prom}")

contador=0

#Ingresar un valor y determinar que calificaciones son mayores al valor ingresado 

CalifMay=float(input("Ingrese un valor especifico (entre 0 y 100) "))
Mayores=[]
for C in calificaciones.split(','):
    C=float(C)
    if C>CalifMay:
        Mayores.append(C)
print(f"Las calificaciones mayores a {CalifMay} son: {Mayores}") 
