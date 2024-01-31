import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return np.heaviside(n, 1)

x = np.arange(-8, 9)
plt.stem(x, u(-x+5)-u(x+3))
plt.title("Plot of x(n) function")
plt.grid(1)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.savefig('fig_1.png')

plt.clf()
x = np.arange(-8, 9)
plt.stem(x, u(x+3),'b')
plt.title('plot of function u(n+3)')
plt.grid(1)
plt.xlabel('n')
plt.ylabel('u(n+3)')
plt.savefig('fig_2.png')

plt.clf()
x = np.arange(-8, 9)
plt.stem(x, u(-x+5),'g')
plt.title('plot of function u(-n+5)')
plt.grid(1)
plt.xlabel('n')
plt.ylabel('u(-n+5)')
plt.savefig('fig_3.png')

