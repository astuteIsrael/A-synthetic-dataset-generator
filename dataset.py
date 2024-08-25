import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
data_size = 250
features = {
    'radius': np.random.normal(14, 2, data_size),  # Feature 1
    'texture': np.random.normal(20, 5, data_size),  # Feature 2
    'perimeter': np.random.normal(80, 10, data_size),  # Feature 3
    'area': np.random.normal(600, 100, data_size),  # Feature 4
    'smoothness': np.random.normal(0.1, 0.02, data_size),  # Feature 5
}

# Label (0 for benign, 1 for malignant)
labels = np.random.choice([0, 1], size=data_size)

# Create DataFrame
df = pd.DataFrame(features)
df['label'] = labels

# Save the dataset to a CSV file
df.to_csv('prostate_cancer_dataset.csv', index=False)

print("Dataset created and saved as 'prostate_cancer_dataset.csv'.")
