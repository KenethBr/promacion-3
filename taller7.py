def calcular_promedio_viento(lista_velocidades):
    suma_total = sum(lista_velocidades)
    promedio = suma_total / 15
    return promedio

#Aquí puede cambiar los datos mientras el valor sea igual o entre 0 y 30
datos_marzo = [12, 15, 28, 10, 5, 20, 25, 30, 18, 14, 22, 9, 11, 27, 16]

resultado = calcular_promedio_viento(datos_marzo)
print(f"La media aritmética de la velocidad del viento es: {resultado} km/h")