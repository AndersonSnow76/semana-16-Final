# -----------------------------------------------------------
# Tarea: Trabajo con Archivos de Texto en Python
# Autor: [Tu nombre]
# Descripción: Este programa crea un archivo de texto, escribe
# algunas notas personales, luego las lee y muestra en consola.
# -----------------------------------------------------------

# --- Escritura de Archivo de Texto ---

# Abrimos (o creamos) el archivo "my_notes.txt" en modo escritura ("w")
# Si el archivo no existe, Python lo creará automáticamente.
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("1. Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("2. Es importante cerrar los archivos después de usarlos.\n")
    file.write("3. Usar 'with open()' facilita el manejo automático del cierre.\n")

# En este punto, el archivo se cierra automáticamente gracias a 'with'

# --- Lectura de Archivo de Texto ---

# Abrimos el archivo en modo lectura ("r")
file = open("my_notes.txt", "r", encoding="utf-8")

# Leemos y mostramos el contenido línea por línea
print("Contenido del archivo my_notes.txt:\n")
linea = file.readline()  # Lee la primera línea

# El bucle continúa hasta que no haya más líneas
while linea:
    print(linea.strip())  # strip() elimina saltos de línea extra
    linea = file.readline()

# --- Cierre del Archivo ---
file.close()  # Cerramos el archivo manualmente

print("\nArchivo cerrado correctamente.")