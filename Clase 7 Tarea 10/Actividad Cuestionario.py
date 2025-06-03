import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3], #1
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8], #2
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8], #3
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],       #4
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8], #5
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5], #6
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9], #7
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0], #8
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7], #9
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],        #10
])
#Exploracion inicial de datos
print("Dimensiones: ", consumo.ndim)                    #2 (filas y columnas)
print("Forma: ", consumo.shape)                         #(10, 7) (filas, columnas)
print("Tipo de datos: ", consumo.dtype)                 #float64 (números decimales)
print("Consumo primer hogar: ", consumo[0])             #Todos los datos de la fila 0
print("Consumo el miércoles (día 3): ", consumo[:, 2])  #Todos los datos de la columna 2

#Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

#Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

#Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

#Máximo por hogar
maximos = np.max(consumo, axis=1)

#Mínimo por hogar
minimos = np.min(consumo, axis=0)

#Desviación estándar global
desviacion_estandar = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion_estandar)


#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

#Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

#Índice del hogar con menor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

#Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

#Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")

#MinMax

#Aplicando normalización Min Max al conjunto de datos
#consumo_normalizado = (consumo - np.min()) / (np.max() - np.min())

#Resultado
#print(consumo_normalizado)

#Cuestionario de trabajo
#1. Cual es el consumo del hogar 5 el viernes?
print("1. El consumo del hogar 5 el dia viernes fue " , consumo[4,4])

#2 Usando indexación, muestra el consumo de los últimos 3 hogares el domingo
print("2. El consumo de los últimos 3 hogares el domingo fue " , consumo[[7,8,9],6])

#3 Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
print("3. El promedio de consumo los fines de semana fue " , promedio_por_dia[5]," y ",promedio_por_dia[6])

#4 Que dia de la semana tiene la mayor desviación estandar entre hogares? Explica que indica esto
desviacion_estandar_dia = np.std(consumo, axis=0)
mayor_desviacion = np.argmax(desviacion_estandar_dia)
dias = ["lunes", "martes", "miercoles","jueves","viernes","sábado","domingo"]
print("4. El dia con mayor desviacion estandar es el ", dias[mayor_desviacion]) #Esto signfica que el sabado es cuando los hogares diferencian mas en su consumo de cada uno.

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
y = np.argsort(consumo_total_hogar)[:3]

print("Índices de los hogares: ", y)
print("Valores de los hogares:", consumo_total_hogar[y])

import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3], #1
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8], #2
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8], #3
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],       #4
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8], #5
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5], #6
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9], #7
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0], #8
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7], #9
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],        #10
])
#Exploracion inicial de datos
print("Dimensiones: ", consumo.ndim)                    #2 (filas y columnas)
print("Forma: ", consumo.shape)                         #(10, 7) (filas, columnas)
print("Tipo de datos: ", consumo.dtype)                 #float64 (números decimales)
print("Consumo primer hogar: ", consumo[0])             #Todos los datos de la fila 0
print("Consumo el miércoles (día 3): ", consumo[:, 2])  #Todos los datos de la columna 2

#Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

#Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

#Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

#Máximo por hogar
maximos = np.max(consumo, axis=1)

#Mínimo por hogar
minimos = np.min(consumo, axis=0)

#Desviación estándar global
desviacion_estandar = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion_estandar)


#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

#Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

#Índice del hogar con menor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

#Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

#Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")

#MinMax

#Aplicando normalización Min Max al conjunto de datos
#consumo_normalizado = (consumo - np.min()) / (np.max() - np.min())

#Resultado
#print(consumo_normalizado)

#Cuestionario de trabajo
#1. Cual es el consumo del hogar 5 el viernes?
print("1. El consumo del hogar 5 el dia viernes fue " , consumo[4,4])

#2 Usando indexación, muestra el consumo de los últimos 3 hogares el domingo
print("2. El consumo de los últimos 3 hogares el domingo fue " , consumo[[7,8,9],6])

#3 Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
print("3. El promedio de consumo los fines de semana fue " , promedio_por_dia[5]," y ",promedio_por_dia[6])

#4 Que dia de la semana tiene la mayor desviación estandar entre hogares? Explica que indica esto
desviacion_estandar_dia = np.std(consumo, axis=0)
mayor_desviacion = np.argmax(desviacion_estandar_dia)
dias = ["lunes", "martes", "miercoles","jueves","viernes","sábado","domingo"]
print("4. El dia con mayor desviacion estandar es el ", dias[mayor_desviacion]) #Esto signfica que el sabado es cuando los hogares diferencian mas en su consumo de cada uno.

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
y = np.argsort(consumo_total_hogar)[:3]

print("Índices de los hogares: ", y)
print("Valores de los hogares:", consumo_total_hogar[y])

#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
print("Consumo con aumento 10%:", consumo[2]+consumo[2]*0.1)
print("Consumo total :", np.sum(consumo[2]+consumo[2]*0.1))