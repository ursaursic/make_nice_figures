import matplotlib.pyplot as plt
from generate_data import *

style = './mynewstyle.mplstyle'
plt.style.use(style)


x, y = simple_sin_plot(1000, 0.2, 0.1)
fit_x, fit_y = simple_sin_plot(1000, 0.2, 0)

plt.plot(x, y, 'o', alpha=0.5)
plt.plot(x, 0.5*y, 'o', alpha=0.5)
plt.plot(x, 1.5*y, 'o', alpha=0.5)
plt.plot(fit_x, fit_y, 'k-')
plt.title('Fun stuff!!')
plt.xlabel('X label (unit)')
plt.ylabel('Y label (unit)')
plt.show()