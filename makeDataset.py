import random
import pandas as pd
import numpy as np

# Set the number of clients and days
num_clients = 10000
num_days = 365 * 2

# Generate a list of client IDs
client_ids = [f"client_{i}" for i in range(num_clients)]

# Generate a list of dates
dates = [f"{i}" for i in range(num_days)]

# Generate fake data for each client and day
client_data = []
for client_id in client_ids:
    for date in dates:
        age = random.randint(18, 75)
        gender = random.choice(["Male", "Female"])
        location = random.choice(["London", "New York", "Paris", "Berlin", "Tokyo"])
        balance = random.randint(0, 100000)
        debt = random.randint(0, balance)
        score = random.randint(400, 850)
        withdrawals = random.randint(0, 1000)
        deposits = random.randint(0, 1000)
        client_data.append([client_id, date, age, gender, location, balance, debt, score, withdrawals, deposits])

# Create a DataFrame from the generated data
client_df = pd.DataFrame(client_data, columns=["client_id", "date", "age", "gender", "location", "balance", "debt", "score", "withdrawals", "deposits"])

# Generate a "loans table"
num_loans = int(num_clients * num_days * 0.01)
loan_data = []
for i in range(num_loans):
    loan_id = f"loan_{i}"
    customer_id = random.choice(client_ids)
    date = random.choice(dates)
    loan_size = random.randint(1000, 100000)
    loan_type = random.choice(["Personal", "Business", "Mortgage", "Auto"])
    loan_data.append([loan_id, customer_id, date, loan_size, loan_type])

# Create a DataFrame from the loan data
loan_df = pd.DataFrame(loan_data, columns=["loan_id", "customer_id", "date", "loan_size", "loan_type"])

# Add a "loan_taken" column to the client DataFrame based on the loans table
client_df["loan_taken"] = np.where(client_df.client_id.isin(loan_df.customer_id) & (client_df.date.astype(int) + 1).isin(loan_df.date.astype(int)), 1, 0)

# Save the DataFrames to CSV files
client_df.to_csv("client_data.csv", index=False)
loan_df.to_csv("loan_data.csv", index=False)
