import pandas as pd #allow to load in the csv file
import csv 
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_decription


class CSV:
    CSV_FILE = "finance_data.csv" #class variable
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    
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

    #Gives all the trabnsactions within a daterange
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)  #read this as data frame
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)  #convert to date time objects
        start_date = datetime.strptime(start_date, CSV.FORMAT)  #convert start_date to date time object
        end_date = datetime.strptime(end_date, CSV.FORMAT)  #convert end_date to date time object

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)    #filter different rows inside data frame 
        filtered_df = df.loc[mask] #returns a new filtered dataframe where the line above was true

        if filtered_df.empty:
            print("No transaction found in the given data range.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
                )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

            return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_decription()
    CSV.add_entry(date, amount, category, description)


def main():
    while True:
        print("\n1. Add a new transaction")
        print("\n2. View transactions and summary within a data range")
        print("\n3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            CSV.get_transactions(start_date, end_date)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()