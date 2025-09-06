import random

# Paso 1: Definir ciudades, días y semanas
cities = ["Quito", "Guayaquil", "Cuenca"]
days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
weeks = 2  # número de semanas

# Paso 2: Crear matriz 3D de temperaturas
temps = []
for city in cities:
    city_weeks = []
    for w in range(weeks):
        week_days = []
        for d in range(len(days)):
            temp = round(random.uniform(10, 30), 1)
            week_days.append(temp)
        city_weeks.append(week_days)
    temps.append(city_weeks)

# Paso 3: Calcular promedios
for ci in range(len(cities)):
    print(f"\nCiudad: {cities[ci]}")
    for wi in range(weeks):
        suma = 0
        for di in range(len(days)):
            suma += temps[ci][wi][di]
        promedio = suma / len(days)
        print(f"  Semana {wi+1}: Promedio = {promedio:.2f}")
