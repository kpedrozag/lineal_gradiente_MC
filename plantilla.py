# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

#Load Dataset
dataSet=np.loadtxt("ex1data2.txt",delimiter=',')
x=dataSet[:,[0,1]]
y=dataSet[:,2]

tetha = np.zeros(3)
m = len(tetha)
alfa = 0.001
N = int(len(x)*0.8)
test = len(x) - N

for q in range(1000):

    for j in range(m):

        sumatoria_hx_y_x = 0

        for n in range(N):

            suma_hx = 0
            for i in range(m):
                suma_hx += tetha * x[n][i]

            sumatoria_hx_y_x += (suma_hx - y[n]) * x[n][j]
        t_temp = tetha[j] - ((alfa / N) * sumatoria_hx_y_x)












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
