def selection_sort(lista):
  for lugar_a_llenar in range(len(lista) - 1, 0, -1):
    posicion_maximo = 0
    for lugar in range(1, lugar_a_llenar + 1):
      if lista[lugar] > lista[posicion_maximo]:
        posicion_maximo = lugar

    # Intercambio de elementos
    aux = lista[lugar_a_llenar]
    lista[lugar_a_llenar] = lista[posicion_maximo]
    lista[posicion_maximo] = aux

l = [1, 25, -3, 20, 30, 10]

selection_sort(l)
print(l)
