from unicodedata import numeric
import numpy as np
from time import time


def armijo(eta, x, p, f0, f1, c1=1e-4, rho=0.5):
    """
    Función que verifica si el tamaño de paso satisface la condición de Armijo
    f(x+eta*p)<=f(x)+c1*eta*gradient(f(x))*p

    Parameters
    ----------
    eta : 1*1
        Tamaño de paso actual.
    x : (N*1)
        Iteración actual.
    p : (N*1)
        Dirección de búsqueda.
    f0 : (RN->R)
        Función objetivo.
    f1 : (RN->RN)
        Gradiente de la función.
    c1 : (1*1)
        Constante proporcionada por el usuario en el rango [0,0.5].
    rho : (1*1)
        Constante proporcionada por el usuario en el rango [0,1].

    Returns
    -------
    valor de eta si la condición se cumple.

    """

    j = 1
    while (j > 0):
        x_new = x + eta*p
        if (f0(x_new) <= f0(x)+c1*eta*np.dot(f1(x), p)):
            j = 0
            eta_armijo = eta
        else:
            eta = eta*rho

    return eta_armijo


def linear_search(x0, F, gradF, tol=1e-4, delta_rest=0.8, c1=1e-4, rho=0.2, maxIter=100):
    """
    Parameters
    ----------
    X0 : (2*1)
        Puntos iniciales.
    F : (lambda function)
        Función objetivo.
    gradF : (lambda function)
        Gradiente de la función objetivo.
    tol : (float64), optional
        Tolerancia del método de LS. The default is 1e-4.
    delta_rest : (float64), optional
        Evalúa para reiniciar el algoritmo. The default is 0.8.
    c1 : (float64), optional
        Constante definida por el usuario. Condición de Armijo. The default is 1e-4.
    rho : (float64), optional
        Constante definida por el usuario. Condición de Armijo. The default is 0.2.

    Retorna
    -------
    X0 : (2,1)
        Valor óptimo de la función.
    F(X): (2,1)
        Función evaluada en el valor mínimo X0.
    Xit : (k,1)
        Vector de trayectorias de X.
    """

    t0 = time()

    x = x0
    k = 0
    xx = []
    xx.append(x)

    gradF_x0 = gradF(x0)

    currentIter = 0

    while (np.linalg.norm(gradF_x0) > tol):

        if currentIter >= maxIter:
            print('Max iter reached')
            break

        # Dirección
        if (k == 0):
            p = -gradF_x0
        else:
            p = -gradF_x0 + beta*p

        # ARMIJO
        eta_guess = 0.5*np.abs(np.dot(gradF_x0, p))/(np.linalg.norm(p))**2
        # eta = armijo(eta_guess,x0,p,F,gradF)
        eta = armijo(eta_guess, x, p, F, gradF)

        # NEW POINT
        # xnew = x0 + eta*p
        x = x + eta*p
        # gradF_xnew = gradF(xnew)
        gradF_xnew = gradF(x)

        # Expresión Fletcher-Reeves
        beta = (np.linalg.norm(gradF_xnew)/np.linalg.norm(gradF_x0))**2

        # Prueba para reinicar
        test = np.abs(np.dot(gradF_xnew, gradF_x0)) > delta_rest*(F(x0))**2
        if (test):
            k = 0
        else:
            k += 1

        # Actualiza y almacena el valor
        x0 = x
        gradF_x0 = gradF_xnew
        xx.append(x)

        # print(f'current iteration: {currentIter}')
        currentIter += 1
        # print((np.linalg.norm(gradF_x0) > tol) or (currentIter < maxIter))

    # Solución
    return F(x0), np.asarray(xx)  # , currentIter, time() - t0


def num_df(F, X, i, h=1e-6):
    Xph = X.copy()
    Xmh = X.copy()
    Xph[i] += h
    Xmh[i] -= h
    return (F(Xph) - F(Xmh)) / (2*h)


