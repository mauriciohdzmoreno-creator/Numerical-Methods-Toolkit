#METODO GRAFICO PARA ENCONTRAR RAICES DE UNA ECUACION
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from sympy import Symbol


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
D=1


while D ==1:

    a=float(input("INGRESE EL VALOR DEL LIMITE INFERIOR:     "))
    b=float(input("INGRESE EL VALOR DEL LIMITE SUPERIOR:     "))


    x1 = np.linspace(a,b,100)
    Y1 = []


    for h in x1:
    
        y = expr.subs(x,h)
        Y1.append(y)

    Y=np.zeros(len(x1))
    
    fa = expr.subs(x,a)
    fb = expr.subs(x,b)
    
    plt.plot(x1,Y1,color="black")
    plt.plot(a,fa,"o",color="blue")
    plt.plot(b,fb,"o",color="green")
    plt.plot(x1,Y,"--",color="red")
    plt.grid()
    T=["f(x)","(a,fa)","(b,fb)"]
    plt.legend(T)
    plt.title("METODO GRAFICO")
    plt.show() 

    D=int(input("¿DESEA HACER UNA ITERACION MAS?, 1 para Si y 0 para No:       "))
    
    
#ACABO EL PROGRAMA :) 