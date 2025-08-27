import statistics

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [5.4, 6.2, 4.8]},
    {"nombre": "María", "notas": [6.0, 5.9, 6.7]},
    {"nombre": "Carlos", "notas": [3.5, 4.2, 5.0]},
    {"nombre": "Sofía", "notas": [7.0, 6.8, 6.9]},
    {"nombre": "Pedro", "notas": [4.0, 3.8, 5.2]},
    {"nombre": "Elena", "notas": [5.5, 6.1, 5.7]},
    {"nombre": "Javier", "notas": [2.9, 3.5, 4.0]},
    {"nombre": "Claudia", "notas": [6.4, 6.7, 6.0]},
    {"nombre": "Diego", "notas": [5.2, 4.9, 6.1]},
    {"nombre": "Valentina", "notas": [6.9, 6.5, 7.0]},
    {"nombre": "Andrés", "notas": [4.3, 5.1, 4.7]},
    {"nombre": "Camila", "notas": [5.8, 6.2, 6.0]},
    {"nombre": "Fernando", "notas": [3.7, 4.0, 4.5]},
    {"nombre": "Isabel", "notas": [6.6, 6.9, 6.4]},
    {"nombre": "Rodrigo", "notas": [4.8, 5.0, 5.5]},
    {"nombre": "Gabriela", "notas": [6.3, 5.9, 6.8]},
    {"nombre": "Mateo", "notas": [2.5, 3.2, 3.8]},
    {"nombre": "Josefina", "notas": [5.7, 6.1, 6.3]},
    {"nombre": "Tomás", "notas": [4.2, 4.9, 5.3]},
    {"nombre": "Paula", "notas": [6.8, 6.5, 6.9]},
    {"nombre": "Ignacio", "notas": [5.0, 5.4, 4.8]},
    {"nombre": "Marta", "notas": [6.2, 6.0, 5.9]},
    {"nombre": "Sebastián", "notas": [3.9, 4.5, 4.2]},
    {"nombre": "Francisca", "notas": [7.0, 6.8, 6.6]},
    {"nombre": "Nicolás", "notas": [4.7, 5.1, 5.4]},
    {"nombre": "Daniela", "notas": [6.3, 6.7, 6.1]},
    {"nombre": "Cristóbal", "notas": [3.6, 4.0, 4.3]},
    {"nombre": "Victoria", "notas": [6.5, 6.9, 7.0]},
    {"nombre": "Felipe", "notas": [5.3, 4.9, 5.7]},
]

# 1-. 

promedio_estudiantes = []
estudiantes_todo_aprobado = 0
estudiantes_materia_reprobada = 0


for estudiante in estudiantes:
    if all(nota >= 4.0 for nota in estudiante["notas"]):
        estudiantes_todo_aprobado += 1
    else:
        estudiantes_materia_reprobada += 1
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    promedio = round(promedio, 2)
    promedio_estudiantes.append({"nombre": estudiante["nombre"], "promedio": promedio})

promedio_minimo = min(promedio_estudiantes, key=lambda x: x["promedio"])
promedio_maximo = max(promedio_estudiantes, key=lambda x: x["promedio"])
print(promedio_minimo)
print(promedio_maximo)


# 2-.cantidad de estudiantes con todos los ramos aprobados

print(f"Estudiantes con todos los ramos aprobados: ", estudiantes_todo_aprobado)

# 3-. Moda
todas_las_notas = [nota for estudiante in estudiantes for nota in estudiante["notas"]]
modas = statistics.multimode(todas_las_notas)
print(f"las modas son: ", modas)

#4-. al menos una reprobada

porcentaje_reprobado = (estudiantes_materia_reprobada / len(estudiantes))*100
porcentaje_reprobado = round(porcentaje_reprobado, 2)
print(f"Estudiantes con al menos un ramo reprobado: ", porcentaje_reprobado)

# 5-.
promedio_estudiantes.sort(key=lambda e: e["promedio"], reverse=True)
for estudiante in promedio_estudiantes:
  print(estudiante)

