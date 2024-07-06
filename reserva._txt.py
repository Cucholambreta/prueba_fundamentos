import numpy as np
import os

def cargar_datos():
    pacientes = np.empty((0, 8), dtype=object)
    try:
        with open('pacientes.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                pacientes = np.vstack([pacientes, np.array(data)])
    except FileNotFoundError:
        print("Archivo de pacientes no encontrado. Se creará uno nuevo al guardar los datos.")
    return pacientes


def guardar_datos(pacientes):
    with open('pacientes.txt', 'w') as file:
        for paciente in pacientes:
            file.write(','.join(paciente) + '\n')

listado_pacientes = cargar_datos()


def ingresar_ficha():
    nombre = input("Ingrese el nombre de la mascota: ")
    codigo = input("Ingrese el código de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    peso = input("Ingrese el peso de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    diagnostico = input("Ingrese el diagnostico del diagnostico de la consulta: ")
    medicamentos = input("Medicamentos recetados: ")

    nueva_ficha = np.array([[nombre, codigo, edad, peso, raza, especie, diagnostico, medicamentos]])
    return nueva_ficha

def buscar_por_codigo(pacientes, codigo):
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente[1] == codigo:
            paciente_encontrado = paciente
            break
    return paciente_encontrado

def eliminar_ficha(pacientes, codigo):
    pacientes_actualizados = [paciente for paciente in pacientes if paciente[1] != codigo]
    return np.array(pacientes_actualizados)

def listar_pacientes(pacientes):
    for i, paciente in enumerate(pacientes, start=1):
        print(f"Mascota {i}:")
        print(f"Nombre: {paciente[0]}")
        print(f"Codigo: {paciente[1]}")
        print(f"Edad: {paciente[2]}")
        print(f"Peso: {paciente[3]}")
        print(f"Raza: {paciente[4]}")
        print(f"Especie: {paciente[5]}")
        print(f"Diagnostico: {paciente[6]}")
        print(f"Medicamentos recetados: {paciente[7]}")
        print()

while True:
    print("Menú:")
    print("1. Crear Ficha de Mascota")
    print("2. Buscar ficha por codigo de mascota")
    print("3. Eliminar ficha de mascota por su código")
    print("4. Listar pacientes atendidos")
    print("5. Salir")
    
    opcion = input("Ingrese la opción que desea ingresar: ")

    if opcion == '1':
        nueva_ficha = ingresar_ficha()
        listado_pacientes = np.concatenate((listado_pacientes, nueva_ficha), axis=0)
        print("¡Ficha ingresada correctamente!")

    elif opcion == '2':
        codigo = input("Ingrese el codigo a buscar: ")
        paciente_encontrado = buscar_por_codigo(listado_pacientes, codigo)
        if paciente_encontrado is not None:
            print("Paciente encontrado:")
            print(f"El nombre de la mascota es: {paciente_encontrado[0]}")
            print(f"tiene {paciente_encontrado[2]} años")
            print(f"pesa {paciente_encontrado[3]} kilogramos")
            print(f"{paciente_encontrado[0]} es de raza {paciente_encontrado[4]}")
            print(f"su diagnostico es: {paciente_encontrado[6]}")
            print(f"los medicamentos recetados son: {paciente_encontrado[7]}")
        else:
            print("No se encontró ninguna mascota asociada al codigo.")

    elif opcion == '3':
            codigo = input("Ingrese el codigo de la mascota que desea eliminar: ")   
            listado_pacientes = eliminar_ficha(listado_pacientes, codigo)
            print("La ficha de la mascota ha sido eliminada correctamente.")


    elif opcion == '4':
        if len(listado_pacientes) > 0:
            print("Listado de mascotas atendidas:")
            listar_pacientes(listado_pacientes)
        else:
            print("No hay atenciones registradas.")

    elif opcion == '5':
        # Guardar los datos actualizados en el archivo de texto antes de salir
        guardar_datos(listado_pacientes)
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")
