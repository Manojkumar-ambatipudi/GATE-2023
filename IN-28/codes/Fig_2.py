import matplotlib.pyplot as plt
import numpy as np 

def u(n):
    return np.heaviside(n,0)

x = np.linspace(-8,8,10000)
plt.plot(x, u(-x+5),'r')
plt.plot(x, u(x+3),'b')
plt.title('plots of functions h(n) and f(n)')
plt.grid(1)
plt.xlabel('n')
plt.ylabel('f(n), h(n)')
plt.legend()
plt.savefig('fig_2.png')

