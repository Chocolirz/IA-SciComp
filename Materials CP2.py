import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt('matcp2dat.txt', delimiter='')

x = data[0:6,0]
y = data[0:6,1]

print('x=',x)
print('y=',y)

def gaussian(x, A, mu, sigma):
    y = A * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    return y

# Curve fit the histgram data using curve_fit()
popt, pcov = curve_fit(gaussian, x, y,p0=(98.8, 240, 100))
perr = np.sqrt(np.diag(pcov))

# Report the values of the fitted parameters and their errors
print('A =', round(popt[0], 3), '+/-', round(perr[0], 3))
print('mu =', round(popt[1], 3), '+/-', round(perr[1], 3))
print('sigma =', round(popt[2], 3), '+/-', round(perr[2], 3))

# prepare for the fitted curve
u = np.arange(98, 101.5, 0.01)
v = round(popt[0], 3) * np.exp(-(u - round(popt[1], 3)) ** 2 / (2 * round(popt[2], 3) ** 2))

# Create histogram of result and superimpose plot
plt.figure(figsize=(10, 6))
plt.title('Fitted plot for (400) peak')
plt.plot(u, v, '-', label='Fitted Function', color='orange')
plt.xlabel('2 theta value / degree')
plt.ylabel('Radiative intensity / counts per second')
plt.legend()
plt.show()