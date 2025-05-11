def mezcla_equilibrada(lista):
    print("\nDividiendo la lista en dos partes...")
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    print("Parte izquierda:", izquierda)
    print("Parte derecha:", derecha)

    izquierda.sort()
    derecha.sort()

    print("Izquierda ordenada:", izquierda)
    print("Derecha ordenada:", derecha)

    resultado = []
    i = j = 0
    print("\nProceso de mezcla equilibrada:")
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            print(f"Agrega {izquierda[i]} de izquierda → {resultado}")
            i += 1
        else:
            resultado.append(derecha[j])
            print(f"Agrega {derecha[j]} de derecha → {resultado}")
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        print(f"Agrega {izquierda[i]} restante de izquierda → {resultado}")
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        print(f"Agrega {derecha[j]} restante de derecha → {resultado}")
        j += 1

    return resultado

print("\nMezcla Equilibrada")
n = int(input("¿Cuántos datos desea introducir? "))
datos = [input(f"Dato {i+1}: ") for i in range(n)]

print("\nLista original:", datos)
resultado = mezcla_equilibrada(datos)
print("\nLista ordenada final:", resultado)
