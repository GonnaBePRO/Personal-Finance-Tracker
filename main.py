import pandas as pd #allow to load in the csv file
import csv 
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv" #class variable
    
    #This will have access to the classess itself but it won t have access to its instance
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)

CSV.initialize_csv()
        