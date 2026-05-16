#INTERPOLACION DE LAGRANGE

import numpy as np
import matplotlib.pyplot as plt
import sympy 
from sympy import Symbol
from sympy import simplify
from sympy import expand


X = [-2.6,-1.4,1.2,2.4]
Y = [-157.612,-16.828,30.336,206.688]
L=[]

Y1 = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []


x = Symbol("x")






for k in range(0,4,1):

    num = 1
    den = 1    

    for i in range(0,4,1):
        
        if i==k :
            q=1
        else : 
            num = (x-X[i])*num
            den = (X[k] - X[i])*den
        
        
    S = expand(num)
    Q = S/den
    
    L.append(Q)
    
    
P0 = Y[0]*simplify(L[0]) 
P1 = Y[1]*simplify(L[1])
P2 = Y[2]*simplify(L[2])
P3 = Y[3]*simplify(L[3])


print("El primer polinomio obtenido fue: ")
print (P0)

X1 = np.linspace(-2.6,2.4,100)

for h in X1:
    y = P0.subs(x,h)
    Y1.append (y)



plt.plot(X1,Y1,"--",color="purple")

print("El segundo polinomio obtenido fue: ")
print (P1)

X2 = np.linspace(-2.6,2.4,100)

for h in X2:
    y = P1.subs(x,h)
    Y2.append (y)



plt.plot(X2,Y2,"--",color="orange")


print("El tercer polinomio obtenido fue: ")
print (P2)

X3 = np.linspace(-2.6,2.4,100)

for h in X3:
    y = P2.subs(x,h)
    Y3.append (y)



plt.plot(X3,Y3,"--",color="green")


print("El cuarto polinomio obtenido fue: ")
print (P3)

X4 = np.linspace(-2.6,2.4,100)

for h in X4:
    y = P3.subs(x,h)
    Y4.append (y)



plt.plot(X4,Y4,"--",color="blue")


PF = P0 + P1 + P2 + P3


print("El polinomio final fue:  ")
print(PF)

X5 = np.linspace(-2.6,2.4,100)

for h in X5:
    y = PF.subs(x,h)
    Y5.append(y)

plt.plot(X5,Y5,color="black")


plt.plot(X[0],Y[0],"o",color="red")
plt.plot(X[1],Y[1],"o",color="red")
plt.plot(X[2],Y[2],"o",color="red")
plt.plot(X[3],Y[3],"o",color="red")

T = ["POLINOMIO 1","POLINOMIO 2","POLINOMIO 3", "POLINOMIO 4","POLINOMIO FINAL","DATOS"]


plt.legend(T)
plt.grid()
plt.show()