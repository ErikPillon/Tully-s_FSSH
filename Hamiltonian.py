import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

n = 200
start = -10 
end = 10
x = np.linspace(start,end,n)

def Potential(x):
    A=0.01
    B=1.6
    C=0.005
    D=1.0
    V=[[0,0],[0,0]]
    if x>0:
        V[0][0]=A*(1-np.exp(-B*x))
    else:
        V[0][0]=-A*(1-np.exp(B*x))
    V[1][1] = -V[0][0]
    V[0][1] = C*np.exp(-D*x**2)
    V[1][0] = V[0][1]
    return V

y = []
for i in x:
    v,w=LA.eigh(Potential(i))
    y.append(v)

k = 8.0
sigma = 20.0/k
psi = np.exp(1j*k*x)*np.exp(-(x/sigma)**2)     
#Hamiltonian = T+V

plt.figure()
plt.plot(x,y)
plt.plot(x,abs(psi)/50)
plt.show()
