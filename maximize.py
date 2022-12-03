import numpy as np
from busqueda_lineal import linear_search_numeric

def maximize_x(V, y):

    g = 9.81

    X0 = 90


    def F(O): 
        return -(V*np.cos((O*np.pi/180))/g) * (V*np.sin((O*np.pi/180)) + np.sqrt(V**2 * np.sin((O*np.pi/180))**2 - 2*g*y))

    tol = 1e-6

    Fmin, xk, num_iters = linear_search_numeric(X0, F, tol=tol)
    Fmin *= -1
    theta = xk[-1]
    return Fmin, theta