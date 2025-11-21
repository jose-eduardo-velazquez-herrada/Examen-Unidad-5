def main():
    while True:
        try:
            num_estudiantes = int(input("¿Cuántos estudiantes tiene el grupo? "))
            num_materias = int(input("¿Cuántas materias tiene el grupo? "))
            
            if num_estudiantes > 0 and num_materias > 0:
                break
            else:
                print("Por favor, ingrese números mayores a 0.")
        except ValueError:
            print("Por favor, ingrese números válidos.")

    calificaciones = []
    
    print("\n--- Captura de calificaciones (0-100) ---")
    for i in range(num_estudiantes):
        print(f"\nEstudiante {i + 1}:")
        estudiante = []
        
        for j in range(num_materias):
            while True:
                try:
                    calif = float(input(f"  Calificación materia {j + 1}: "))
                    if 0 <= calif <= 100:
                        estudiante.append(calif)
                        break
                    else:
                        print("    La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("    Por favor, ingrese un número válido.")
        
        calificaciones.append(estudiante)

    promedios_estudiantes = []
    for estudiante in calificaciones:
        promedio = sum(estudiante) / len(estudiante)
        promedios_estudiantes.append(promedio)

    promedios_materias = []
    for j in range(num_materias):
        suma_materia = 0
        for i in range(num_estudiantes):
            suma_materia += calificaciones[i][j]
        promedio_materia = suma_materia / num_estudiantes
        promedios_materias.append(promedio_materia)

    calif_maxima = max(max(fila) for fila in calificaciones)
    calif_minima = min(min(fila) for fila in calificaciones)

    print("\n" + "="*50)
    print("RESULTADOS FINALES")
    print("="*50)

    print("\n--- Matriz de Calificaciones ---")
    print("Estudiante\\Materia", end="")
    for j in range(num_materias):
        print(f"{j+1:>8}", end="")
    print("   Promedio")
    
    for i in range(num_estudiantes):
        print(f"Estudiante {i+1}:", end="")
        for j in range(num_materias):
            print(f"{calificaciones[i][j]:>8.1f}", end="")
        print(f"{promedios_estudiantes[i]:>10.1f}")

    print("\n--- Promedios por Materia ---")
    for j in range(num_materias):
        print(f"Materia {j+1}: {promedios_materias[j]:.1f}")

    print("\n--- Estadísticas Generales ---")
    print(f"Calificación más alta: {calif_maxima:.1f}")
    print(f"Calificación más baja: {calif_minima:.1f}")
    promedio_general = sum(promedios_estudiantes) / len(promedios_estudiantes)
    print(f"Promedio general del grupo: {promedio_general:.1f}")

if __name__ == "__main__":
    main()