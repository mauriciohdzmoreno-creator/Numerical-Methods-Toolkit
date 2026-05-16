# METODO DE BISECCION


import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy import Symbol

E=100 
i=0



#PREGUNTAR POOR EL RANGO
a=float(input("Ingrese el valor de a (limite inferior):    "))
b=float(input("Ingrese el valor de b (limite superior):    "))
#preguntar por el grado de error
error = float(input("Ingrese el valor de convergencia (en porcentaje):    "))


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



while (E > error):
    
    Y=[]

#calcular el punto medio
    m= (a+b)/2
    print("Punto medio = ",m )
#contador para saber el numero de la iteracion actual    
    i=i+1
    
#evaluo la funcion en a,b,m 
    print("Valor de a = ",a)
    print("Valor de b = ",b)
    
    fa = expr.subs(x,a)
    fb = expr.subs(x,b)
    fm = expr.subs(x,m)
#calcular el error    
    E=abs((a-b)/a)*100
    
    X = np.linspace(a,b,100)    
    
    for h in X:
        y = expr.subs(x,h)
        Y.append(y)
        
        
    plt.plot(a,fa,"o",color="blue")
    plt.plot(b,fb,"o",color="black")
    plt.plot(m,fm,"o",color="green")
    plt.plot(X,Y,color="red")
    T=["(a,fa)","(b,fb)","(m,fm)","f(x)"]
    plt.legend(T)
    plt.grid()
    plt.title("METODO DE BISECCION ")
    plt.show()
    
    if fa > 0 and fm < 0:
        a=a 
        b=m
    elif fm > 0 and fb <0:
        b=b
        a=m
    elif fb > 0 and fm < 0:
        a=m
        b=b    
    elif fb == fm:
        b=m
        a=a
    elif fm > 0 and fa <0:    
        b=m
        a=a
    
        
        
        
    print("Funcion F(a)=  ",fa)
    print("Funcion F(b) =  ",fb)
    print("Funcion F(m) =   ",fm)
    
    print("ERROR ACTUAL",E,"%")
    
print("La Raiz es aproximadamente = ",m)
#programa terminado :)    