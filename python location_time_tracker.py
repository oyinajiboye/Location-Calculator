import json
import requests
from datetime import datetime, timedelta

# Define function to calculate days in location
def calculate_days_in_location(location_data, location_name, start_date, end_date, api_key):
    # Initialize variables
    total_time = timedelta()
    location_name = location_name.lower()

    # Loop through location data
    for entry in location_data:
        # Get date and coordinates from entry
        date_str = entry["dateAsString"]
        lat = entry['latitude']
        lon = entry['longitude']

        # Skip entry if date is outside date range
        date = datetime.strptime(date_str, '%d-%m-%Y')
        if date < start_date or date > end_date:
            continue

        # Get location name from coordinates using Geocoding API
        url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}'
        response = requests.get(url).json()
    if response['status'] == 'OK':
        return response['results'][0]['formatted_address']
    else:
        return None

        # Add time to total if location matches
        if location_name in formatted_address:
            time = timedelta(hours=entry['hour'], minutes=entry['minute'], seconds=entry['second'])
            total_time += time

    # Return total time spent in location
    return total_time


# Define main function
def main():
    # Load location data from JSON file
    with open('location_data.json', 'r') as f:
        location_data = json.load(f)

    # Get user input for location name, start date, and end date
    location_name = input('Enter a location name: ')
    start_date_str = input('Enter the start date (YYYY-MM-DD): ')
    end_date_str = input('Enter the end date (YYYY-MM-DD): ')
    api_key = input('Enter your Google Maps API key: ')

    # Parse date strings into datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # Calculate days in location
    days_in_location = calculate_days_in_location(location_data, location_name, start_date, end_date, api_key)

    # Print result
    print(f"You spent a total of {days_in_location} in {location_name} between {start_date_str} and {end_date_str}.")


# Call main function
if __name__ == '__main__':
    main()

