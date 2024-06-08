import numpy as np
import matplotlib.pyplot as plt
import math, cmath


theta = np.arange(0, 4*math.pi, 0.001)
z_rose = []
for t in theta:
    z_rose.append(complex(1.2 * abs(math.cos(0.75 * t))*math.cos(t), 1.2 * abs(math.cos(0.75 * t))*math.sin(t)))

z_rose = np.array(z_rose)

z_border = []
for phi in np.arange(0, 2*math.pi, 0.001):
    r = 1.2 * max(abs(math.cos(0.75 * (phi + 2*math.pi*k))) for k in range(5))
    z_border.append(complex(r * math.cos(phi),r * math.sin(phi)))     
z_border = np.array(z_border)

r = 0.1
plt.figure()
while r <= 1.3:
    x_axis1 = []
    y_axis1 = []
    for i in np.arange(0, 2*math.pi, 0.001):
        x_axis1.append(r * math.cos(i))
        y_axis1.append(r * math.sin(i))
    plt.plot(x_axis1,y_axis1, color="black", linewidth=0.2)
    r += 0.1
    
phi = 0
while phi <= 2*math.pi:
    x_axis1 = []
    y_axis1 = []
    for i in np.arange(0, 1.3, 0.001):
        x_axis1.append(i * math.cos(phi))
        y_axis1.append(i * math.sin(phi))
    plt.plot(x_axis1,y_axis1, color="black", linewidth=0.2)
    phi += math.pi / 10

plt.axis([-1.3, 1.3, -1.3, 1.3])
plt.title("|z| = 1.2 * |cos(0.75 * arg(x))|")
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.plot(z_rose.real, z_rose.imag, color='red', linewidth=1)
plt.scatter(z_border.real, z_border.imag, s=3, color='red')
plt.show()

fz_rose = []
for t in z_rose:
    fz_rose.append(cmath.asin(0.5j * t))
fz_rose = np.array(fz_rose)

fz_border = []
for t in z_border:
    fz_border.append(cmath.asin(0.5j * t))
fz_border = np.array(fz_border)
plt.figure()

r = 0.1
plt.figure()
while r <= 1.3:
    z_axis = []
    for i in np.arange(0, 2*math.pi, 0.001):
       t = complex(r * math.cos(i), r * math.sin(i))
       z_axis.append(cmath.asin(0.5j * t))
    z_axis = np.array(z_axis)
    plt.plot(z_axis.real,z_axis.imag, color="black", linewidth=0.2)
    r += 0.1
    
phi = 0
while phi <= 2*math.pi:
    z_axis = []
    for i in np.arange(0, 1.3, 0.001):
        t = complex(i * math.cos(phi), i * math.sin(phi))
        z_axis.append(cmath.asin(0.5j * t))
    z_axis = np.array(z_axis)
    plt.plot(z_axis.real,z_axis.imag, color="black", linewidth=0.2)
    phi += math.pi / 10






#plt.axis([-0.7, 0.7, -0.7, 0.7])
plt.axis([-1.3, 1.3, -1.3, 1.3])
plt.title("f(z) = arcsin(0.5 * iz)")
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.plot(fz_rose.real, fz_rose.imag, color='red', linewidth=1)
plt.scatter(fz_border.real, fz_border.imag, s=3, color='red')
plt.show()











        
