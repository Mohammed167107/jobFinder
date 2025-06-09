# Job Finder Script

This Python script allows you to search for job listings near a specific location using the HigherMe API. It first converts a location (postal code or city name) to geographic coordinates, then fetches nearby job listings based on those coordinates.

## Features
- Convert locations to latitude/longitude coordinates
- Search for jobs within a specified distance (in miles)
- Save job listings to a CSV file
- Works with postal codes or city names
- Designed for Canadian locations (modifiable for other countries)

## Requirements
- Python 3.x
- Required packages:
  ```bash
  pip install requests pandas pgeocode

## Installation
-Download the script or clone the repository
-Install required dependencies:
--pip install requests pandas pgeocode

### Location parameters
-country = "CA"  # ISO country code (e.g., "US" or "CA")
-postal_code = ""  # Enter postal code (e.g., "M5V 2T6")
-place_name = "Toronto"  # Enter city name if no postal code

-Search parameters
-distance = 5  # Search radius in miles

-Run the script:
--python job_finder.py
-Find results in jobs.csv in your current directory

## Functions
-get_lat_lon(country_code, postal_code=None, place_name=None)
-Converts a location to geographic coordinates using pgeocode.

-Parameters
--country_code (str): ISO 3166-1 alpha-2 country code (e.g., "CA", "US")
--postal_code (str, optional): Postal/ZIP code
--place_name (str, optional): Name of a place (city, town, etc.)
--Returns: Tuple (latitude, longitude) or (None, None) if not found

-Behavior:
--Prioritizes postal codes for more accurate results

--Falls back to place name search if postal code not provided or invalid

--Selects best match based on GeoNames accuracy score

--get_jobs(lat, lng, distance=20)
--Fetches job listings from HigherMe API near specified coordinates.

## Parameters
-lat (float): Latitude coordinate
-lng (float): Longitude coordinate
-distance (int): Search radius in miles (default: 20)

## Workflow
-Constructs API request with proper headers and parameters
-Processes JSON response into structured job data

## Extracts
-Job ID
-Job title
-Location (city + postal code)
-Company name
-Job summary (HTML-free)
-Saves results to CSV file (jobs.csv)

## API Endpoint
-https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]={distance}&sort[distance]=asc

## Sample Output
-Console Output
--Coordinates for Toronto: (43.6532, -79.3832)
-jobs.csv

id,title,location,company,summary
abc123,Shift Manager,"city: Toronto, postalCode: M5V 2T6",Tim Hortons,"Manage daily operations, staff scheduling..."
def456,Barista,"city: Toronto, postalCode: M5V 2Z4",Tim Hortons,"Prepare beverages, maintain clean workspace..."

## Troubleshooting
  Issue	                        Solution
No jobs found	            Increase distance value
                          Verify coordinates are valid
                          
Coordinate errors	        Check postal code format 
                          Try nearby city name instead  
                          
API returns 403 error	    Update headers (especially user-agent and higherme-client-version)

Missing company names	    Check if API structure changed
                          Add error handling for missing keys
                          
Canadian locations only	   Change country code to "US" and use ZIP codes

