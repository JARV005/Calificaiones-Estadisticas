#Tarea 1: Determinar el estado de aprobación:

#Determinar si estudiante aprueba o no
while True:
    try:
        Calificacion=float(input("Ingrese una calificación (0 a 100) "))
        if Calificacion<0 or Calificacion>100:
            print("Ingrese una califiacion entre 0 y 100")

        if Calificacion>=50 and Calificacion<100: 
            print("Aprobado")
            break
        elif Calificacion<50 and Calificacion>=0:
            print("Reprobado")
            break
        
        
    except ValueError:
        print("Ingrese un valor numerico ")

#Tarea 2: Calcular el promedio:

ListaC=[]
x=int(input("¿Cuantas calificaciones desea ingresar ? "))

for y in range(x):
    try: 
        VariasC=int(input("Ingrese la calificacion "))
        if Calificacion<0 or Calificacion>100:
            print("Ingrese una califiacion entre 0 y 100")
        ListaC.append(VariasC)
    except ValueError:
        print("Ingrese un valor numerico ")

print(ListaC)