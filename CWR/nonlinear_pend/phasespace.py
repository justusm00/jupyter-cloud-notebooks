import numpy as np
import matplotlib.pyplot as plt


t = np.loadtxt("time.dat")

#load position 
phi_eu = np.loadtxt("pos_euler.dat",usecols = 0)
phi_rk2 = np.loadtxt("pos_rk2.dat",usecols = 0)
phi_rk4 = np.loadtxt("pos_rk4.dat",usecols = 0)

#load velocity
v_eu = np.loadtxt("pos_euler.dat",usecols = 1)
v_rk2 = np.loadtxt("pos_rk2.dat",usecols = 1)
v_rk4 = np.loadtxt("pos_rk4.dat",usecols = 1)


delta_t = np.loadtxt("delta.dat")



fig, axs = plt.subplots(3, figsize=(10,20), dpi = 400)
plt.subplots_adjust(hspace = 0.5)


axs[0].grid()
axs[0].set_ylabel(r'$\varphi$')
axs[0].set_xlabel(r'$\dot\varphi$')
axs[0].plot(phi_eu, v_eu,  'k' ,lw = 0.5)
axs[0].set_title("Euler")

axs[1].grid()
axs[1].set_ylabel(r'$\varphi$')
axs[1].set_xlabel(r'$\dot\varphi$')
axs[1].plot(phi_rk2, v_rk2,  'k' ,lw = 0.5)
axs[1].set_title("RK2")

axs[2].grid()
axs[2].set_ylabel(r'$\varphi$')
axs[2].set_xlabel(r'$\dot\varphi$')
axs[2].plot(phi_rk4, v_rk4,  'k' ,lw = 0.5)
axs[2].set_title("RK4")

fig.suptitle("phasespace for $\Delta t=%g$ s" %delta_t)

fig.savefig("nonlinear_pend_phasespace.pdf")
fig.show()
