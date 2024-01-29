import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return np.heaviside(n, 0)

x = np.linspace(-8, 8, 10000)
plt.plot(x, u(-x+5) - u(x+3))
plt.title("Plot of x(n) function")
plt.grid(1)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.savefig('fig_1.png')
