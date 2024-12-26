import matplotlib
matplotlib.use('TkAgg')  # Use a compatible backend
import seaborn as sns
import matplotlib.pyplot as plt

# Create a scatter plot
sns.scatterplot(x=[1, 2, 3, 4], y=[10, 20, 25, 30])

# Label the axes and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Show the plot
plt.show()
