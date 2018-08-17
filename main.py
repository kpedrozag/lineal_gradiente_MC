import math


def normalizar(val):
    suma = 0
    for i in range(len(val)):
        suma += val[i]
    media = suma / len(val)
    den = max(val) - min(val)
    salida = []
    for i in val:
        salida.append((i - media)/den)
    return salida


f = open("datos.txt", 'r')
X0 = []
Y = []
while True:
    a = f.readline()
    if not a:
        break
    a = a.split('\n')
    a = a[0].split(',')
    Y.append(int(a.pop()))
    aux = []
    for x in a:
        aux.append(float(x))
    X0.append(aux)

n1 = []
n2 = []
for x in X0:
    n1.append(x[0])
    n2.append(x[1])

sal1 = normalizar(n1)
sal2 = normalizar(n2)

X = []
for i in range(len(X0)):
    X.append([1, X0[i][0], X0[i][1]])
    print(X[i])

theta = [0 for i in range(len(X[0]))]
aux_t = [0 for i in range(len(theta))]
alpha = 0.001
error = 0.0001
it = 0

for q in range(10000):
    it += 1
    e = []
    h = 0

    for j in range(len(theta)):
        aux = 0

        for n in range(int(len(X) * 0.8)):
            aux2 = 0

            for i in range(len(theta)):
                aux2 += theta[i] * X[n][i]
            h = 1 / (1 + math.exp(-1 * aux2))
            mult = (h - Y[n]) * (X[n][j])
            aux = aux + mult
            # aux += ((1 / (1 + math.exp(-1 * aux2))) - Y[n]) * X[n][j]

        alf = alpha / (len(X))
        alf_sum = alf * aux
        aux_t[j] = aux_t[j] - alf_sum
        # aux_t[j] = theta[j] - alpha * (1 / len(X)) * aux

        e.append(alpha * abs((1 / len(X)) * aux))

    theta = aux_t[:]

    if (e[0] < error) or (e[1] < error) or (e[2] < error):
        break

print("El entrenamiento arrojo lo siguiente:", it)
for i in range(len(theta)):
    print("Theta", i, "=", theta[i])

x0 = X[len(X)-1][0]
x1 = X[len(X)-1][1]
x2 = X[len(X)-1][2]
y = 1

print(x0 * theta[0] + x1 * theta[1] + x2 * theta[2])
