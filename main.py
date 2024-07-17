import pandas as pd #allow to load in the csv file
import csv 
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_decription


class CSV:
    CSV_FILE = "finance_data.csv" #class variable
    COLUMNS = ["date", "amount", "category", "description"]
    
    #This will have access to the classess itself but it won t have access to its instance
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):    #adding entries using dictionary
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:    #a = pending to the end of the file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) #csv writer
            writer.writerow(new_entry)
        print("Entry added successfully")

CSV.initialize_csv()
CSV.add_entry("16-07-2024", 435.28, "Income", "Salary")
        