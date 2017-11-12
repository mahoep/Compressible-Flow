import math
import numpy as np
M = 1.0
k = 1.4

P = (1+0.5*(k-1)*M**2)**(k/(k-1))
rho = (1+0.5*(k-1)*M**2)**(1/(k-1))
T = 1 + (k-1)/2*M**2
A = (1/M*((1+0.5*(k-1)*M**2)/(0.5*(k+1)))**(0.5*(k+1)/(k-1)))**-1
v = ((k+1)/(k-1))**(1/2)*np.arctan(((k-1)/(k+1)*(M**2-1))**(1/2))-np.arctan((M**2-1)**(1/2))
mu = np.arcsin(1/M)

P = P**-1
rho = rho**-1
T = T**-1
A = A**-1
PtA = P*A

print("For M =",M,"and k =",k,":")
print("P/Pt =",P)
print("rho/rhot =",rho)
print("T/Tt =",T)
print("A/A* =",A)
print("PA/PtA* =",PtA)
