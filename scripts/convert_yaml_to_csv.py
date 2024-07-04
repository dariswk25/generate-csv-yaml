import yaml
import pandas as pd

# Load the YAML file
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data.csv', index=False)
