import numpy as np
import matplotlib.pyplot as plt

x1 = [3, 4, 5, 6]
y1 = [5, 6, 3, 4]
x2 = [2, 5, 8]
y2 = [3, 4, 3]

plt.bar(x1, y1, label= 'linea 1', linewidth =4,  color='brown')
plt.bar(x2, y2, label= 'linea 2', linewidth =4,  color='purple')

plt.title('diagram barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.legend()
plt.grid()
plt.show()

