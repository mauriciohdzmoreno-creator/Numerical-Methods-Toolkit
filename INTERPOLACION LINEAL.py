# INTERPOLACION LINEAL

import matplotlib.pyplot as plt

print("TENIENDO EN CUENTA QUE EL VALOR DE f(x) a aproximar es de x = 1")

i=0

x=1

X=[-4,-3,-2,0,2,4.5]
Y=[-10,-2,4,10,8,-5.75]


y = Y[3] + ((Y[4] - Y[3])/(X[4] - X[3])*(x - X[3]))



plt.plot(X,Y,color="black")
plt.plot(X[0],Y[0],"o",color="red")
plt.plot(x,y,"o",color="blue")
plt.plot(X[1],Y[1],"o",color="red")
plt.plot(X[2],Y[2],"o",color="red")
plt.plot(X[3],Y[3],"o",color="red")
plt.plot(X[4],Y[4],"o",color="red")
plt.plot(X[5],Y[5],"o",color="red")

T=["FUNCION","DATOS","INTERPOLACION LINEAL"]
plt.legend(T)

plt.title("INTERPOLACION LIEAL")
plt.grid()
plt.show()