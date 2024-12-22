import subprocess

import pandas as pd
import matplotlib.pyplot as plt
from numpy.version import git_revision

# Create a sample DataFrame
data = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 15]}
df = pd.DataFrame(data)

# Plot the data
df.plot(x='Category', y='Values', kind='bar', legend=False)
plt.title("Sample Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()
