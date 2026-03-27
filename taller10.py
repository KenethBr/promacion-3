import numpy as np
import matplotlib.pyplot as plt

# 1. Generar 1000 datos aleatorios (Distribución Normal)
# Media deseada = 50, Desviación estándar = 10
datos = np.random.normal(loc=50, scale=10, size=1000)

# 2. Calcular Media y Mediana
media = np.mean(datos)
mediana = np.median(datos)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")

# 3. Crear el Histograma
plt.figure(figsize=(10, 6))
plt.hist(datos, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# 4. Agregar líneas para Media y Mediana
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='dotted', linewidth=2, label=f'Mediana: {mediana:.2f}')

# Personalización
plt.title('Histograma de Datos Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Mostrar gráfica
plt.show()