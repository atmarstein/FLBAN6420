# Flask Survey Application

## Overview

This Flask application allows users to input survey data, generate plots based on the collected data, and download the results in CSV format. Users can also download specific images generated from the survey data analysis.

## Features

- Input survey data (age, gender, income, and expenses)
- Generate visualizations (scatter plots and bar charts)
- Download survey data as a CSV file
- Download generated plot images

## Table of Contents

1. [How to Input Data](#how-to-input-data)
2. [How to Download CSV](#how-to-download-csv)
3. [How to Download Chat Images](#how-to-download-chat-images)

## How to Input Data

To input data into the survey:

1. Launch the application by running the Flask server:
   ```bash
   python app.py
   
2. Open a web browser and navigate to http://localhost:8000.

3. Fill out the survey form with the following fields:

 - Age: Enter your age.
 - Gender: Select your gender (e.g., Male, Female, Other).
 - Income: Input your monthly income.
 - Expenses: Enter your expenses in the respective fields (e.g., utilities, entertainment, school fees, shopping, healthcare).
4. Click the Submit button to save your data.
   
##How to Download CSV

To download the survey data as a CSV file:

Click the Export Data button on the main page.
The CSV file will be generated and automatically downloaded to your device.
Open the CSV file using any spreadsheet software (e.g., Microsoft Excel, Google Sheets) to view the survey data.
How to Download Chat Images
To download the generated chat images (plots):

After submitting the survey data, you can generate the plots by clicking the Generate and Download Plots button.
The application will create visualizations based on the survey data:
Age vs Income Plot: A scatter plot visualizing the relationship between age and income.
Gender Spending Distribution: A bar chart showing spending distribution by gender.
The Age vs Income Plot will be downloaded automatically upon generation. To download the Gender Spending Distribution plot, click the Download Gender Spending Plot button on the main page.
Conclusion
This application provides a simple way to collect survey data, analyze it visually, and export the results for further use. If you have any questions or feedback, feel free to open an issue in this repository.
