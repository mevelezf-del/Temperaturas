# --- Datos de entrada (TODAS LAS 24 CAPITALES DE PROVINCIA) ---
# Diccionario con datos de temperaturas de las capitales de Ecuador.
temperaturas_ciudades = {
    # Sierra
    "Quito": [17, 18, 16, 17],
    "Cuenca": [18, 19, 17, 20],
    "Ambato": [19, 20, 18, 21],
    "Riobamba": [16, 17, 15, 18],
    "Ibarra": [22, 23, 21, 24],
    "Loja": [22, 21, 23, 24],
    "Tulcán": [12, 13, 11, 14],
    "Latacunga": [14, 15, 13, 16],
    "Guaranda": [15, 16, 14, 15],
    "Azogues": [17, 18, 16, 19],
    # Costa
    "Guayaquil": [30, 32, 31, 29],
    "Machala": [31, 30, 32, 33],
    "Portoviejo": [29, 30, 28, 31],
    "Esmeraldas": [28, 29, 27, 29],
    "Santo Domingo": [26, 27, 25, 28],
    "Babahoyo": [31, 33, 30, 32],
    "Santa Elena": [27, 28, 26, 28],
    # Amazonía
    "Macas": [25, 26, 24, 27],
    "Puyo": [24, 25, 23, 26],
    "Tena": [26, 27, 25, 28],
    "Nueva Loja": [28, 29, 27, 30],
    "Coca": [27, 28, 26, 29],
    "Zamora": [23, 24, 22, 25],
    # Galápagos
    "San Cristóbal": [26, 28, 25, 27]
}


# --- Definición de la Función (No necesita cambios) ---

def calcular_temperaturas_promedio(datos):
    """
    Calcula e imprime la temperatura promedio para cada ciudad en un diccionario.

    Parámetros:
    datos (dict): Un diccionario donde las claves son los nombres de las ciudades (str)
                  y los valores son listas de temperaturas (list de int o float).
    """
    print("--- Calculando Temperaturas Promedio de las Capitales de Ecuador ---")

    for ciudad, temperaturas in datos.items():
        suma_total = sum(temperaturas)
        cantidad_semanas = len(temperaturas)
        promedio = suma_total / cantidad_semanas
        print(f"- La temperatura promedio para {ciudad} es: {promedio:.2f}°C")


# --- Pruebas y Verificación ---
# La misma llamada a la función ahora procesará los 24 registros.
calcular_temperaturas_promedio(temperaturas_ciudades)