import numpy as np
import matplotlib.pyplot as plt
x1 =[0.25,1.25,2.25,3.25,4.25]
y1= [10,55,80,32,40]
x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,10,29,66]

plt.scatter(x1,y1, label='Datos 1', color='red' )
plt.scatter(x2,y2, label='Datos 2', color='blue')

plt.title('Graficos de Dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.legend()
plt.show()

