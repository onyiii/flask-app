# Flask Survey Application

This project is a Flask-based survey application where users can submit their age, gender, income, and expenses information. The data is stored in MongoDB and is used for analysis. The application can be run locally or deployed to an AWS EC2 instance.

## Features

- Collects user data (age, gender, income, and expenses).
- Saves data to MongoDB.
- Allows the user to submit survey data via an API endpoint.
- Data is saved both to the MongoDB database and optionally to a CSV file.
- Can be deployed on an AWS EC2 Windows instance.

## Requirements

- Python 3.8 or higher
- Flask
- MongoDB
- Git (for cloning the repository)

## Installation

### 2. **Install Python Dependencies**

Navigate to the project folder and set up a virtual environment:

```bash
cd your-flask-repo
python -m venv venv
.\venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```txt
Flask
pymongo
numpy
pandas
```

### 3. **Set Up MongoDB**

You need a running MongoDB instance to store the survey data. If MongoDB is not installed on your machine:

- [Download and install MongoDB](https://www.mongodb.com/try/download/community) or use a managed service like MongoDB Atlas.
- Make sure MongoDB is running on the default port (`27017`), or modify the connection string in the application code if necessary.

### 4. **Run the Flask Application Locally**

After setting up the environment and MongoDB, run the Flask app:

```bash
python app.py
```

The Flask application should now be running locally at `http://127.0.0.1:5000/`.

You can access the form via the browser or submit data through the `/submit` API endpoint using POST requests with JSON data.

## Deployment on AWS EC2 (Windows Instance)

### 1. **Launch an EC2 Instance**

Follow AWS documentation to launch a Windows EC2 instance:

- [Launching Windows Instances on AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_Win_Intro.html)

### 2. **Set Up the Windows EC2 Instance**

- Ensure **RDP** (Remote Desktop Protocol) is enabled for your EC2 instance.
- SSH into the instance using an RDP client or connect directly via **Remote Desktop**.

### 3. **Install Dependencies on EC2 Instance**

On the EC2 Windows instance:

- Install **Python** and **MongoDB** if not already installed. You can download Python from [here](https://www.python.org/downloads/) and MongoDB from [here](https://www.mongodb.com/try/download/community).
- Clone the repository from GitHub:

  ```powershell
  git clone https://github.com/yourusername/your-flask-repo.git
  ```

- Install the required Python libraries:
  ```powershell
  cd your-flask-repo
  python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  ```

### 4. **Run the Flask Application on EC2**

To run the Flask app:

```powershell
python app.py
```

The Flask app will now be running on the EC2 instance. Ensure the security group for your EC2 instance allows inbound traffic on port `5000` (or whichever port your Flask app is using).

### 5. **Access the Application**

You can access your Flask application by using the **Public IP** of your EC2 instance:

```bash
http://<your-ec2-public-ip>:5000/
```

## API Endpoints

### `/submit` (POST)

- **Description**: Submit user data to the server.
- **Payload**:
  ```json
  {
    "age": 30,
    "gender": "Male",
    "income": 50000,
    "expenses": {
      "utilities": 30000,
      "healthcare": 25000
    }
  }
  ```
- **Response**:
  ```json
  {
    "message": "Data submitted successfully",
    "id": "61372f9a6c5a470b8d2d8a3d"
  }
  ```

## Troubleshooting

- **MongoDB not connecting**: Ensure MongoDB is running on the default port (`27017`) or update the connection string in `app.py`.
- **Missing libraries**: Make sure all dependencies are installed by running `pip install -r requirements.txt`.
- **Firewall issues**: Check if the EC2 security group allows traffic on port `5000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
