import numpy as np
import matplotlib.pyplot as plt
from Graficador import *

class Bezier:
    '''
    Recibe como parámetro una lista de los puntos de control.
    PRE: pueden ser 3 puntos o 4
    '''
    def __init__(self, puntos_de_control: list[list[int]]):
        self.puntos_de_control = np.array(puntos_de_control)
        self.grado = len(puntos_de_control)-1

    def punto_en_t(self, t):
        pc = self.puntos_de_control
        if(self.grado == 3):
            return ((1-t)**3) * pc[0] + 3*((1-t)**2)*t*pc[1] + 3* (1-t) * (t**2)*pc[2] + (t**3)*pc[3]
        elif(self.grado == 2):
            return ((1-t)**2) * pc[0] + 2*(1-t)*t*pc[1] + (t**2)*pc[2]
        
    def longitud(self):
        t = np.linspace(0, 1, 100)
        pts = np.array([self.punto_en_t(ti) for ti in t])
        diffs = np.diff(pts, axis=0)
        return np.sum(np.sqrt((diffs**2).sum(axis=1)))
        
    def graficar(self, show_plot=True, poligonal=True, curve_color="blue", pc_color="darkviolet", figsize=(0,0)):
        '''
        Graficar la curva de Bezier.
        - show_plot: si mostrar el gráfico con matplot (al ponerlo en False, se pueden graficar varias curvas en un mismo gráfico)
        - poligonal: si mostrar la poligonal de control
        - curve_color: el color de la curva
        - pc_color: el color de los puntos de control
        '''
        lista_de_t =  np.arange(0, 1.01, 0.01)
        puntos = [] # lista de array([float, float])

        for i in range(101):
            puntos.append(self.punto_en_t(lista_de_t[i]))

        data = np.array(puntos)
        x = data[:, 0]
        y = data[:, 1]

        plt.plot(x, y, color=curve_color, label='Bézier')  # Curva
        if(poligonal):
            plt.plot(self.puntos_de_control[:, 0], self.puntos_de_control[:, 1], marker='o' ,linestyle='--',color=pc_color, label='Puntos de control')
        else:
            plt.scatter(self.puntos_de_control[:, 0], self.puntos_de_control[:, 1], marker='o' ,color=pc_color, label='Puntos de control')

        for i, punto in enumerate(self.puntos_de_control):
            plt.text(punto[0] + 0.1, punto[1] + 0.1, f'P{i}', fontsize=10, color=pc_color)

        if(figsize != (0,0)):
            min_x = np.min(self.puntos_de_control[:, 0])
            min_y = np.min(self.puntos_de_control[:, 1])
            max_x = np.max(self.puntos_de_control[:, 0])
            max_y = np.max(self.puntos_de_control[:, 1])

            plt.xlim(min_x - 1, max_x + 1)
            plt.ylim(min_y - 1, max_y + 1)
        else:
            plt.figure(figsize=figsize)

        plt.plot(x, y, color='black', alpha=0.3)
        if(show_plot):
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.show()

    def graficar_con_obstaculos(self):
        fig, ax = plt.subplots(figsize=(15,9)) 
        ax = configurar_mapa(ax)
        ax, obstaculos = configurar_obstaculos(ax)

        self.graficar(show_plot=False, poligonal=False, figsize=(15,9), curve_color='darkviolet', pc_color='darkviolet')

        plt.show()
    