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

fig, ax = plt.subplots(2, 1, sharex=True)
plt.subplots_adjust(hspace=0.1)

for i in range(1, 6):
	N = 2*2**i
	dt = t / N
	t_val = np.array([t*i/N for i in range(N+1)])

	#solve equation

	T_data = rku4(cool, x_0, t_val)

	T_ex = ex_sol(t_val, x_0)

	#plots

	#ax[0].plot(t_val, abs(T_data-T_ex), label=r'$\Delta t = $'+str(round(dt, 1)))
	ax[0].plot(t_val, T_data, label=r'$\Delta t = $'+str(round(dt, 1)))
	#ax[0].plot(t_val, T_data, label='euler')

N = 100
t_val = np.array([t*i/N for i in range(N+1)])
T_ex = ex_sol(t_val, x_0)

ax[0].plot(t_val, T_ex, 'k--', label='eksaktna')
ax[0].set_ylabel(r'$T [\degree C]$')
ax[0].legend(loc=1)

for i in range(1, 6):
	N = 2*2**i
	dt = t / N
	t_val = np.array([t*i/N for i in range(N+1)])

	#solve equation

	T_data = rku4(cool, x_0, t_val)

	T_ex = ex_sol(t_val, x_0)

	#plots

	ax[1].plot(t_val, abs(T_data-T_ex), label=r'$\Delta t = $'+str(round(dt, 1)))
	#ax[0].plot(t_val, T_data, label=r'$\Delta t = $'+str(round(dt, 1)))
	#ax[0].plot(t_val, T_data, label='euler')

ax[1].set_xlabel('t')
ax[1].set_ylabel(r'$\Delta T [\degree C]$')
ax[1].set_yscale('log')
ax[1].legend(loc=1)

plt.show()