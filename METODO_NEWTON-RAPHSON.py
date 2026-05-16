#METODO NEWTON - RAPHSON
import numpy as np
import matplotlib.pyplot as plt


Xo = -1.5
print("Valor del punto inicial =   ",Xo)
error = 0.001
print("Valor del error =   ",error,"%")
E=100
X1 = [Xo]
i=0

X=np.linspace(-2,4,100)

x2= X
y2 = np.zeros(len(x2))

y3=np.linspace(-20,20,100)
x3=np.zeros(len(y3))


Y= X**3 - 3*X**2 + 1
Y2= 3*X**2 -6*X





while (E > error):
    
    z1=((X1[i]**3) - 3*X1[i]**2 + 1)
    z2=(3*(X1[i]**2) - 6*X1[i])
    
    x =  X1[i] - (z1/z2)
    
    y= np.zeros(len(X1))
    
    X1.append(x)
        
    if i >= 1:
        E = abs((X1[i]-X1[i-1])/X1[i])*100
        print("ERROR ACTUAL DE:   ",E,"%")
    
    
    
    plt.plot(X,Y,color="red")
    plt.plot(x,y[i],"o",color="blue")
    plt.plot(x2,y2,color="black")
    plt.plot(x3,y3,color="black")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("METODO DE NEWTON-RAPHSON")
    plt.show()
    
    i=i+1


print("LA RAIZ APROXIMADA ES:   ",x) 