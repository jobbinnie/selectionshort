lista = input("ingresa lista de números separados por un espacio o comas: ")
lista_limpia = lista.replace(",", " ").split()
ingreso = [int(x) for x in lista_limpia]

def selection_sort(ingreso):
    largo = len(ingreso)
    for i in range(largo - 1):
        min_index = i

        for j in range(i + 1, largo):
            if ingreso[j] < ingreso[min_index]:
                min_index = j         
        ingreso[i], ingreso[min_index] = ingreso[min_index], ingreso[i]
    return ingreso
print(selection_sort(ingreso))
