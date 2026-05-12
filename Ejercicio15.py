from Bezier import Bezier

# Pasa por abajo
# pc = [[0,0], [8.5,0], [10,1],[10,5]]

# Pasa por el medio
pc = [[0,0], [9,0], [1.8,5.3],[10,5]]

curva = Bezier(pc)

curva.graficar_con_obstaculos()

print(curva.longitud())