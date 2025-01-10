import json
import requests
import datetime
from flask import Flask, render_template, request, jsonify
import pandas as pd
import base64
from io import BytesIO
from os import getenv
import pathlib
import os
from fuzzywuzzy import process

# Set up environment variables
# from dotenv import load_dotenv

# load_dotenv()

# Get the current working directory

# Dynamically get the base directory of the script
base_dir = os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'Capstone-Project-Final', 'Dataset'))

# Construct the dataset path
dataset_path = os.path.join(base_dir, 'Hospital inmoratlity.csv')

print(dataset_path)


app = Flask(__name__)
from flask_cors import CORS
CORS(app)

# hospitals = [
#     {"id": "1", "name": "General Hospital", "rating": 4.5, "specialty": "General Medicine", "distance": "2.5 miles", "address": "123 Healthcare Ave"},
#     {"id": "2", "name": "City Medical Center", "rating": 4.8, "specialty": "Emergency Care", "distance": "3.1 miles", "address": "456 Wellness Blvd"},
#     {"id": "3", "name": "Community Health Hospital", "rating": 4.2, "specialty": "Family Medicine", "distance": "1.8 miles", "address": "789 Care Street"},
# ]

dataset = pd.read_csv(dataset_path)
# print(dataset)
def get_suggestions(location, measure_name, top_n=5):
    # Filter by location
    location_filtered = dataset[dataset['City'].str.contains(location, case=False, na=False)]
    
    if location_filtered.empty:
        return []
    
    # Get approximate matches for Measure Name
    measure_names = location_filtered['Measure Name'].tolist()
    matched_measures = process.extract(measure_name, measure_names, limit=top_n)
    
    # Prepare results in desired format
    results = []
    for match, score in matched_measures:
        matching_row = location_filtered[location_filtered['Measure Name'] == match].iloc[0]
        results.append({
            "id": str(matching_row["Provider ID"]),
            "name": matching_row["Hospital Name"],
            "rating": round(matching_row["Score"], 1),  # Example rating, can modify based on data
            "specialty": match,
            "distance": "Unknown",  # Placeholder, replace with actual data if available
            "address": matching_row["Address"]
        })
    
    return results

@app.route('/api/hospitals/search', methods=['GET'])
def search_hospitals():
    location = request.args.get('location', '')
    health_issue = request.args.get('healthIssue', '')
    
    if not location or not health_issue:
        return jsonify({"error": "Location and health issue are required."}), 400
    
    suggestions = get_suggestions(location, health_issue)

    
    if not suggestions:
        return jsonify({"message": "No suggestions found for the given input."}), 404
    
    return jsonify(suggestions), 200

@app.route('/api/patients/register', methods=['POST'])
def register_patient():
    data = request.json
    data['id'] = "generated-id"  # Simulate generating a unique ID
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)