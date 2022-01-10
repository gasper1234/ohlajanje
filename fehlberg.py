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

def cool(T, t):
	return -k * (T-T_out)

def ex_sol(t, x_0):
	return T_out + np.exp(-k*t) * (x_0 - T_out)

fig, ax = plt.subplots(1, 1)

for i in range(5):
	#solve equation

	t_val_calc, T_data = rkf(cool, 0, t, x_0, 10**(-3-i), 5, 0.01)

	T_ex = ex_sol(t_val_calc, x_0)

	ax.plot(t_val_calc, abs(T_data-T_ex), 'x-', label=r'$10^{%d}, N=%d$'%(-i-3, len(T_ex)))

plt.legend()
plt.yscale('log')
plt.ylabel(r'$\Delta T [\degree C]$')
plt.xlabel('t')
plt.show()