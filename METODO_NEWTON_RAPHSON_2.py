#METODO NEWTON - RAPHSON
#EJEMPLO2

#IMPORTAR LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

#PUNTO INICIAL
Xo = 1
print("Valor del punto inicial =   ",Xo)

#VALOR DEL ERROR
error = 0.001
print("Valor del error =   ",error,"%")

#"E" ES EL VALOR DEL ERROR ACTUAL
E=100

#LISTA EN DONDE SE IRAN GUARDANDO TODAS LAS ITERACIONES DE X
X1 = [Xo]

#VARIABLE PARA MANEJAR LOS ELEMNTOS DE LA FUNCION
i=0

#CREAR LISTA PARA DIBUJAR LA GRAFICA POSTERIORMENTE
X=np.linspace(-2,3,100)

#EVALUAMOS LOS VALORES DE LA LISTA X EN LA FUNCION
Y= X**3 - 2*X**2 - 4*X + 8

#AQUI INICIALIZO LAS SIGUIENTES LISTA PARA GRAFICAR LOS EJES X y Y
x2= X
y2 = np.zeros(len(x2))

y3=np.linspace(0,10,100)
x3=np.zeros(len(y3))

y4= y3


#DERIVADA DE LA FUNCION ORIGINAL
#Y2= 3*X**2 - 4*X - 4

#INICIO DEL CICLO WHILE (TRUE CUANDO EL ERROR ACTUAL SEA MAYOR AL VALOR DE CONVERGENCIA)
while (E > error):
    
#z1 es el numerador de la fraccion es el equivalente a f(Xi)
    z1=(X1[i]**3 - 2*X1[i]**2 - 4*X1[i] + 8)
#z2 es el denomindaor de la fraccion es el quivalente a f´(Xi)
    z2=(3*(X1[i]**2) - 4*X1[i] - 4)

#Es la nueva iteracion
    x =  X1[i] - (z1/z2)
    fx = x**3 -2*x**2 -4*x + 8
#LISTA DE ZEROS DEL MISMO TAMAÑO QUE X1    
    y= np.zeros(len(X1))

#AGREGAR EL ELEMENTO x EN LA LISTA X1    
    X1.append(x)

#SI LA OTERACION LA SEGUNDA O MAS ENTONCES CALCULA EL ERROR        
    if i >= 1:
        E = abs((X1[i]-X1[i-1])/X1[i])*100
        print("ERROR ACTUAL DE:   ",E,"%")

    x4=np.full(len(y3),x)
    

    
#SE DIBUJA LA GRAFICA    
    plt.plot(X,Y,color="red")
    plt.plot(x2,y2,color="black")
    plt.plot(x3,y3,color="black")
    plt.plot(x,fx,"s",color="purple")
    plt.plot(x,y[i],".",color="blue")
    
#EL NUMERO DE LA ITERACION AUMENTA EN 1
    i=i+1
    
    P=["x = f(x)","eje x","eje y","f(x)","Raiz"]
    plt.legend(P)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(i)
    plt.show()
    

#SE IMPRIME LA RAIZ Y EL NUMERO DE LA ITERACION
print("LA RAIZ APROXIMADA ES:   ",x) 
print("El numero de iteracoines fue de  :",i)