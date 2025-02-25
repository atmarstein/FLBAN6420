from flask import Flask, render_template, request, redirect, send_file
import os
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Initialize the Flask application
# The 'template_folder' argument ensures Flask knows where to find HTML templates
app = Flask(__name__, template_folder=os.path.abspath("templates"))

# Establish a connection to the MongoDB database
# Replace 'test:test' with actual username and password if needed
client = MongoClient("mongodb://test:test@cluster0-shard-00-00.3nduw.mongodb.net:27017,"
                     "cluster0-shard-00-01.3nduw.mongodb.net:27017,"
                     "cluster0-shard-00-02.3nduw.mongodb.net:27017/"
                     "?replicaSet=atlas-aow68k-shard-0&ssl=true&authSource=admin")

# Select the database and collection
# 'aws' is the database name, 'davi' is the collection name
db = client["aws"]
collection = db["davi"]

# Define the main route for handling GET and POST requests
@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Retrieve form data from the request
        user_data = {
            "age": request.form["age"],
            "gender": request.form["gender"],
            "income": request.form["income"],
            "expenses": { 
                "utilities": request.form.get("utilities", 0),
                "entertainment": request.form.get("entertainment", 0),
                "school_fees": request.form.get("school_fees", 0),
                "shopping": request.form.get("shopping", 0),
                "healthcare": request.form.get("healthcare", 0),
            }
        }
        
        # Insert the collected user data into MongoDB
        collection.insert_one(user_data)
        
        # Redirect back to the survey form after submission
        return redirect("/")
    
    # Render the survey form template with an export button
    return render_template("index.html")

# Route to export data to CSV and download it
@app.route("/export")
def export_to_csv():
    # Fetch data from MongoDB, excluding the MongoDB '_id' field
    data = list(collection.find({}, {"_id": 0}))
    
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Define the CSV file path
    csv_path = "survey_data.csv"
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)
    
    # Send the file as a response for download
    return send_file(csv_path, as_attachment=True)

@app.route("/generate_plots")
def generate_plots():
    # Fetch data from MongoDB, excluding the MongoDB '_id' field
    data = list(collection.find({}, {"_id": 0}))
    
    # Check if data is empty
    if not data:
        return redirect("/")  # Or render a message saying no data is available

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Ensure numeric types for plotting
    df["age"] = pd.to_numeric(df["age"], errors='coerce')
    df["income"] = pd.to_numeric(df["income"], errors='coerce')
    expense_categories = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]
    for category in expense_categories:
        df[category] = pd.to_numeric(df["expenses"].apply(lambda x: x.get(category, 0)), errors='coerce')

    # Age vs Income Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df["age"], df["income"], c="blue")
    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.title("Age vs Income")
    plt.savefig("age_vs_income.png")
    plt.close()
    
    

    # Gender Spending Distribution
    gender_spending = df.groupby("gender")[expense_categories].sum()

    gender_spending.plot(kind="bar", stacked=True, figsize=(8, 5))
    plt.title("Gender-wise Spending Distribution")
    plt.savefig("gender_spending.png")
    plt.close()
    
    #send_file("gender_spending.png", as_attachment=True)
    
    return send_file("age_vs_income.png", as_attachment=True)

# Run the Flask application on host 0.0.0.0 and port 8000
# Setting 'debug=False' for production use
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
