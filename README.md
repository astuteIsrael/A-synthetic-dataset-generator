# Synthetic Prostate Cancer Dataset

This repository contains a Python script that generates a synthetic dataset for a prostate cancer study. The dataset mimics real-world data with features that are often used in cancer diagnosis, such as radius, texture, perimeter, area, and smoothness.

## Dataset Details

- **Number of Samples:** 250
- **Features:**
  - `radius`: Generated using a normal distribution with a mean of 14 and a standard deviation of 2.
  - `texture`: Generated using a normal distribution with a mean of 20 and a standard deviation of 5.
  - `perimeter`: Generated using a normal distribution with a mean of 80 and a standard deviation of 10.
  - `area`: Generated using a normal distribution with a mean of 600 and a standard deviation of 100.
  - `smoothness`: Generated using a normal distribution with a mean of 0.1 and a standard deviation of 0.02.
- **Label:**
  - `label`: 0 for benign, 1 for malignant (randomly assigned).

## Files

- `synthetic_prostate_cancer_dataset.py`: The Python script that generates the synthetic dataset.
- `prostate_cancer_dataset.csv`: The generated synthetic dataset saved as a CSV file.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/synthetic-prostate-cancer-dataset.git

2.  Run the Python script to generate the dataset:  python synthetic_prostate_cancer_dataset.py


3.  License:

- Replace `your-username` in the clone URL with your actual GitHub username.
- If you initialized your repository with a README, you can simply edit it with this content.
- You might want to add a `LICENSE` file as well if you plan to open source the code.

This setup will give you a well-documented project on GitHub that others can easily understand and use.

