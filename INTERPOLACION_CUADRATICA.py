# INTERPOLACION CUADRATICA
import matplotlib.pyplot as plt
import numpy as np

X=[-4,-3,-2,0,2,4.5]
Y=[-10,-2,4,10,8,-5.75]

x=1

#Y = A + BX + CX**2
#PARA LOS PUNTOS: (-2,4),(0,10),(2,8)

#PARA EL PUNTO (0,10)
# 10 = A + B(0) + C(0)**2
# A=10
A=10


#PARA (-2,4),(2,8)
# 4 = 10 + B*(-2) + C*(-2)**2
# 8 = 10 + B*(2) + C*(2)**2

#ENTONCES 
# -2*B + 4C = -6
# 2*B + 4C = -2

# SI SUMAMOS AMBAS ECUACIONES
# 0*B + 8*C = -8
# C = -1
C=-1

# SI C = -1 ENTONCES
# 2*B + 4*C = -2
# 2*B + 4*(-1) = -2
# 2*B -4 = -2
# 2*B = 2
# B=1
B=1


y= A + B*x + C*x**2

X1 = np.linspace(-4,4.5,100)
Y1 = A + B*X1 + C*X1**2

plt.plot(X1,Y1,color="black")
plt.plot(x,y,"o",color="blue")
plt.plot(X[0],Y[0],"o",color="red")
plt.plot(X[1],Y[1],"o",color="red")
plt.plot(X[2],Y[2],"o",color="red")
plt.plot(X[3],Y[3],"o",color="red")
plt.plot(X[4],Y[4],"o",color="red")
plt.plot(X[5],Y[5],"o",color="red")
T = ["f(x)","INTERPOLACION CUADRATICA","DATOS"]
plt.legend(T)
plt.grid()
plt.title("INTERPOLACION CUADRATICA")
plt.show()