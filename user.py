import csv
import os
from pymongo import MongoClient


class User:
    def __init__(self, age, gender, income, expenses):
        """
        Initialize a User object with basic user information.
        """
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def save_to_csv(self, filename='survey_data.csv'):
        """
        Save the user data into a CSV file.
        """
        try:
            # Check if the file exists
            file_exists = os.path.exists(filename)

            with open(filename, mode='a', newline='') as file:  # Append mode
                writer = csv.writer(file)
                # Write header if the file is new
                if not file_exists:
                    writer.writerow(['Age', 'Gender', 'Income', 'Expenses'])
                writer.writerow([self.age, self.gender, self.income, self.expenses])
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    @staticmethod
    def load_data_from_mongodb():
        """
        Load data from MongoDB and return a list of User objects.
        """
        try:
            client = MongoClient('mongodb://localhost:27017/')
            db = client['survey_data']
            collection = db['user_data']

            users = []
            for record in collection.find():
                # Use .get() to safely access fields
                age = record.get('age', 0)
                gender = record.get('gender', 'Unknown')
                income = record.get('income', 0.0)
                expenses = record.get('expenses', {})
                users.append(User(age, gender, income, expenses))

            return users
        except Exception as e:
            print(f"Error loading data from MongoDB: {e}")
            return []
