#Construindo Plots

import matplotlib as mpl

import matplotlib.pyplot as plt

#O método plot() define os eixos do gráfico

plt.plot([1, 3, 5], [2, 4, 7])
plt.show()

x = [2, 3, 5]
y = [3, 5, 7]

plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend()
plt.show()