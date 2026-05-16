#METODO DE LA SECANTE
import numpy as np
import matplotlib.pyplot as plt
import sympy 
from sympy import Symbol


Y=[]
Y2=[]

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
    
print("EL POLINOMIO INGRESADO FUE: ...",expr)

Xo = float(input("Ingrese el valor del primer valor inicial:     "))
Xi = float(input("Ingrese el valor del segundo valor inicial:     "))
error = float(input("Ingrese el valor del criterio de convergencia:     "))

E=100
X1 = [Xo,Xi]
i=0

X=np.linspace(Xo,Xo+10,100)

X2=np.linspace(Xo,Xo+10,100)

x2= X
yy2 = np.zeros(len(x2))




y=expr
for h in X:

    y1 = expr.subs(x,h)
    Y.append(y1)



y2=sympy.diff(y,x)
for k in X:

    y2 = expr.subs(x,h)
    Y2.append(y2)


#Y= X**3 - 3*X**2 + 1
#Y2=3*X**2 - 6*X


X4=np.zeros(len(X2))
Y4=X2




h=0.1

i=0

while (E > error):
    
    Y5=[]
    
    z1 = (X1[i+1]-X1[i])*(y.subs(x,X1[i+1]))
    z2 = (y.subs(x,X1[i+1]))-(y.subs(x,X1[i]))
    
    
    x1 =  X1[i+1] - (z1/z2)
    X1.append(x1)
    
    
    
    
    
    E = abs((X1[i]-X1[i-1])/X1[i])*100
    print("ERROR ACTUAL DE:   ",E,"%")
    
    z = X1[i]+h
    m = ( y.subs(x,z) - y.subs(x,X1[i]) / h)

    
    y5 = m*(x-X1[i]) + y.subs(x,X1[i])
    
    for p in X:
        
        yy5=y5.subs(x,p)
        Y5.append(yy5)
    
    
    
    plt.plot(X,Y,color="red")
    plt.plot(X,Y5,"--",color="green")
    plt.plot(x1,0,"o",color="blue")
    plt.plot(X4,Y4,color="black")
    plt.plot(x2,yy2,color="black")
    T=["f(x)","Secante","Iteración de X"]
    plt.legend(T)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("METODO DE LA SECANTE")
    plt.show()
    
    i=i+1


print("LA RAIZ APROXIMADA ES:   ",x1) 