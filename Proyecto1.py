import numpy as np
import matplotlib.pyplot as plt 

f = 10
t = np.linspace(0, 0.1, 101)
y = np.sin(2 * np.pi * f * t)

plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Senoidal')
plt.show()