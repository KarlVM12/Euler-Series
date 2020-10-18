import numpy as np
import math

def function(x, y):
    return math.pow(x, 2) * y - 0.5*math.pow(y,2)

x0 = 0
y0 = 5
yMax = 1
xF = 1
deltaX = 0.2
n = 6

x = np.linspace(x0, xF, n)

y = np.zeros([n])

y[0] = y0

for i in range(1, n):
    y[i] = y[i-1] + (deltaX * function(x[i-1], y[i-1]))

for i in range(n):
    print(x[i], y[i])
