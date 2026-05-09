import numpy as np
import matplotlib.pyplot as plt

class Bezier:
    def __init__(self, punto_de_control):
        self.puntos_de_control = punto_de_control

    def punto_en_t(self, t):
        p0 = self.puntos_de_control[0]
        p1 = self.puntos_de_control[1]
        p2 = self.puntos_de_control[2]
        p3 = self.puntos_de_control[3]

        return ((1-t)**3) * p0 + 3*((1-t)*2)*t*p1 + 3* (1-t) * (t**2)*p2 + (t**3)*p3

p0 = np.array([-5,0])
p1 = np.array([2,-2])
p2 = np.array([9,6])  
p3 = np.array([16,3])  
control = [p0,p1,p2,p3]

curva = Bezier(control)

## Punto c.

def aplicarFuncion(funcion, lista_de_t):
    puntos = []

    for i in range(101):
        t = lista_de_t[i]
        puntos.append([t, funcion(t)])

    data = np.array(puntos)
    x = data[:, 0]  # los t
    y = data[:, 1]  # los f(t)
    return [x, y]

def b0(t):
    return (1-t)**3
def b1(t):
    return 3*((1-t)**2)*t
def b2(t):
    return 3*(1-t)*(t**2)
def b3(t):
    return t**3

def graficar(datos, color, label):
    plt.plot(datos[0], datos[1], color=color, label=label)  # Curva

lista_de_t =  np.arange(0, 1.01, 0.01)
p_b0 = aplicarFuncion(b0, lista_de_t)
p_b1 = aplicarFuncion(b1, lista_de_t)
p_b2 = aplicarFuncion(b2, lista_de_t)
p_b3 = aplicarFuncion(b3, lista_de_t)

graficar(p_b0, 'red', 'B0')
graficar(p_b1, 'blue', 'B1')
graficar(p_b2, 'green', 'B2')
graficar(p_b3, 'darkviolet', 'B3')

plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.show()