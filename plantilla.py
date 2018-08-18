# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


# tr: numero de datos usados para entrenamiento (N)
# ft: features (x)
# hp: array de thetas. hipotesis (theta)
# op: outputs (y)
def error(tr, ft, hp, op):
    e = 0.0
    for i in range(tr, len(ft)):
        e += (np.dot(hp, ft[i]) - op[i])**2
    return e

# Load Dataset
dataSet=np.loadtxt("ex1data2.txt",delimiter=',')
x=dataSet[:,[0,1]] # features
y=dataSet[:,2] # outputs

theta = np.zeros(3) # array de theta
m = len(theta) # tamaño del vector theta
alfa = 0.001 # alpha: define convergencia del algoritmo
N = int(len(x)*0.8) # Cantidad de inputs para entrenamiento
# test = len(x) - N # cantidad de inputs para testing

for q in range(1000): # 1000 iteraciones
    theta_temp = np.zeros(3) # array de thetas temporal, se reinicia en 0 al inicio de cada iteracion
    for j in range(m): # calculo de cada theta
        sumatoria_hx_y_x = 0 # sumatoria(*) de 0 hasta N datos de entrada
        for n in range(N): # calculo de la sumatoria(*)
            sumatoria_hx_y_x += (np.dot(theta, x[n]) - y[n]) * x[n][j] # proceso de la sumatoria
        theta_temp[j] = theta[j] - ((alfa / N) * sumatoria_hx_y_x) # theta temporal
    theta = theta_temp.copy() # actualizacion de theta

print("Con la hipotesis:", theta, "se obtiene un error de:\n", error(N, x, theta, y), end='\n\n')

#Create a 3d plot
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

#Plot y vector from testing data
ax.scatter(x[:,0], x[:,1], y, c='b', marker='o')

#Set labels' names
ax.set_xlabel('$Area$')
ax.set_ylabel('$Rooms$')
ax.set_zlabel('$Price$')

#Set plot's title
ax.set_title("Data Set")

#Set plot's elevation
ax.view_init(elev=20)

#Create plot's legends
l1 = lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
ax.legend([l1], ['Examples'], numpoints = 1, loc=6)


plt.show()
