from diffeq_tsint import *
import numpy as np
import matplotlib.pyplot as plt

T_0 = 21.
t = 50
N = 100
dt = t/N
T_out = -5
k = 0.1
x_0 = T_0
t_val = np.array([t*i/N for i in range(N+1)])

def cool(T, t):
	return -k * (T-T_out)

def ex_sol(t, x_0):
	return T_out + np.exp(-k*t) * (x_0 - T_out)

T_data, T_err = rk45(cool, x_0, t_val)
T_ex = ex_sol(t_val, x_0)

for i in range(1, len(T_err)):
	T_err[i] += T_err[i-1]

plt.plot(t_val, abs(T_data-T_ex), 'r-', label=r'napaka (21 $\degree C$)')
plt.plot(t_val, T_err, 'r:', label=r'ocena napake (21 $\degree C$)')

T_0 = -10.
x_0 = T_0
T_data_1, T_err_1 = rk45(cool, x_0, t_val)
T_ex_1 = ex_sol(t_val, x_0)

for i in range(1, len(T_err_1)):
	T_err_1[i] += T_err_1[i-1]

plt.plot(t_val, abs(T_data_1-T_ex_1), 'b-', label=r'napaka (-15 $\degree C$)')
plt.plot(t_val, T_err_1, 'b:', label=r'ocena napake (-15 $\degree C$)')
plt.xlabel('t')
plt.ylabel(r'$\Delta T [\degree C]$')
plt.legend()
plt.show()