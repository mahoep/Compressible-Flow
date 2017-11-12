import math
import numpy as np
type = "P"
ratio = 5.12096
k = 1.4

max = 20
res =  max/0.001

M = np.linspace(0 ,20, res)
P_ratio = np.linspace(0 , len(M), res)
T_ratio = np.linspace(0 , len(M), res)
#A_ratio = np.linspace(0 , len(M), res)

for i in range(0, len(M)):
    P_ratio[i] = (1+0.5*(k-1)*M[i]**2)**(k/(k-1))
    P_ratio[i] = P_ratio[i]**-1

    T_ratio[i] = (1+0.5*(k-1)*M[i]**2)
    T_ratio[i] = T_ratio[i]**-1
    #A_ratio[i] = 1/M[i]*(1+(k-1)/2*M[i]**2/((k+1)/2))**((k+1)/(2*(k-1)))

if type == "P":
    idx = (np.abs(P_ratio - ratio)).argmin()
    print("For a pressure ratio P/Pt =", ratio, "and k =", k)
    print("M =", M[idx])
elif type == "T":
    idx = (np.abs(T_ratio - ratio)).argmin()
    print("For a temperature ratio T/Tt =", ratio, "and k =", k)
    print("M =", M[idx])
#elif type == "A":
    #idx = (np.abs(A_ratio - ratio)).argmin()
    #print("For an Area ratio A/A* =", ratio, "and k =", k)
    #print("M =", M[idx])
