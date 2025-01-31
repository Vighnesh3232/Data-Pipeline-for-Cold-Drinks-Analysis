import pandas as pd
import os
import matplotlib.pyplot as plt

# Define the input and output folders
input_folder = "./airflow/input_data"
extract_folder = "./airflow/extract_folder"

# Ensure the folders exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(extract_folder, exist_ok=True)


def load_data_from_directory():
    """Load data from CSV files in a directory into a single DataFrame."""
    all_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]
    if not all_files:
        raise FileNotFoundError("No CSV files found in the input directory.")

    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)

    # Convert relevant columns to numeric if they exist
    if 'Age' in combined_df.columns:
        combined_df['Age_Numeric'] = pd.to_numeric(combined_df['Age'], errors='coerce')
    if 'Price' in combined_df.columns:
        combined_df['Price_Numeric'] = pd.to_numeric(combined_df['Price'], errors='coerce')
    if 'Frequency' in combined_df.columns:
        combined_df['Frequency_Numeric'] = pd.to_numeric(combined_df['Frequency'], errors='coerce')

    return combined_df


def analyze_age_vs_frequency(df):
    """Analyze the relationship between age and frequency of cold drink consumption."""
    if 'Age_Numeric' in df.columns and 'Frequency_Numeric' in df.columns:
        correlation = df['Age_Numeric'].corr(df['Frequency_Numeric'])
        print(f"Correlation between Age and Frequency: {correlation}")
        plt.scatter(df['Age_Numeric'], df['Frequency_Numeric'])
        plt.title('Age vs Frequency of Cold Drink Consumption')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig(f"{extract_folder}/age_vs_frequency.png")
    else:
        print("Required columns are missing for analysis.")


def marketing_channels_by_age_group(df):
    """Analyze the most effective marketing channels for different age groups."""
    if 'Age Group' in df.columns and 'Marketing Channel' in df.columns:
        result = df.groupby('Age Group')['Marketing Channel'].value_counts().unstack().fillna(0)
        print(result)
        result.to_csv(f"{extract_folder}/marketing_channels_by_age_group.csv")
    else:
        print("Required columns are missing for analysis.")


def packaging_preferences_health_concerns(df):
    """Identify packaging preferences among people with health concerns."""
    if 'Health Concern' in df.columns and 'Packaging' in df.columns:
        health_concerns = df[df['Health Concern'] == 'Yes']
        packaging_prefs = health_concerns['Packaging'].value_counts()
        print(packaging_prefs)
        packaging_prefs.to_csv(f"{extract_folder}/packaging_preferences_health_concerns.csv")
    else:
        print("Required columns are missing for analysis.")


def taste_ratings_vs_price_range(df):
    """Analyze how taste ratings vary across different price ranges."""
    if 'Price_Numeric' in df.columns and 'Taste Rating' in df.columns:
        df['Price Range'] = pd.cut(df['Price_Numeric'], bins=[0, 10, 20, 30, 50], labels=['Low', 'Medium', 'High', 'Premium'])
        avg_taste_ratings = df.groupby('Price Range')['Taste Rating'].mean()
        print(avg_taste_ratings)
        avg_taste_ratings.to_csv(f"{extract_folder}/taste_ratings_vs_price_range.csv")
    else:
        print("Required columns are missing for analysis.")


def reasons_new_brands_urban_rural(df):
    """Analyze primary reasons preventing consumers from trying new brands in urban vs rural areas."""
    if 'Area' in df.columns and 'Reason' in df.columns:
        urban_reasons = df[df['Area'] == 'Urban']['Reason'].value_counts()
        rural_reasons = df[df['Area'] == 'Rural']['Reason'].value_counts()
        print("Urban Reasons:\n", urban_reasons)
        print("Rural Reasons:\n", rural_reasons)
        urban_reasons.to_csv(f"{extract_folder}/urban_reasons.csv")
        rural_reasons.to_csv(f"{extract_folder}/rural_reasons.csv")
    else:
        print("Required columns are missing for analysis.")