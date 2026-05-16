# INTERPOLACION LINEAL

import matplotlib.pyplot as plt
import numpy as np

i=0

XY = {}

N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee:     "))

for i in range(0,N,1):
    print("Para el indice ",i+1,":")
    
    xi = float(input("Ingrese el valor de x: "))
    
    yi = float(input("Ingrese el valor de y: "))
    
    XY [xi]=yi
    
x = float(input("Ingrese el valor de x para aproximar su respectivo valor de f(x):      "))

f=0

XY_ord = dict(sorted(XY.items()))

X = list (XY_ord.keys())
Y = list (XY_ord.values())

tabla = np.vstack((X,Y))
Tabla = np.transpose(tabla)

print ("La tabla de los datos ingresados fue:  ")
print (Tabla)

for l in range (0,N,1):
    if x < X[l] and f == 0:
        may = l
        f=1
        men = l-1


print("La formula para la interpolación lineal es:    ")
print("y = Yi + ((Yi+1)-Y(i)/(Xi+1)-(Xi) * (x-Xi)")

y = Y[men] + ( (Y[may] - Y[men] )/ (X[may] - X[men]) )*(x - X[men])





plt.plot(X,Y,color="black")
plt.plot(x,y,"o",color="blue")
for k in range(0,N,1):
    plt.plot(X[k],Y[k],"o",color="red")


T=["FUNCION","INTERPOLACION LINEAL","DATOS"]
plt.legend(T)

plt.title("INTERPOLACION LIEAL")
plt.grid()
plt.show()