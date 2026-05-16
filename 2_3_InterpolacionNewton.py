#Interpolacion de Newton

import sympy 
from sympy import Symbol , expand 
import matplotlib.pyplot as plt
import numpy as np

x = Symbol("x")



XY ={}

N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee, (como máximo ingrese 10):     "))

if N > 10:
    print("Excedio el limite de datos para ingresar")
    quit()
    

for i in range(0,N,1):
    print("Para el indice ",i+1,":")
    
    xi = float(input("Ingrese el valor de x: "))
    
    yi = float(input("Ingrese el valor de y: "))
    
    XY [xi]=yi
    
    
        
XY_ord = dict(sorted(XY.items()))

a=[[] for j in range(N)]

X = list (XY_ord.keys())

a[0] = list (XY_ord.values())

tabla1 = np.vstack((X,a[0]))
Tabla1 = np.transpose(tabla1)

print ("La tabla de los datos ingresados fue:  ")
print (Tabla1)



for j in range (0,N,1):
    
    b = 0
    
    for i in range(1,N-j,1):
        
        elem = ((a[j][i] - a[j][i-1])/(X[i+j] - X[b]))
        a[j+1].append(elem)
        b=b+1
    
A=[]    
    
for k in range(0,N,1):
    A.append(a[k][0])


expr = 0
for q in range(0,N,1):
    if q==0:
        expr = expr + A[q]
    elif q==1:
        expr = expr + A[q]*(x-X[q-1])
    elif q==2:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])
    elif q==3:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])
    elif q==4:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])
    elif q==5:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])
    elif q==6:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])*(x-X[q-6])
    elif q==7:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])*(x-X[q-6])*(x-X[q-7])
    elif q==8:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])*(x-X[q-6])*(x-X[q-7])*(x-X[q-8])
    elif q==9:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])*(x-X[q-6])*(x-X[q-7])*(x-X[q-8])*(x-X[q-9])
    elif q==10:
        expr = expr + A[q]*(x-X[q-1])*(x-X[q-2])*(x-X[q-3])*(x-X[q-4])*(x-X[q-5])*(x-X[q-6])*(x-X[q-7])*(x-X[q-8])*(x-X[q-9])*(x-X[q-10])

Y1=[]

Expr = expand(expr)
print("La ecuación generada por el Método fue:   ",Expr)


c=len(a[0])

for m in range(0,len(a[0]),1):
    
    if m==1:
        for g in range(1,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((a[0],a[1]))
            
    elif m==2:    
        for g in range(2,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[2]))
    
    elif m==3:
        for g in range(3,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[3]))
    
    elif m==4:
        for g in range(4,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[4]))
    
    elif m==5:
        for g in range(5,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[5]))
    
    elif m==6:
        for g in range(6,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[6]))
    
    elif m==7:
        for g in range(7,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[7]))
    
    elif m==8:
        for g in range(8,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[8]))
    
    elif m==9:
        for g in range(9,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[9]))
    
    elif m==10:
        for g in range(10,len(a[0]) ,1):
            a[g].insert(0,"///")
        tabla = np.vstack((tabla,a[10]))
    
Tabla = np.transpose(tabla)

print("La tabla de los datos obtenidos fue:   ")
print(Tabla) 

    
X1 = np.linspace(X[0],X[N-1],100)

for h in X1:
    y = Expr.subs(x,h)
    Y1.append(y)

plt.plot(X1,Y1,color="black")

for w in range(0,N,1):
    plt.plot(X[w],a[0][w],"o",color="blue")


T=["f(x)","Datos"]
plt.legend(T)
plt.grid()
plt.show()