import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()