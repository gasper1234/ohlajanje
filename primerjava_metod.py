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

functions = [euler, heun, rk2a, rk2b, rku4, pc4]

linestyles = ['solid', (0, (3, 1, 1, 1, 1, 1)), (0, (3, 5, 1, 5, 1, 5)), (0, (3, 10, 1, 10, 1, 10)), 'dotted', 'solid']

colors = ['k', 'k', 'springgreen', 'r', 'blue', 'fuchsia']

def cool(T, t):
	return -k * (T-T_out)

def ex_sol(t, x_0):
	return T_out + np.exp(-k*t) * (x_0 - T_out)

fig, ax = plt.subplots(1, 1)
plt.subplots_adjust(hspace=0.1)

for i in range(len(functions)):	
	#solve equation

	T_data = functions[i](cool, x_0, t_val)

	T_ex = ex_sol(t_val, x_0)

	#plots

	ax.plot(t_val, abs(T_data-T_ex), linestyle=linestyles[i], color=colors[i], label=str(functions[i])[10:-23])
	#ax.plot(t_val, T_data, label=r'$\Delta t = $'+str(round(dt, 1)))

ax.set_xlabel('t')
ax.set_ylabel(r'$\Delta T [\degree C]$')
ax.set_yscale('log')
ax.legend(loc=1)

plt.show()