def numeric_gradient(F, X, h=1e-6):
    # n = len(X)
    # grad = []
    # for i in range(n):
    #     partial = num_df(F, X, i, h)
    #     grad.append(partial)
    # return np.array(grad)

    return (F(X+h) - F(X-h))/(2*h)

def armijo_numeric(eta, x, p, f0, f1, c1=1e-4, rho=0.5):
    """
    Función que verifica si el tamaño de paso satisface la condición de Armijo
    f(x+eta*p)<=f(x)+c1*eta*gradient(f(x))*p

    Parameters
    ----------
    eta : 1*1
        Tamaño de paso actual.
    x : (N*1)
        Iteración actual.
    p : (N*1)
        Dirección de búsqueda.
    f0 : (RN->R)
        Función objetivo.
    f1 : (RN->RN)
        Gradiente de la función.
    c1 : (1*1)
        Constante proporcionada por el usuario en el rango [0,0.5].
    rho : (1*1)
        Constante proporcionada por el usuario en el rango [0,1].

    Returns
    -------
    valor de eta si la condición se cumple.

    """

    j = 1
    while (j > 0):
        x_new = x + eta*p
        if (f0(x_new) <= f0(x)+c1*eta*np.dot(f1(f0, x), p)):
            j = 0
            eta_armijo = eta
        else:
            eta = eta*rho

    return eta_armijo


def linear_search_numeric(x0, F, tol=1e-4, delta_rest=0.8, c1=1e-4, rho=0.2, maxIter=10000):
    """
    Parameters
    ----------
    X0 : (2*1)
        Puntos iniciales.
    F : (lambda function)
        Función objetivo.
    gradF : (lambda function)
        Gradiente de la función objetivo.
    tol : (float64), optional
        Tolerancia del método de LS. The default is 1e-4.
    delta_rest : (float64), optional
        Evalúa para reiniciar el algoritmo. The default is 0.8.
    c1 : (float64), optional
        Constante definida por el usuario. Condición de Armijo. The default is 1e-4.
    rho : (float64), optional
        Constante definida por el usuario. Condición de Armijo. The default is 0.2.

    Retorna
    -------
    X0 : (2,1)
        Valor óptimo de la función.
    F(X): (2,1)
        Función evaluada en el valor mínimo X0.
    Xit : (k,1)
        Vector de trayectorias de X.
    """

    x = x0
    k = 0
    xx = []
    xx.append(x)

    gradF_x0 = numeric_gradient(F, x0)

    currentIter = 0

    while (np.linalg.norm(gradF_x0) > tol):

        if currentIter >= maxIter:
            print('MaxIter reached')
            break

        # if len(xx) > 2:
        #     if np.linalg.norm(xx[-2] - xx[-1]) < tol:
        #         print('x converged')
        #         break

        # Dirección
        if (k == 0):
            p = -gradF_x0
        else:
            p = -gradF_x0 + beta*p

        # ARMIJO
        eta_guess = 0.5*np.abs(np.dot(gradF_x0, p))/(np.linalg.norm(p))**2
        # eta = armijo_numeric(eta_guess,x0,p,F,gradF)
        eta = armijo_numeric(eta_guess, x, p, F, numeric_gradient)

        # NEW POINT
        # xnew = x0 + eta*p
        x = x + eta*p
        # gradF_xnew = gradF(xnew)
        gradF_xnew = numeric_gradient(F, x)

        # Expresión Fletcher-Reeves
        beta = (np.linalg.norm(gradF_xnew)/np.linalg.norm(gradF_x0))**2

        # Prueba para reinicar
        test = np.abs(np.dot(gradF_xnew, gradF_x0)) > delta_rest*(F(x0))**2
        if (test):
            k = 0
        else:
            k += 1

        # Actualiza y almacena el valor
        x0 = x
        gradF_x0 = gradF_xnew
        xx.append(x)

        # print(f'current iteration: {currentIter}')
        currentIter += 1
        # print((np.linalg.norm(gradF_x0) > tol) or (currentIter < maxIter))

    # Solución
    # print(f'Iter: {currentIter}')
    return F(x0), np.asarray(xx), currentIter+1
