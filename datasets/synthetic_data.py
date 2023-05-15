import numpy as np
import pandas as pd

# Generate a random dataset with 100 rows and 5 columns
np.random.seed(1234)
df = pd.DataFrame(np.random.randn(100, 5))

# Name the columns
df.columns = ['col1', 'col2', 'col3', 'col4', 'col5']

# Print the first 5 rows of the dataset
df.head()

# Save the dataset to a CSV file
df.to_csv('synthetic_data.csv', index=False)
