import numpy as np
import matplotlib.pyplot as plt

##### PARTE A.
def BezierNoIterativa(t: int, p0, p1, p2):
    return ((1-t)**2) * p0 + 2*(1-t)*t*p1 + (t**2)*p2

p0 = np.array([0,0])
p1 = np.array([2,4])
p2 = np.array([4,0])

lista_de_t =  np.arange(0, 1.01, 0.01)
puntos = [] # lista de array([float, float])

for i in range(101):
    puntos.append(BezierNoIterativa(lista_de_t[i], p0,p1,p2))

data = np.array(puntos)
x = data[:, 0]
y = data[:, 1]

puntos_de_control = np.array([p0,p1,p2])

plt.plot(x, y, color='blue', label='Bézier')  # Curva
plt.plot(puntos_de_control[:, 0], puntos_de_control[:, 1], marker='o' ,linestyle='--',color='darkviolet', label='Puntos de control')

for i, punto in enumerate(puntos_de_control):
    plt.text(punto[0] + 0.1, punto[1] + 0.1, f'P{i}', fontsize=10, color='darkviolet')

plt.xlim(-1, 5)
plt.ylim(-1, 5)

# 2. Definir las marcas de los ejes cada 0.5
intervalo = np.arange(-1, 5.5, 0.5) # De -1 a 5 inclusive
plt.xticks(intervalo)
plt.yticks(intervalo)

plt.plot(x, y, color='red', alpha=0.3)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

### PARTE d.

def interpolar(t:int, p0, p1):
    return (1-t)*p0 + t*p1

def BezierIterativa(t: int, p0, p1, p2):
    Q0 = interpolar(t,p0,p1)
    Q1 = interpolar(t,p1,p2)
    return interpolar(t,Q0,Q1)

t_para_comparar = np.arange(0, 1.01, 0.1)

for t in t_para_comparar:
    b1 = BezierNoIterativa(t,p0,p1,p2)
    b2 = BezierIterativa(t,p0,p1,p2)
    print(f'- con t={round(t,1)}: iterativa = {b1} y no iterativa = {b2}')