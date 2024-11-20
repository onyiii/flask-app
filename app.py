from flask import Flask, request, render_template
from pymongo import MongoClient
from user import User  # Ensure this is implemented correctly

app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_data']
collection = db['user_data']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        # Get and validate form data
        age = request.form.get('age')
        gender = request.form.get('gender')
        income = request.form.get('income')

        if not age or not gender or not income:
            return "Error: Age, gender, and income are required fields!", 400

        # Convert numeric fields
        age = int(age)
        income = float(income)

        # Collect expenses only for checked categories
        expenses = {}
        for expense in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']:
            if expense in request.form:
                expenses[expense] = float(request.form.get(expense, 0))

        # Save the data to MongoDB
        user_data = User(age, gender, income, expenses)  # Assuming User is implemented
        collection.insert_one({
            'age': age,
            'gender': gender,
            'income': income,
            'expenses': expenses
        })

        # Save the user data to CSV
        user_data.save_to_csv('user_data.csv')  # Assuming `append` is supported
        users=user_data.load_data_from_mongodb()
        for user in users:
            print(user.age, user.gender, user.income, user.expenses)

        return "Data submitted and saved to CSV successfully!"

    except ValueError as ve:
        print(f"ValueError during data submission: {ve}")
        return f"Invalid data format: {ve}", 400

    except Exception as e:
        print(f"Error during data submission: {e}")
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
