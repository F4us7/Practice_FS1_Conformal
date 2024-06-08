import numpy as np
import matplotlib.pyplot as plt
import math, cmath, colorsys


x_point = np.arange(-0.8, 0.8, 0.01)
y_point = np.arange(-0.8, 0.8, 0.01)
z_point = []
for n in x_point:
    for m in y_point:
        z_point.append(complex(n, m))
point = []
color_point = []    
for z in z_point:
    z_polar = cmath.polar(z)
    r_min = 0.2 * max(abs(math.cos(0.2 * (z_polar[1] + 2*math.pi*k))) for k in range(6))
    r_max = 0.75 * max(abs(math.cos(5 * (z_polar[1] + 2*math.pi*k) / 3)) for k in range(3))
    if r_min  < z_polar[0] < r_max:
        point.append(z)
        color_point.append(colorsys.hls_to_rgb(z_polar[1] / (2 * math.pi), z_polar[0]**0.5 / (1 + (z_polar[0])**0.5), 1))

point = np.array(point)
color_point = np.array(color_point)

plt.figure()
#plt.axis([-0.8, 0.8, -0.8, 0.8])
plt.axis([-2, 2, -2, 2])
plt.title("0.2 |cos( arg(z) / 5)| < |z| < 0.75 |cos(5 arg(x) / 3)|")
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.scatter(point.real, point.imag, c = color_point)
plt.show()

f_point = []

for z in point:
    f_point.append(cmath.exp(1j * z - 1j))
f_point = np.array(f_point)

plt.figure()
#plt.axis([-0.5, 1.6, -2.1, 0])
plt.axis([-2, 2, -2, 2])
plt.title("f(z) = exp(iz - i)")
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.scatter(f_point.real, f_point.imag, c = color_point)
plt.show()
