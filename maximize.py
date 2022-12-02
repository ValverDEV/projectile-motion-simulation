import numpy as np
import matplotlib.pyplot as plt
from busqueda_lineal import linear_search_numeric

V = float(input('V: '))
y = float(input('y: '))
g = 9.81

X0 = 90


def F(O): 
    return -(V*np.cos((O*np.pi/180))/g) * (V*np.sin((O*np.pi/180)) + np.sqrt(V**2 * np.sin((O*np.pi/180))**2 - 2*g*y))

tol = 1e-6
nk = 1e-2

Fmin, xk, num_iters = linear_search_numeric(X0, F, tol=tol)
Fmin *= -1
theta = xk[-1]
print(Fmin)
print(theta, 'grads')