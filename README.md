# HealthMap Finder

HealthMap Finder is a web application designed to help users find healthcare facilities based on their location and specific health conditions. The application provides personalized hospital recommendations and detailed information about each facility.

## Features

- Search for hospitals based on location and health conditions.
- View detailed hospital information, including performance ratings and statistics.
- Use geolocation to find nearby healthcare facilities.
- Responsive UI with a user-friendly interface.

## Technologies Used

- *Frontend*: React, TypeScript, Tailwind CSS
- *Backend*: Flask, Pandas, Geopy
- *Database*: CSV file for hospital data
- *APIs*: Custom API endpoints for searching locations and conditions

## Prerequisites

- Node.js and npm
- Python 3.x
- Flask
- Pandas
- Geopy

## Setup Instructions

### Frontend

1. Navigate to the healthmap-finder directory:
   bash
   cd healthmap-finder
   

2. Install the dependencies:
   bash
   npm install
   

3. Start the development server:
   bash
   npm run dev
   

### Backend

1. Navigate to the healthmapfinderflask directory:
   bash
   cd healthmapfinderflask
   

2. Create a virtual environment:
   bash
   python -m venv venv
   

3. Activate the virtual environment:

   - On Windows:
     bash
     venv\Scripts\activate
     

   - On macOS/Linux:
     bash
     source venv/bin/activate
     

4. Install the required Python packages:
   bash
   pip install -r req.txt
   

5. Run the Flask application:
   bash
   python app.py
   

## Usage

- Access the frontend application at http://localhost:5173.
- Use the search form to enter your location and health condition.
- View the list of recommended hospitals and their details.

## API Endpoints

- *GET /api/locations/search*: Search for locations based on a query.
- *GET /api/hospitals/search*: Search for hospitals based on location and health conditions.
- *GET /api/conditions/search*: Search for health conditions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.



















http://127.0.0.1:5000/api/update    ------------>To update the information


'/api/update_data'                 -------------->To update the information through API (Postman)






{
    "Facility ID": "010002",
    "Facility Name": "NORTHWEST MEDICAL CENTER",
    "Address": "1234 MEDICAL DRIVE",
    "City/Town": "TUSCALOOSA",
    "State": "AL",
    "ZIP Code": "35401",
    "County/Parish": "TUSCALOOSA",
    "Telephone Number": "(205) 555-1234",
    "Measure ID": "COMP_HIP_KNEE",
    "Measure Name": "Rate of complications for hip/knee replacement patients",
    "Compared to National": "No Different Than the National Rate",
    "Denominator": 45,
    "Score": 4.2,
    "Lower Estimate": 2.1,
    "Higher Estimate": 6.3,
    "Footnote": "",
    "Start Date": "2020-07-01",
    "End Date": "2023-03-31"
}



--------------------------------------------------------------------------------------



{
    "Facility ID": "050123",
    "Facility Name": "CEDARS-SINAI MEDICAL CENTER",
    "Address": "8700 BEVERLY BLVD",
    "City/Town": "LOS ANGELES",
    "State": "CA",
    "ZIP Code": "90048",
    "County/Parish": "LOS ANGELES",
    "Telephone Number": "(310) 423-3277",
    "Measure ID": "COMP_HIP_KNEE",
    "Measure Name": "Rate of complications for hip/knee replacement patients",
    "Compared to National": "Better Than the National Rate",
    "Denominator": 120,
    "Score": 2.8,
    "Lower Estimate": 1.5,
    "Higher Estimate": 4.1,
    "Footnote": "",
    "Start Date": "2020-07-01",
    "End Date": "2023-03-31"
}

