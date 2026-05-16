#METODO DE FALSA POSICION 
#OTENER UN RANGO EN DONDE HAYA UNA RAIZ DE LA ECUACION (A,B)
#EVALUAR LA FUNCIOON EN f(a) y f(b).
#OBTENER Xi; Xi = a*f(b) - b*f(a) / f(a)-f(b)
#ingresar un valor del error para iterar n veces hasta tener un resultado satisfactorio
#error = Val_abs(Xi - Xi-1)


import matplotlib.pyplot as plt
import numpy as np
import sympy 
from sympy import Symbol


a=float(input("INGRESE EL VALOR DEL LIMITE INFERIOR:   "))
b=float(input("INGRESE EL VALOR DEL LIMITE SUPERIOR:   "))
error = float(input("Ingrese el valor de el criterio de convergencia (en porcentaje):   "))
E=100

Q=0

X1=[]


x = Symbol("x",real=True)

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


i=1

while(E > error):
    print("                                        ITERACION NUMERO",i)
    
    X = np.linspace(a,b,100)
    Y = []
    for h in X:
        y = expr.subs(x,h)
        Y.append(y)
    
    A = expr.subs(x,a)
    B = expr.subs(x,b)
    
    fa = float(A)
    fb = float(B)
    
    print("VALOR DE a:   ",a)
    print("FUNCION F(a):   ",fa)
    print("VALOR DE b:   ",b)
    print("FUNCION F(b):   ",fb)

    x1 = ((a * fb) - (b * fa)) / (fb - fa)
    
    X1.append(x1)
    
    C = expr.subs(x,x1)
    Fx = float(C)
    
    print("VALOR DE x:   ",x1)
    print("FUNCION f(x):   ",Fx)
    
    
    if i >= 2:
        
        E = abs(X1[i-1]-X1[i-2]) * 100
        print("ERROR ACTUAL :   ",E,"%")
        
    if fa > 0 and Fx < 0:
        a=a 
        b=x1
    elif Fx > 0 and fa <0:    
        b=x1
        a=a
    elif Fx > 0 and fb <0:
        a=x1
        b=b
    elif fb > 0 and Fx < 0:
        a=x1
        b=b    
    elif fb == Fx:
        b=x1
        a=a
    
        
    i=i+1 
    
    plt.plot(a,fa,"o",color="blue")
    plt.plot(b,fb,"o",color="black")
    plt.plot(x1,Fx,"o",color="green")
    plt.plot(X,Y,color="black")
    T=["(a,fa)","(b,fb)","(x,fx)","F(x)"]
    plt.legend(T)
    plt.grid()
    plt.title("METODO DE LA FALSA POSICION ")
    plt.show()

    
    if Q==1:
        break



if Q==1:
    W=1
else:        
    print("LA RAIZ ES APROXIMADAMENTE:   ",x1)