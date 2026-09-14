Python API, SQLite & Data Processing Assignment
Overview

This repository contains the implementation of three Python-based tasks involving REST API data retrieval, SQLite database operations, data processing, visualization, and CSV data import.

The assignment demonstrates practical use of Python for working with external APIs, databases, structured datasets, and data visualization.

Problem Statements 1
1 — API Data Retrieval and Storage

The objective is to fetch book data from an external REST API, store the retrieved data in a local SQLite database, and display the stored information.

Key Operations
Send a request to an external REST API
Retrieve book information in JSON format
Extract relevant attributes such as:
Book title
Author
Publication year
Create a local SQLite database
Store the API data in a database table
Retrieve and display the stored records
Technologies Used
Python
Requests
REST API
JSON
SQLite
 2 — Data Processing and Visualization

The objective is to retrieve student test-score data from an API, process the data, calculate the average score, and visualize the results using a bar chart.

Key Operations
Fetch student score data from an API
Parse the JSON response
Process the student scores
Calculate the average score
Display the calculated result
Generate a bar chart for visualization
Technologies Used
Python
Requests
Pandas
Matplotlib
REST API
JSON
Visualization

The generated bar chart is saved as:

student_scores.png

 3 — CSV Data Import to SQLite

The objective is to read user information from a CSV file and insert the records into a local SQLite database.

Key Operations
Read data from a CSV file
Extract user information such as:
Name
Email
Create a SQLite database
Create the required database table
Insert CSV records into the database
Retrieve and verify the inserted records
Technologies Used
Python
CSV
SQLite
