# Minimos Cuadrados (Cuadratica)

import matplotlib.pyplot as plt
import numpy as np
import sympy 
from sympy import Symbol


x=Symbol ("x")
y=Symbol ("y")

N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee, (como máximo ingrese 10):     "))

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

Sxi1 = sum(X)

Sxi2 = 0
for i in X:
    Sxi2 = Sxi2 + i**2

Sxi3 = 0
for i in X:
    Sxi3 = Sxi3 + i**3

Sxi4 = 0
for i in X:
    Sxi4 = Sxi4 + i**4

Syi = sum(Y)

Syixi1 =0
for k in range(0,len(X),1):
    Syixi1 = Syixi1 + (X[k]*Y[k])

Syixi2 =0
for k in range(0,len(X),1):
    Syixi2 = Syixi2 + ((X[k]**2)*Y[k])

A= [ [Sxi2 , Sxi1 , N],
     [Sxi3 , Sxi2 , Sxi1],
     [Sxi4 , Sxi3 , Sxi2]
   ]


B=[Syi , Syixi1 , Syixi2]

print("El sistema de ecuaciones a resolver es:   ")

print(A[0][0]*x**2 + A[0][1]*x + A[0][2] , " = " , B[0])
print(A[1][0]*x**2 + A[1][1]*x + A[2][2] , " = " , B[1])
print(A[2][0]*x**2 + A[2][1]*x + A[2][2] , " = " , B[2])



a=A[0][0]
b=A[0][1]
c=A[0][2]
d=A[1][0]
e=A[1][1]
f=A[1][2]
g=A[2][0]
h=A[2][1]
i=A[2][2]


DetA = a*((e*i) - (f*h)) - b*((d*i) - (f*g)) +c*((d*h) - (e*g))
if DetA == 0:
    print("El sistema de ecuaciones no tiene solucion unica ...  ")
    quit()


detA = 1/DetA


A_inv = [ [detA*((e*i) - (f*h)) , -detA*((b*i) - (c*h)) , detA*((b*f) - (c*e))],
          [-detA*((d*i) - (f*g)) , detA*((a*i) - (c*g)) , -detA*((a*f) - (c*d))],
          [detA*((d*h) - (e*g)) , -detA*((a*h) - (b*g)) , detA*((a*e) - (b*d))]
        ]

a = A_inv[0][0]*B[0] + A_inv[0][1]*B[1] + A_inv[0][2]*B[2]
b = A_inv[1][0]*B[0] + A_inv[1][1]*B[1] + A_inv[1][2]*B[2]
c = A_inv[2][0]*B[0] + A_inv[2][1]*B[1] + A_inv[2][2]*B[2]

print("La solucion obtenida fue....")
print("a = ",a)
print("b = ",b)
print("c = ",c)



recta = a*x**2 + b*x + c

print("La ecuacion de la recta es:  ")
print(y ,"=",recta)


X1 = np.linspace(xmin,xmax,100)
Y1=[]

for k in X1:
    y1 = recta.subs(x,k)
    Y1.append(y1)


plt.plot(X1,Y1,color="black")
for q in range(0,len(X),1):
    plt.plot(X[q],Y[q],"o",color="red")

T=["Curva Obtenida","Datos"]

plt.legend(T)
plt.grid()
plt.show()