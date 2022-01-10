from diffeq_tsint import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm


T_0 = 21.
t = 50
N = 100
dt = t/N
T_out = -5
k_0 = 0.02
k = k_0
x_0 = T_0
t_val = np.array([t*i/N for i in range(N+1)])

def cool(T, t):
	return -k * (T-T_out)

def ex_sol(t, x_0):
	return T_out + np.exp(-k*t) * (x_0 - T_out)

fig, ax = plt.subplots(1, 1)

colormap = plt.cm.cool
num_plots = 20
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.cool(np.linspace(0, 1, num_plots))))

normalize = mcolors.Normalize(k_0, k_0*num_plots)

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(np.arange(k_0, k_0*num_plots, num_plots))
cbar = plt.colorbar(scalarmappaple, location='right')

cbar.set_label('k', rotation=0)

for i in range(1, 1+num_plots):
	k = k_0*i
	#solve equation

	T_data = rku4(cool, x_0, t_val)

	T_ex = ex_sol(t_val, x_0)

	#plots

	ax.plot(t_val, abs(T_data-T_ex), label=str(k))
	#ax.plot(t_val, T_data, label=r'$\Delta t = $'+str(round(dt, 1)))

ax.set_xlabel('t')
ax.set_ylabel(r'$\Delta T [\degree C]$')
ax.set_yscale('log')

#ax.legend(loc=1)

plt.show()