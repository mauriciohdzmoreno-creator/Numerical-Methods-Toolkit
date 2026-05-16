#INTERPOLACION CUADRATICA

import numpy as np
import matplotlib.pyplot as plt
import sympy 
from sympy import symbols ,Eq ,solve ,linsolve


A1,B1,C1,X = symbols("A B C X")


XY = {}


Y2 =[]


N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee:     "))

for i in range(0,N,1):
    print("Para el indice ",i+1,":")
    
    xi = float(input("Ingrese el valor de x: "))
    
    yi = float(input("Ingrese el valor de y: "))
    
    XY [xi]=yi
    
x = float(input("Ingrese el valor de x para aproximar su respectivo valor de f(x):      "))

f=0

XY_ord = dict(sorted(XY.items()))

X1 = list (XY_ord.keys())
Y = list (XY_ord.values())

xmin = min(X1)
xmax = max(X1)

X2 = np.linspace(xmin,xmax,100)



for l in range (0,N,1):
    if x < X1[l] and f == 0:
        may = l
        f=1
        men = l-1
        
if may == N-1:
    p3 = may-2
else: 
    p3 = may+1
    
tabla = np.vstack((X1,Y))
Tabla = np.transpose(tabla)

print("La tabla de los datos Ingresados fue:   ")
print(Tabla)


#Sistemas de ecuaciones de tipo (A + B + C)= D
#Ec1 = (A + B*X1[may] + C*X1[may]**2 )
#Ec2 = (A + B*X1[men] + C*X1[men]**2 )
#Ec3 = (A + B*X1[p3] + C*X1[p3]**2 )

A = [ [1 , X1[may] , X1[may]**2],
      [1 , X1[men] , X1[men]**2],
      [1 , X1[p3] , X1[p3]**2] ]


a= A [0][0]
b= A [0][1]
c= A [0][2]
d= A [1][0]
e= A [1][1]
f= A [1][2]
g= A [2][0]
h= A [2][1]
i= A [2][2]


B = [Y[may],Y[men],Y[p3] ]


detM = a*((e*i) - (f*h)) - b*((d*i)-(f*g)) + c*((d*h) - (e*g))
det = 1/detM


if detM == 0:
    print("El sistema de ecuaciones no tiene solucion unica")
    quit()

print("El sistema de ecuaciones creado fue:   ")
print(A[0][0]*A1 + A[0][1]*B1 + A[0][2]*C1 ," = ",Y[may] )
print(A[1][0]*A1 + A[1][1]*B1 + A[1][2]*C1 ," = ",Y[men] )
print(A[2][0]*A1 + A[2][1]*B1 + A[2][2]*C1 ," = ",Y[p3] )






M_inv = [ [ det*((e*i) - (f*h)) , det*(-((b*i) - (c*h))) , det*((b*f) - (c*e))],
          [ det*(-((d*i) - (f*g))) , det*((a*i) - (c*g)) , det*(-((a*f) - (c*d)))],
          [ det*((d*h) - (e*g)) , det*(-((a*h) - (b*g))) , det*((a*e) - (b*d))]
        ]

a = M_inv[0][0]*B[0] + M_inv[0][1]*B[1] + M_inv[0][2]*B[2]
b = M_inv[1][0]*B[0] + M_inv[1][1]*B[1] + M_inv[1][2]*B[2]
c = M_inv[2][0]*B[0] + M_inv[2][1]*B[1] + M_inv[2][2]*B[2]

print("La solución al sistema de ecuaciones creado es:   ")
print("a = ",a)
print("b = ",b)
print("c = ",c)



#Sol = solve((Ec1,Ec2,Ec3),(A,B,C))

y = a + b*x + c*x**2

y1 = a + b*X + c*X**2
print("La ecuacion encontrada fue:   ")
print(y1)

for k in X2:
    y2 = y1.subs(X,k)
    Y2.append(y2)


plt.plot(X2,Y2,color="black")
plt.plot(x,y,"o",color="blue")
for d in range(0,len(X1),1):
    plt.plot(X1[d],Y[d],"o",color="red")


T=["FUNCION","INTERPOLACION LINEAL","Datos"]
plt.legend(T)

plt.title("INTERPOLACION LIEAL")
plt.grid()
plt.show()