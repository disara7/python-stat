import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend

import matplotlib.pyplot as plt

plt.subplot(2,1,1)
plt.plot([1, 2, 3, 4], [10,20,25,30])
plt.title('Subplot 1')

plt.subplot(2,1,2)
plt.plot([1,2,3,4], [5,15,20,25])
plt.title('Subplot 2')

plt.tight_layout()
plt.show()