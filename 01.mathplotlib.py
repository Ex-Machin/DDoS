import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # Sample data.

fix, ax1 = plt.subplots()
plt.plot(x, x**2, color='green')
ax1.set_title('Kwadraty i sześciany liczb', fontsize=20)
ax1.set_xlabel('Liczby', fontsize=16)
ax1.set_ylabel('Kwadray liczb', fontsize=16)
ax1.tick_params(axis='y', color='green')
ax2 = ax1.twinx()

ax2.plot(x, x ** 3)
ax2.set_ylabel("Sześciany liczb", fontsize = 16, color = 'red')


plt.savefig('wykres.jpg')

