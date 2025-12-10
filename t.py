import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

class LibraryDashboard:
    def _init_(self):
        self.transactions_df = pd.DataFrame()
        self.statistics = {}

    def load_data(self, file_path):
        print(f"Loading data from: {file_path}...")
        try:
            df = pd.read_csv(file_path)
            df.columns = ['Transaction_ID', 'Date', 'User_ID', 'Book_Title', 'Genre', 'Duration_Days']
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            initial_count = len(df)
            df.drop_duplicates(inplace=True)
            print(f"Removed {initial_count - len(df)} duplicate rows.")
            df.dropna(subset=['Date', 'Book_Title', 'Duration_Days'], inplace=True)
            df['Duration_Days'] = df['Duration_Days'].astype(int)
            self.transactions_df = df
            print(f"Data loaded, cleaned, and validated successfully. Total transactions: {len(df)}")
            return True         
            
        except Exception as e:
            print(f"An unexpected error occurred during data loading: {e}")
            return False