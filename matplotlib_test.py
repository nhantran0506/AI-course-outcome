#21110790
import numpy as np
import matplotlib.pyplot as plt
# Exercise a

def g(x, u, o):
    return 1/(o*np.sqrt(2*np.pi))*np.exp( (-(x-u)**2)/(2*o**2) )

x = np.linspace(-10, 10, 100)
params = np.array([[0, 1.2], [0, 3.14], [5, 1.2], [5, 3.14]])

for u, o in params:
    plt.plot(x, g(x, u, o), label=f'u={u}, o={o}')
    
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Gaussian function')
plt.legend()
plt.show()

# Exercise b

def f(x, y, A, x0, y0, ox, oy):
    return A*np.exp(-( ((x-x0)**2)/(2*ox**2) + ((y-y0)**2)/(2*oy**2) ))

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
params = np.array([1.2, 3.14])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
for o in params:
    Z = f(X, Y, 1, 0, 0, o, o)
    ax.plot_surface(X, Y, Z, cmap='coolwarm')
    
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('2D Gaussian function')
plt.show()