#Metodo Punto Fijo

import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import Symbol , root ,pprint

x = Symbol("x")

expr=0
Cons = 0

G = int(input("INGRESE EL GRADO DE POLINOMIO:     "))
for i in range(0,G+1,1):
    
    
    if i == G:
        
        Cons= float(input("INGRESE EL VALOR DE LA CONSTANTE:     "))
        expr = expr + Cons
    else:     
        print("INGRESE EL COEFICIENTE DE LA VARIBLE CON POTENCIA ...",G-i)
        COF = float(input())
        expr = COF*x**(G-i) + expr
        if i==0:
            c3 = COF
            C3 = COF*x**G  
        
print("EL POLINOMIO INGRESADO FUE: ...",expr)


Xo = float(input("Ingrese el valor del punto inicial:   "))
error = float(input("Ingrese el criterio de convergencia:    "))
E=100
X1 = [Xo]
i=0


exprsim = -(expr - C3)
print("g(x) = ")
pprint(root(exprsim , G)/c3)

exprsim = (exprsim/c3)**(1/G)

X=np.linspace(Xo,Xo+10,100)
Y=[]

for k in X:
    y = expr.subs(x,k)
    Y.append(y)

x1=np.linspace(Xo,Xo+10,100)
y1=np.zeros(len(x1))



while (E > error):
    
    h = X1[i]
    
    y = exprsim.subs(x,h) 
    
    
    
    
    X1.append(y)
        
        
    E = abs((X1[i+1]-X1[i])/X1[i+1])*100
    print("ERROR ACTUAL DE:   ",E,"%")
    i=i+1

    plt.plot(X,Y,color="red")
    plt.plot(h,0,"o",color="blue")
    plt.plot(x1,y1,color="black")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    T=["f(x)","(xi , f(xi))"]
    plt.legend(T)
    plt.title("METODO DE PUNTO FIJO")
    plt.show()



print("LA RAIZ APROXIMADA ES:   ",h) 