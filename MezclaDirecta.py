def merge_sort(lista, nivel=0):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], nivel+1)
    derecha = merge_sort(lista[medio:], nivel+1)
    resultado = merge(izquierda, derecha, nivel)
    return resultado

def merge(izq, der, nivel):
    resultado = []
    i = j = 0
    print("  " * nivel + f"Mezclando {izq} y {der}")
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado += izq[i:]
    resultado += der[j:]
    print("  " * nivel + f"→ {resultado}")
    return resultado

print("\nMEZCLA DIRECTA")
n = int(input("¿Cuántos datos desea introducir? "))
datos = [input(f"Dato {i+1}: ") for i in range(n)]
print("Lista original:", datos)
ordenado = merge_sort(datos)
print("\nLista ordenada final:", ordenado)
