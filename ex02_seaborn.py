import matplotlib
matplotlib.use('TkAgg')  # Use a compatible backend
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the data as a pandas DataFrame
data = pd.DataFrame({
    'category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [10, 12, 14, 20, 22, 21, 30, 31, 29]
})

# Step 2: Create a box plot
sns.boxplot(x='category', y='value', data=data)

# Step 3: Label the axes and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')

# Step 4: Show the plot
plt.show()
