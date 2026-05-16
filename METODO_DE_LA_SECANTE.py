#METODO DE LA SECANTE
import numpy as np
import matplotlib.pyplot as plt



Y=[]
Y2=[]


Xo = float(input("Ingrese el valor del primer valor inicial:     "))
Xi = float(input("Ingrese el valor del segundo valor inicial:     "))
error = float(input("Ingrese el valor del criterio de convergencia:     "))

E=100
X1 = [Xo,Xi]
i=0

X=np.linspace(-2,4,100)

X2=np.linspace(-30,30,100)

x2= X
y2 = np.zeros(len(x2))


Y= X**3 - 3*X**2 + 1
#Y2=3*X**2 - 6*X


X4=np.zeros(len(X2))
Y4=X2


i=0

while (E > error):
    
    z1 = (X1[i+1]-X1[i])*(X1[i+1]**3 - 3*X1[i+1]**2 + 1)
    z2 = (X1[i+1]**3 - 3*X1[i+1]**2 + 1)-(X1[i]**3 - 3*X1[i]**2 + 1)
    
    
    x =  X1[i+1] - (z1/z2)
    X1.append(x)
    
    Y3= np.full(len(X),X2)
    X3= np.full(len(Y3),x)
    
    
    
    E = abs((X1[i+1]-X1[i])/X1[i+1])*100
    print("ERROR ACTUAL DE:   ",E,"%")
    
    
    
    plt.plot(X,Y,color="red")
    plt.plot(X4,Y4,color="black")
    plt.plot(X3,Y3,"--",color="red")
    plt.plot(x,0,"o",color="blue")
    plt.plot(x2,y2,color="black")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("METODO DE LA SECANTE")
    plt.show()
    
    i=i+1


print("LA RAIZ APROXIMADA ES:   ",x) 