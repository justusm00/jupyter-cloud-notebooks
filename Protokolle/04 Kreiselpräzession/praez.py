import numpy as np
import matplotlib.pyplot as plt


g = 9.81	#grav.constan
m1 = 0.01	#mass 1
m2 = 0.06	#mass 2
m3 = 0.04	#mass 3
r = 0.27	#distance to mass


omegaTr = 0.01
omegaTp = np.sqrt(0.5**2+0.01**2)
omegar = 0.003

"""the periodes for 10g. uppermost is the wheel"""
t0 = np.array([0.14, 0.335, 0.619, 0.985])/3
t1 = np.array([66, 38, 21, 16.5])*2

"""the periodes for 60g. uppermost is the wheel"""
t2 = np.array([0.161, 0.215, 0.267, 0.310])/3
t3 = np.array([11, 10, 8, 7])*2

"""the periodes for 40g. uppermost is the wheel"""
t4 = np.array([0.134, 0.188, 0.334, 0.450])/3
t5 = np.array([20.5, 16.5, 11, 8])*2



"""Error"""
def err(t, t1, m, e, f, d):
	return np.sqrt(e**2*(t1*m*g*r/(2*np.pi))**2+f**2*(t*m*g*r/(2*np.pi))**2+d**2*(t*t1*m*g/(2*np.pi))**2)

print(err(t0, t1, m1, omegaTr, omegaTp, omegar), err(t2, t3, m2, omegaTr, omegaTp, omegar), err(t4, t5, m3, omegaTr, omegaTp, omegar))


def delta(t, t1):
	"""calculating the inverse of the angular velocity, so as to get 1/(w_r*w_p)"""
	return t1*t/(4*np.pi**2)

"""defining the inverse of the angular velocity as variables"""
d1 = delta(t0, t1)
d2 = delta(t2, t3)
d3 = delta(t4, t5)


md1 = np.mean(d1)
md2 = np.mean(d2)
md3 = np.mean(d3)

def I(md, m):
	"""calculating the inertia"""
	return md*m*g*r


print (I(md1, m1), I(md2, m2), I(md3, m3))


a = 0.245/2
c = 0.06/3


ms = 1.33
ls = 0.12
ma = 0.936
la = 0.17

def Ia(m):
	return ms*ls**2+ma*la**2+m*r**2
print(Ia(m1), Ia(m2), Ia(m3))


print(a**2*ms/2+c**2*ma/2)


w0 = 2*np.pi/t0
w1 = 2*np.pi/t1
w2 = 2*np.pi/t2
w3 = 2*np.pi/t3
w4 = 2*np.pi/t4
w5 = 2*np.pi/t5


v1 = w0*w1
v2 = w2*w3
v3 = w4*w5

b1 = np.mean(v1)
b2 = np.mean(v2)
b3 = np.mean(v3)

def k(b, m):
	"""calculating the inertia"""
	return m*g*r/b

print(k(b1, m1), k(b2, m2), k(b3, m3))
