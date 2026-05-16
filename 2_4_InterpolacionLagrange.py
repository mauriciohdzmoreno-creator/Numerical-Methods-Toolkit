#Interpolacion de Lagrange

import numpy as np
import sympy 
from sympy import Symbol,expand
import matplotlib.pyplot as plt


x = Symbol("x")



L=[]

XY={}




N = int(input("Ingrese el numero de datos (de tipo (x,y)) tabulados que posee:     "))


P = [[] for i in range(N)]
    

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

for k in range(0,N,1):

    num = 1
    den = 1    

    for i in range(0,N,1):
        
        if i==k :
            q=1
        else : 
            num = (x-X[i])*num
            den = (X[k] - X[i])*den
        
        
    S = expand(num)
    Q = S/den
    
    L.append(Q)

    
print("Los polinomios encontrados fueron:    ")
for g in range(0,N,1):
    P[g].append (Y[g]*L[g])
    print(Y[g]*(P[g][0]))

Y1 = [[] for i in range(N)]

xmin = min(X)
xmax = max(X)

X1 = np.linspace(xmin,xmax,100)

Pf=0

for k in range(0,N,1):
    for q in X1:
        y = P[k][0].subs(x,q)
        Y1[k].append(y) 
    Pf = Pf + P[k][0]


print("El polinomio final fue:    ")    
print(Pf)    

YF = []

for f in X1:
    y = Pf.subs(x,f)
    YF.append(y)


plt.plot(X1,YF,color="black")
for w in range(0,N,1):
    if w==0:
        c = "blue"
        plt.plot (X1,Y1[w],"--",color=c)
    elif w==1:
        c = "green"
        plt.plot (X1,Y1[w],"--",color=c)
    elif w==2:
        c = "purple"
        plt.plot (X1,Y1[w],"--",color=c)
    elif w==3:
        c = "brown"
        plt.plot (X1,Y1[w],"--",color=c)
    elif w==4:
        c = "yellow"
        plt.plot (X1,Y1[w],"--",color=c)
    elif w==5:
        c = "pink"
        plt.plot (X1,Y1[w],"--",color=c)
    else:
        c = "red"
        plt.plot (X1,Y1[w],"--",color=c)


    plt.plot(X[w],Y[w],"o",color="red")


T=["Polinomio Final","Polinomios","Datos"]
plt.legend(T)
plt.grid()
plt.show()