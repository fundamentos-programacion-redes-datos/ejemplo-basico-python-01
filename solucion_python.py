"""
    Ejemplo 1: Calcular el costo de un terreno, a partir de sus dimensiones y 
    el costo por metro cuadrado
"""

# Inicio

# Declaración de variables (Python no requiere especificar el tipo de dato previamente)
# Se capturan los valores mediante entrada de usuario con input()
# input() devuelve un valor de tipo "cadena de texto" (str), por lo que es necesario 
# convertirlo al formato que se necesita

largo_terreno = input("Ingrese el largo del terreno (en metros): ")  # Captura como texto
largo_terreno = float(largo_terreno)  # Convierte el texto a número decimal

ancho_terreno = input("Ingrese el ancho del terreno (en metros): ")  # Captura como texto
ancho_terreno = float(ancho_terreno)  # Convierte el texto a número decimal

costo_metro = input("Ingrese el costo por metro cuadrado: ")  # Captura como texto
costo_metro = float(costo_metro)  # Convierte el texto a número decimal

# Cálculo del área del terreno
# Se multiplica el largo por el ancho para obtener el área total
area_terreno = largo_terreno * ancho_terreno

# Cálculo del costo total del terreno
# Se multiplica el área obtenida por el costo del metro cuadrado
costo_total = area_terreno * costo_metro

# Mostrar los resultados en pantalla
# Se usa print() con f-strings para formatear la salida con dos decimales (.2f)
print(f"El área del terreno es: {area_terreno:.2f} metros cuadrados")
print(f"El costo total del terreno es: ${costo_total:.2f}")
