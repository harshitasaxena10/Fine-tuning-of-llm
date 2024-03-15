import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('output1.csv')

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Save the training and testing sets to separate CSV files
train_data.to_csv('train_dataset.csv', index=False)
test_data.to_csv('test_dataset.csv', index=False)
