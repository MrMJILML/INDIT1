import numpy as np
import matplotlib.pyplot as plt

# Daten für die Sinuskurve generieren
x = np.linspace(0, 2 * np.pi, 10000)
y = np.sin(x)

# Diagramm erstellen
plt.plot(x, y)

# Achsenbeschriftungen
plt.xlabel('x')
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['0', 'π/2', 'π', '3π/2', '2π']) # Die x-Achse soll in pi/2 Schritten beschriftet sein
plt.ylabel('sin(x)')
plt.title('sin')

# Diagramm anzeigen
plt.show()