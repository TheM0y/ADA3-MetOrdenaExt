import os

def dividir_archivo(nombre, archivo1, archivo2):
    with open(nombre, 'r', encoding='utf-8') as archivo:
        datos = archivo.read().split()
        mitad = len(datos) // 2
        with open(archivo1, 'w', encoding='utf-8') as a1, open(archivo2, 'w', encoding='utf-8') as a2:
            a1.write(' '.join(datos[:mitad]))
            a2.write(' '.join(datos[mitad:]))
    print(f"\nArchivo '{nombre}' dividido en '{archivo1}' y '{archivo2}'.")

def leer_archivo(nombre):
    with open(nombre, 'r', encoding='utf-8') as archivo:
        return archivo.read().split()

def escribir_archivo(nombre, datos):
    with open(nombre, 'w', encoding='utf-8') as archivo:
        archivo.write(' '.join(datos))

print("\nMEZCLA EQUILIBRADA (simulada con archivos)")
n = int(input("¿Cuántos datos desea introducir? "))
datos = [input(f"Dato {i+1}: ") for i in range(n)]
escribir_archivo("original.txt", datos)

print("\nDatos originales escritos en 'original.txt':", datos)

# Dividir y ordenar
dividir_archivo("original.txt", "a.txt", "b.txt")
a = sorted(leer_archivo("a.txt"))
b = sorted(leer_archivo("b.txt"))

print("\nLista A ordenada:", a)
print("Lista B ordenada:", b)

# Mezclar
resultado = []
i = j = 0
print("\nProceso de mezcla:")
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        resultado.append(a[i])
        print(f"Agrega {a[i]} de A → {resultado}")
        i += 1
    else:
        resultado.append(b[j])
        print(f"Agrega {b[j]} de B → {resultado}")
        j += 1
while i < len(a):
    resultado.append(a[i])
    print(f"Agrega {a[i]} restante de A → {resultado}")
    i += 1
while j < len(b):
    resultado.append(b[j])
    print(f"Agrega {b[j]} restante de B → {resultado}")
    j += 1

print("\nLista ordenada final:", resultado)

# Limpiar archivos
for archivo in ["original.txt", "a.txt", "b.txt"]:
    if os.path.exists(archivo):
        os.remove(archivo)
