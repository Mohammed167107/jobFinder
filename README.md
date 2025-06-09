# jobFinder

This Python script allows you to search for job listings near a specific location using the HigherMe API. It first converts a location (postal code or city name) to geographic coordinates, then fetches nearby job listings based on those coordinates.

Features
Convert locations to latitude/longitude coordinates

Search for jobs within a specified distance (in miles)

Save job listings to a CSV file

Works with postal codes or city names

Designed for Canadian locations (can be modified for other countries)

Requirements
Python 3.x

Required Python packages:

bash
pip install requests pandas pgeocode
How to Use
Set your location parameters:

Modify the country, postal_code, and place_name variables at the bottom of the script

Set the search distance (in miles) in the get_jobs() call

Run the script:

bash
python job_finder.py
Check the output:

Job listings will be saved to jobs.csv in your current directory

Coordinates will be printed in the console

Functions
get_lat_lon(country_code, postal_code=None, place_name=None)
Converts a location to geographic coordinates.

Parameters:

country_code: ISO country code (e.g., "CA" for Canada)

postal_code: Postal code (optional)

place_name: City name (optional)

Returns: Tuple (latitude, longitude)

get_jobs(lat, lng, distance=20)
Fetches job listings near specified coordinates.

Parameters:

lat: Latitude

lng: Longitude

distance: Search radius in miles (default: 20)

Output: Saves results to jobs.csv with columns:

id: Job ID

title: Job title

location: City and postal code

company: Company name

summary: Job description

Example Usage
python
# Get coordinates for Toronto
lat, lon = get_lat_lon("CA", place_name="Toronto")
print(f"Coordinates: ({lat}, {lon})")

# Search for jobs within 5 miles
get_jobs(lat, lon, 5)
Sample Output (jobs.csv)
id	title	location	company	summary
abc123	Shift Manager	Toronto, M5V 2T6	Restaurant Co	Manage daily operations...
xyz789	Barista	Toronto, M5V 2Z4	Coffee Shop	Prepare coffee drinks...
Notes
The script is currently configured to search for jobs at brand ID 58bd9e7f472bd (Tim Hortons Canada). To search for other brands:

Update the filters[brand.id] parameter in the URL

Modify the brand.id value in both the URL and querystring

For use outside Canada:

Change the country code in get_lat_lon() calls

Verify API supports your target region

The headers contain browser-specific information that might need periodic updating to mimic a real browser

Troubleshooting
No results? Try increasing the search distance

Coordinate errors? Verify your location names with official postal codes

API errors? Check if headers need updating (particularly user-agent and higherme-client-version)
