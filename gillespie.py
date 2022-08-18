import numpy as np 
import matplotlib.pyplot as plt 
import math


#const
k_denovo = 1
k_fission = 5
k_fusion = 1
k_gamma = 1 
n0 = 7

N = 400


n = [n0]
time = [0]
#gillespie algorithm
for i in range(N):
    k_total = k_denovo + k_fission*(n[i]) + k_gamma*n[i] + k_fusion*n[i]*(n[i]-1)
    p_deonovo = k_denovo/k_total
    p_fission = k_fission*(n[i])/k_total
    p_fusion = k_fusion*n[i]*(n[i]-1)/k_total
    p_gamma = k_gamma*n[i]/k_total

    tau = time[-1]+np.random.exponential(k_total)
    time.append(tau)

    r1 = np.random.random()
    r2 = np.random.random()
    r3 = np.random.random()
    r4 = np.random.random()
    delta = 0
    if r1 < p_deonovo:
        delta += 1
    if r2 < p_fission:
        delta += 1
    if r3 < p_fusion:
        delta -= 1
    if r4 < p_gamma:
        delta -= 1
    n.append(n[i]+delta)
plt.plot(time, n, label='fission donimated', color='red')
plt.ylabel('n')
plt.xlabel('time')
plt.legend()
plt.show()