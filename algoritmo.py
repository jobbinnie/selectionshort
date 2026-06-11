lista = int(input("Digita el tamaño de la lista: "))
numeros = []

for _ in range(lista):
    numero = int(input("Digita un número: "))
    numeros.append(numero)

def selection_sort(numeros):
    for i in range(len(numeros)):
        min_index = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[min_index]:
                min_index = j
        numeros[i], numeros[min_index] = numeros[min_index], numeros[i]
    return numeros
print(selection_sort(numeros))