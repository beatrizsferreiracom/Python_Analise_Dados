#Criando Gráficos Customizados com Pylab

import matplotlib as mpl

#O Pylab combina funcionalidades do pyplor com funcionalidades do Numpy
from pylab import *

#Gráfico de Linha

#Dados
x = linspace(0, 5, 10)
y = x ** 2

#Cria a figura
fig = plt.figure()

#Define a escala dos eixos
axes = fig.add_axes([0, 0, 0.8, 0.8])

#Cria o plot
axes.plot(x, y, 'r')

#Labels e Título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')
plt.show()

#Gráfico de Linha com 2 Figuras

#Dados
x = linspace(0, 5, 10)
y = x ** 2

#Cria a figura
fig = plt.figure()

#Cria os eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) #eixos da figura secundária

#Figura principal
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

#Figura secundária
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')
plt.show()

#Gráfico de Linha em Paralelo

#Dados
x = linspace(0, 5, 10)
y = x ** 2

#Divide a área de plotagem em dois subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)

#Loop pelos eixos para criar cada plot
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

#Ajusta o layout
fig.tight_layout()
plt.show()