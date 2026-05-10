import numpy as np
from Bezier import Bezier
import matplotlib.pyplot as plt
rng = np.random.default_rng()

def generar_curva_aleatoria():
    p = rng.integers(0, 50, size=(4, 2))
    return Bezier(p)

b1 = generar_curva_aleatoria()
b2 = generar_curva_aleatoria()

b1.graficar(poligonal=False, curve_color="darkviolet", pc_color="darkviolet")
b2.graficar(poligonal=False, curve_color="blue", pc_color="blue")

def transformacion(b1: Bezier, b2: Bezier):
    L = np.array([b1.puntos_de_control[0], b1.puntos_de_control[len(b1.puntos_de_control) - 1]]).transpose()
    Q = np.array([b2.puntos_de_control[len(b2.puntos_de_control) - 1], b2.puntos_de_control[0]]).transpose()

    print("L ES INV? det(L)="+str(np.linalg.det(L)))

    Linv = np.linalg.inv(L)
    A = Q @ Linv

    pc = b1.puntos_de_control
    pc_nuevo = []
    for p in pc:
        pc_nuevo.append(A @ p)
    return Bezier(pc_nuevo)

T_b1 = transformacion(b1,b2)

b2.graficar(poligonal=False, curve_color="blue", pc_color="blue", show_plot=False)
T_b1.graficar(poligonal=False, curve_color="darkviolet", pc_color="darkviolet", show_plot=False)

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()