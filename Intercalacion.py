def intercalacion(lista1, lista2):
    resultado = []
    i = j = 0
    print("\nProceso de Intercalación:")
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            print(f"Agrega {lista1[i]} de lista1 → {resultado}")
            i += 1
        else:
            resultado.append(lista2[j])
            print(f"Agrega {lista2[j]} de lista2 → {resultado}")
            j += 1
    while i < len(lista1):
        resultado.append(lista1[i])
        print(f"Agrega {lista1[i]} restante de lista1 → {resultado}")
        i += 1
    while j < len(lista2):
        resultado.append(lista2[j])
        print(f"Agrega {lista2[j]} restante de lista2 → {resultado}")
        j += 1
    return resultado

print("INTERCALACIÓN")
n1 = int(input("¿Cuántos datos tendrá la primera lista? "))
lista1 = [input(f"Elemento {i+1} de la lista 1: ") for i in range(n1)]
lista1.sort()

n2 = int(input("¿Cuántos datos tendrá la segunda lista? "))
lista2 = [input(f"Elemento {i+1} de la lista 2: ") for i in range(n2)]
lista2.sort()

print("Lista 1 ordenada:", lista1)
print("Lista 2 ordenada:", lista2)

resultado = intercalacion(lista1, lista2)
print("\nLista intercalada final:", resultado)
