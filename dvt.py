import pandas as pd
import matplotlib.pyplot as plt

# Example data with unequal length arrays
data = {
    'age': [25, 30, 35],
    'year': [2001, 2002, 2003, 2004]  # Notice an extra element here
}

# Correct the data by ensuring equal lengths
data = {
    'year': [2001, 2002, 2003, 2004]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot data
df.plot(x='year', y='age', kind='bar')
plt.show()