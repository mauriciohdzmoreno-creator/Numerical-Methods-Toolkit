#Minimos Cuadrados (Lineal)


import matplotlib.pyplot as plt
import numpy as np
import sympy 
from sympy import Symbol


x=Symbol ("x")
y=Symbol ("y")

N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee:     "))

XY={}



for i in range(0,N,1):
    print("Para el indice ",i+1,":")
    
    xi = float(input("Ingrese el valor de x: "))
    
    yi = float(input("Ingrese el valor de y: "))
    
    XY [xi]=yi
    
    
        
XY_ord = dict(sorted(XY.items()))

X = list (XY_ord.keys())
Y = list (XY_ord.values())

tabla = np.vstack((X,Y))
Tabla = np.transpose(tabla)

print ("La tabla de los datos ingresados fue:  ")
print (Tabla)

xmin = min(X)
xmax = max(X)



Sxi1 = sum (X)

Sxi2 = 0
for i in X:
    Sxi2 = Sxi2 + i**2


Syi = sum(Y)

Syixi =0
for k in range(0,len(X),1):
    Syixi = Syixi + (X[k]*Y[k])
    
    
A = [ [Sxi1 , N],
      [Sxi2 , Sxi1]
     ]

B = [ Syi , Syixi ]


a=A[0][0]
b=A[0][1]
c=A[1][0]
d=A[1][1]

print("El sistema de ecuaciones creado por el método fue:    ")
print(a*x + b*y , "=" , B[0])
print(c*x + d*y , "=" , B[1])


DetA = (a*d) - (b*c)

if DetA == 0:
    print("El sistema de ecuaciones no tiene solucion unica   ")
    quit()

detA = 1/DetA

A_inv = [ [ detA*d  , -(detA*b) ],
          [ -(detA*c) , detA*a  ]   
        ]


a = A_inv[0][0]*B[0] + A_inv[0][1]*B[1]
b = A_inv[1][0]*B[0] + A_inv[1][1]*B[1]

recta = a*x + b

print("La solucion encontrada fue:   ")
print("a = ",a)
print("b = ",b)

print("La ecuacion de la recta encontrada con menor grado de error fue:   ")
print(y , "=" , recta)

X1 = np.linspace(xmin,xmax,100)

Y1 = []

for h in X1:
    y1 = recta.subs(x,h)
    Y1.append(y1)




plt.plot(X1,Y1,color="black")
for g in range(0,N,1):
    plt.plot(X[g],Y[g],"o",color="red")


T = ["Recta Obtenida","Datos"]
plt.legend(T)
plt.grid()
plt.show()


