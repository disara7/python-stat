import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend

import matplotlib.pyplot as plt

plt.bar(['A','B','C'],[50,30,40],color=['red','blue','green'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Customized Bar Plot')
plt.show()
