import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#print("Dimensiones:", consumo.ndim)
#print("Forma:", consumo.shape)
#print("Tipos de datos:", consumo.dtype)
#print("Consumo del primer hogar:", consumo[0])
#print("Consumo el miercoles (dia 3):", consumo[:,2])

#Promedio de consumo por hogar
promedio_por_hogar=np.mean(consumo, axis=1)

#Promedio de consumo por hogar
promedio_por_dia=np.mean(consumo, axis=0)

#Promedio de consumo por hogar
total_consumo=np.sum(consumo)

#print(promedio_por_hogar)
#print(promedio_por_dia)
#print(total_consumo)

#Maximos por hogar
maximos=np.max(consumo, axis=1)

#Minimo por dia
minimos=np.min(consumo, axis=0)

#Desviacion estandar global
desviacion=np.std(consumo)

#print(maximos)
#print(minimos)
#print(desviacion)

#Suma por hogar (semana)
consumo_total_hogar= np.sum(consumo, axis=1)

#Compara cada hogar con un valor mayor a 100
altos=consumo_total_hogar > 100

#Filtrando hogares que cumplen la condicion:
consumo_mayor_100= np.where(altos)[0]

#print(f"Ids de hogares con consumo mayor a 100")

#Indice del hogar con mayor consumo
hogar_mayor_consumo= np.argmax(consumo_total_hogar)

#Indice del hogar con mejor consumo
hogar_mas_eficiente= np.argmin(consumo_total_hogar)

#print(consumo_total_hogar)
#print(hogar_mayor_consumo)
#print(hogar_mas_eficiente)

#Aplicando normalizacion MinMax al conjunto de datos
consumo_normalizado= (consumo - consumo.min())/(consumo.max()-consumo.min())


#------------------------------------------- Cuestionario de Trabajo -------------------------------------------------------------------------------------

# 1) ¿Cuál es el consumo del hogar 5 el viernes (día 5)?

consumodelhogar5elviernes= consumo[4,4]
print("El consumo del hogar numero 5 para el dia viernes fue de:", consumodelhogar5elviernes, "Kw/h")

# Tal como se enseño en la guia, como se pide un dato especifico, 
# se indica que imprima el dato de la columna 5 y fila 5, pero en phyton se empieza de 0 por lo que seria el indice 4


# 2)  Usando indexación, muestra el consumo de los últimos 3 hogares el domingo

consumoeldomingodelosultimos3hogares = consumo[-3:, -1]
print("El consumo en los últimos 3 hogares el dia domingo fue de :", consumoeldomingodelosultimos3hogares, "Kw/h")

# De forma parecida se indica la ubicacion de los datos que se necesita conocer, 
# pero con el menos 3 y los dos puntos se indica que deben ser los ultimos 3 hogares y el -1 indica que son los datos del ultimo dia es decir la ultima columna


# 3) Consumo promedio en el fin de semana

promedio_fin_de_semana = np.mean(consumo[:, 5:7]) 
print("El promedio de consumo en el fin de semana fue de:", promedio_fin_de_semana, "Kw/h" )

# Se usa el comando que se nos enseño "mean", se seleccionan todas las filas y unicamente las columanas 5 y 6, 
# que son el sabado y el domingo y el axis 0 refleja que se trabaja con los datos para cada dia


# 4) ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.


desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_por_dia)
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(f"El día con mayor desviación estándar fue el {dias_semana[dia_mayor_desviacion]} con una desviacion de ({desviacion_por_dia[dia_mayor_desviacion]:.2f})")

# Lo que refleja que el dia con mayor desviacion haya sido el viernes es que para ese dia en especifico los hogares
# tuvieron consumos muy diferentes entre si, es decir que no hubo un comportamiento promedio, cada hogsar tuvo una tendencia de consumo diferente 


# 5) Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.

consumo_total = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total)[:3]
valores_menor_consumo = consumo_total[indices_menor_consumo]
print("Los indices de los 3 hogares con menor consumo fueron:", indices_menor_consumo)
print("Los valores de consumo para esos hogares fueron de:", valores_menor_consumo, "Kw/h")

#Aca lo primero que se hace es que se suma el consumo de cada hogar en cada dia de la semana, luego ordena los hogares segun menor haya sido su consumo y toma
#los tres hogares que consumieron menos, luego se obtienen los valores y se imprimen los indices 


# 6) Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?

nuevo_consumo_hogar3 = consumo[2] * 1.10
nuevo_total_hogar3 = round(np.sum(nuevo_consumo_hogar3),2)
print("El nuevo consumo total del hogar 3 aumentando un 10% es de:", nuevo_total_hogar3,"Kw/h")

# Primero se multiplica el valor del consumo del hogar 3 (indice 2) por 1.10 para suponer que aumento un 10% su consumo por dia, luego
# se suma el consumo de cada dia para conocer el mensual y ya se imprime cual es su nuevo consumo 