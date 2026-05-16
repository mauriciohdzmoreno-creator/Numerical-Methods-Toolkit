# INTERPOLACION DE NEWTON

#IMPORTAR LIBRERIAS 
import sympy 
from sympy import Symbol
from sympy import simplify




import matplotlib.pyplot as plt
import numpy as np


#CREAR LISTAS DE LOS DATOS DADOS
X = [-4,-3,-2,0,1.2,3,3.4]
a0 = [-69,153,79,3,-5.55168,-111,-75.08576]

Y2 = []

#CREAR LISTAS PARA LAS PROXIMAS ITERACIONES A OBTENER
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []


#PARA RELLENAR a1
for i in 1,2,3,4,5,6: 
    elem = ((a0[i] - a0[i-1])/(X[i] - X[i-1]))
    a1.append(elem)
    
#PARA RELLENAR a2    
for i in 1,2,3,4,5:
    elem = (a1[i]-a1[i-1])/(X[i+1]-X[i-1])
    a2.append(elem)

#PARA RELLENAR a3       
for i in 1,2,3,4:
    elem = (a2[i]-a2[i-1])/(X[i+2] - X[i-1])
    a3.append(elem)

#PARA RELLENAR a4   
for i in 1,2,3:
    elem = (a3[i] - a3[i-1])/(X[i+3]-X[i-1])
    a4.append(elem)

#PARA RELLENAR a5   
for i in 1,2:
    elem = (a4[i] - a4[i-1])/(X[i+4] - X[i-1])
    a5.append(elem)

#PARA RELLENAR a6   
i=1
elem = (a5[i] - a5[i-1])/(X[i+5] - X[i-1])
a6.append(elem)


#LISTA DE LOS PRIMEROS ELEMENTOS DE CADA Ai
A = [a0[0],a1[0],a2[0],a3[0],a4[0],a5[0],a6[0]]

#CREAR SIMBOLO DE PARA X
x = Symbol("x")

#RESOLVER LA ECUACION CON FORMA DE: a0 + a1(x-x0) + a2(x-x0)(x-x1) + ... + an(x-x0)(x-x0)...(x-xn)
Y = A[0] + A[1]*(x-X[0]) + A[2]*(x-X[0])*(x-X[1]) + A[3]*(x-X[0])*(x-X[1])*(x-X[2]) + A[4]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3]) + A[5]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4]) + A[6]*(x-X[0])*(x-X[1])*(x-X[2])*(x-X[3])*(x-X[4])*(x-X[5])

#LE PIDO A SYMPY QUE SIMPLIFIQUE LA EXPRESION ANTERIOR
z= simplify(Y)

#CREO UNA LISTA PARA EVALUAR LA FUNCION Y GRAFICAR LA FUNCION
X2 = np.linspace(-4,4,100)

#EVALUAR LA FUNCION OBTENIDA 
for h in X2:
    y = z.subs(x,h)
    Y2.append(y)

#IMPRIMIR LA ECUACION DADA

print("La ecuacion obtenida fue: ")
print(z)


#CREO LISTAS PARA LA TABLA DE LAS ITERACIONES ECHAS
A0 = a0
A1 = [" /// ",222.0,-74.0,-38.0,-7.126400000000001,-58.58239999999999,89.78560000000003]
A2 = [" /// "," /// ",-148.0,12.0,9.648,-17.151999999999997,67.44000000000001]
A3 = [" /// "," /// "," /// ",40.0,-0.56,-5.359999999999999,24.880000000000006]
A4 = [" /// "," /// "," /// "," /// ",-7.8,-0.7999999999999998,5.6000000000000005]
A5 = [" /// "," /// "," /// "," /// "," /// ",1,1]
A6 = [" /// "," /// "," /// "," /// "," /// "," /// ",0]


# AGRUPO LAS TABLAS VERTICALMENTE
tabla = np.vstack((A0,A1,A2,A3,A4,A5,A6) )

#OBTENGO LA MATRIZ TRANSPUESTA
TABLA = np.transpose(tabla)

#IMPRIMIR LA TABLA
print("La tabla de todas las iteraciones fue:  ")
print(TABLA)

#GRAFICAR LA FUNCION OBTENIDA
plt.plot(X2,Y2,color="black")
plt.plot (X[0],a0[0],"o",color="red")
plt.plot (X[1],a0[1],"o",color="blue")
plt.plot (X[2],a0[2],"o",color="black")
plt.plot (X[3],a0[3],"o",color="green")
plt.plot (X[4],a0[4],"o",color="purple")
plt.plot (X[5],a0[5],"o",color="brown")
plt.plot (X[6],a0[6],"o",color="orange")

T = ["f(x)","(-4,-69)","(-3,153)","(-2,79)","(0,3)","(1.2,-5.55168)","(3,-111)","(3.4,-75.08576)"]

plt.title("INTERPOLACION DE NEWTON")
plt.legend(T)
plt.grid()
plt.show()