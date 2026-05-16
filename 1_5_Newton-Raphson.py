#METODO NEWTON - RAPHSON
import numpy as np
import matplotlib.pyplot as plt
import sympy 
from sympy import Symbol


x = Symbol("x")

Y=[]
Y2=[]


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



Xo = float(input("Ingrese el valor del punto inicial:     "))
error = float(input("Ingrese el criterio de convergencia (en porcentaje) "))
E=100
X1 = [Xo]
i=0

X=np.linspace(-10,10,100)

x2= X
y21 = np.zeros(len(x2))

y3=np.linspace(-100,100,100)
x3=np.zeros(len(y3))


#Y= X**3 - 3*X**2 + 1
#Y2= 3*X**2 -6*X

y = expr
for h in X:
    yy = y.subs(x,h)
    Y.append(yy)

y2 = sympy.diff(expr,x)
for k in X:
    yy2 = y2.subs(x,k)
    Y2.append(yy2)




while (E > error):
    
    Y4=[]
    
    
    q = float(X1[i])
    
    
    z1 = y.subs(x,q)
    z2 = y2.subs(x,q)
    
    
    x1 =  X1[i] - (z1/z2)
    A = y.subs(x,X1[i])
    
    
    
    m = y2.subs(x,X1[i])
    
    
    y4 = m*(x-X1[i]) + z1
    
    for j in X:
        yy4 = y4.subs(x,j)
        Y4.append(yy4)
    
    
    y1= np.zeros(len(X1))
    
    X1.append(x1)
        
    if i >= 1:
        E = abs((X1[i]-X1[i-1])/X1[i])*100
        print("ERROR ACTUAL DE:   ",E,"%")
    
    
    
    plt.plot(X,Y,color="red")
    plt.plot(X,Y4 ,"--",color="green")
    plt.plot(X1[i],A,"o",color="blue")
    plt.plot(x1,y1[i],"o",color="blue")
    plt.plot(x2,y21,color="black")
    plt.plot(x3,y3,color="black")
    
    T=[" f(x) "," f'(x) "," f(Xi) "," RAIZ "]
    plt.legend(T)
    
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("METODO DE NEWTON-RAPHSON")
    plt.show()
    
    i=i+1


print("LA RAIZ APROXIMADA ES:   ",x1) 