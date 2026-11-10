def square_sum(numbers):
    #Crear un total que empiece en 0
    total = 0
    #Para cada número de la lista
    for n in numbers:
        #Elevarlo al cuadrado
        elevado = n**2
        #Sumarlo al total
        total += elevado
    #Devolver el total
    return total
    