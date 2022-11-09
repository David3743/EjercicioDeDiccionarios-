#Hacer un programa para hacer gestión de estudiantes utilizando como contenedor un diccionario.
# Los atributos de un estudiante son: código, nombre, apellidos, y tres notas. Debe permitir agregar,
# modificar, eliminar, ver alguno y ver todos, además algunas estadísticas como promedios –listado-,
# promedio de un estudiante, promedio general, el mejor estudiante (con toda su información incluido promedio)
# y el peor estudiante (ídem).​
numeros = 9

salon= {1: {"codigo": 101, "nombre": "Juan", "apellido":  "Lopez", "nota1": 1.0, "nota2": 2.0, "nota3": 4.0},
        2: {"codigo": 102, "nombre": "Camilo", "apellido":  "Jimenez", "nota1": 4.0, "nota2": 2.3, "nota3": 4.1},
        3: {"codigo": 103, "nombre": "Eduard", "apellido":  " Meza", "nota1": 5.0, "nota2": 2.2, "nota3": 4.3},
        4: {"codigo": 104, "nombre": "Pablo", "apellido":  "Flores", "nota1": 3.0, "nota2": 2.1, "nota3": 4.2},
        5: {"codigo": 105, "nombre": "David", "apellido":  "Vargas", "nota1": 2.0, "nota2": 2.5, "nota3": 4.5},
        6: {"codigo": 106, "nombre": "Gabriela", "apellido":  "Montero", "nota1": 1.6, "nota2": 2.4, "nota3": 4.6},
        7: {"codigo": 107, "nombre": "Daniel", "apellido":  "Mejia", "nota1": 1.7, "nota2": 2.6, "nota3": 4.7},
        8: {"codigo": 108, "nombre": "Daniela", "apellido":  "Mendoza", "nota1": 1.2, "nota2": 2.7, "nota3": 4.8},
        9: {"codigo": 109, "nombre": "María", "apellido":  "Garcia", "nota1": 1.9, "nota2": 2.9, "nota3": 4.9}}

def agregarEstudiantes(numeros):
        i = int(input("Ingrese el numero de estudiantes que quiere agregar"))
        for a in range(i):
                salon[numeros+1]={"codigo": input("Ingrese el codigo del estudiantes"), "nombre": input("Ingrese el nombre del estudiante"), "apellido":input("Ingrese el apellido del estudiante"), "nota1": input("ingrese la primera nota "), "nota2": input("Ingrese la segunda nota"), "nota3":input("Ingrese la tercera nota ")}
                numeros+=1
def modificarDato():
        a = int(input("Ingrese el codigo del estudiante  en numeros enteros"))
        for i in range(1, len(salon)):
                if a==salon[i]["codigo"]:
                        h = int(input("Que dato quiere modificar? \n1-codigo \n 2-nombre \n 3-Apellido \n 4-nota 1 \n 5-nota 2\n 6-nota 3"))
                        if h ==1:
                                c = int(input("Ingrese el nuevo codigo del estudiante"))
                                salon[i].update(codigo=c)
                        elif h ==2:
                                c = input("Ingrese el nuevo nombre del estudiante")
                                salon[i].update(nombre=c)
                        elif h ==3:
                                c = input("Ingrese el nuevo apellido del estudiante")
                                salon[i].update(apellido=c)
                        elif h ==4:
                                c = int(input("Ingrese la nueva nota 1  del estudiante"))
                                salon[i].update(nota1=c)
                        elif h == 5:
                                c = int(input("Ingrese la nueva nota  2 del estudiante"))
                                salon[i].update(nota2=c)
                        else:
                                c = int(input("Ingrese la nueva nota 2 del estudiante"))
                                salon[i].update(nota3=c)
def eliminarEstudiante():
        numero= int(input("Ingrese el código del estudiante que quiere eliminar\n->"))
        for i in range(1, len(salon)):
                if salon[i]["codigo"]== numero:
                        del salon[i]
        print(salon)
def calcularNotas():
        opc= int(input("¿Qué opción desea?\n1. Promedio de cada estudiante\n2. Promedio general del salón\n->"))
        if opc== 1:
                for i in range(1, len(salon)):
                        x1= salon[i]["nota1"]
                        x2= salon[i]["nota2"]
                        x3= salon[i]["nota3"]
                        print(salon[i]["nombre"], salon[i]["apellido"], "Nota promedio: ", ((x1+x2+x3)/3))
        promedioGeneral= 0
        if opc== 2:
                for i in range(1, len(salon)):
                        x1= salon[i]["nota1"]
                        x2= salon[i]["nota2"]
                        x3= salon[i]["nota3"]
                        promedioGeneral+= (x1+x2+x3)/3

                promedioGeneral/= len(salon)
                print("Promedio general: ", promedioGeneral)

opcion= 1
while opcion != 0:

        switchh = int(input("Ingrese la opcion que desea\n 0 - salir \n 1-mostrar estudiantes \n 2-Agergar estudiante\n 3-modificar Dato \n 4- Eliminar estudiante \n 5- Calcular notas\n->"))

        if switchh ==1:
                for i in salon:
                        print(salon[i])
        if switchh ==2:
                agregarEstudiantes(numeros)
        if switchh ==3:
                modificarDato()
        if switchh ==4:
                eliminarEstudiante()
        if switchh ==5:
                calcularNotas()
        if switchh==0:
                break

