import numpy as np
import matplotlib.pyplot as plt 

f = 10
fs = 1000
t = np.linspace(0, 0.1, 11)
y = np.sin(2 * np.pi * f * t)

plt.stem(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Senoidal')
plt.show()