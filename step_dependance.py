from diffeq_tsint import *
import numpy as np
import matplotlib.pyplot as plt

def cool(T, t):
	return -k * (T-T_out)

def ex_sol(t, x_0):
	return T_out + np.exp(-k*t) * (x_0 - T_out)

T_0 = 21.
t = 50
N = 100
dt = t/N
T_out = -5
k = 0.1
x_0 = T_0

functions = [euler, heun, rk2a, rk2b, rku4, pc4]

max_errors = [2**(-i) for i in range(47)]

linestyles = ['solid', (0, (3, 1, 1, 1, 1, 1)), (0, (3, 5, 1, 5, 1, 5)), (0, (3, 10, 1, 10, 1, 10)), 'dotted', 'solid']

colors = ['k', 'k', 'springgreen', 'r', 'blue', 'fuchsia']

def step_finder(f, max_error):
	N = 1

	max_err = 100

	while max_err > max_error:
		if N > 10:
			N += round(N*0.1)
		else:
			N += 1
		print(N)
		t_val = np.array([t*i/N for i in range(N+1)])
		T_data = f(cool, x_0, t_val)
		T_ex = ex_sol(t_val, x_0)

		max_err = max(abs(T_data-T_ex))

	return N

for j in range(4, len(functions)):
	steps = [step_finder(functions[j], max_errors[i]) for i in range(len(max_errors))]

	print(steps)
	plt.plot(np.log(max_errors), np.log(steps),linestyle=linestyles[j], color=colors[j], label=str(functions[j])[10:-23])
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('napaka')
plt.ylabel('N')
plt.legend()
plt.show()	
