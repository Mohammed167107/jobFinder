import requests
import pandas as pd
import json
import pgeocode


def get_jobs(lat,lng, distance=20):
    url = f"https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]={distance}&sort[distance]=asc"

    querystring = {"page":"1","includes":"location,location.company,location.externalServiceReferences","limit":"20","filters[brand.id]":"58bd9e7f472bd"}

    payload = "page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd"
    headers = {
        "^accept": "application/json, text/plain, */*^",
        "^accept-language": "en-GB,en;q=0.7^",
        "^higherme-client-version": "2025.06.04_20.0^",
        "^origin": "https://app.higherme.com^",
        "^priority": "u=1, i^",
        "^sec-ch-ua": "^\^Brave^^;v=^\^137^^, ^\^Chromium^^;v=^\^137^^, ^\^Not/ABrand^^;v=^\^24^^^",
        "^sec-ch-ua-mobile": "?0^",
        "^sec-ch-ua-platform": "^\^Windows^^^",
        "^sec-fetch-dest": "empty^",
        "^sec-fetch-mode": "cors^",
        "^sec-fetch-site": "same-site^",
        "^sec-gpc": "1^",
        "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36^",
        "Content-Type": "application/json"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    #print(response.text)

    data= response.json()
    data= data['data']
    #print(data)
    jobs = []
    location=""
    for job in data:
        city =job["relations"].get("location")["attributes"].get("city")
        postalCode = job["relations"].get("location")["attributes"].get("zipcode")
        location = f" city: {city}, postalCode: {postalCode}"
        job_info = {
            "id": job.get("id"),
            "title": job["attributes"].get("title"),
            "location": location,
            "company": job.get("relations", {}).get("location").get("relations").get("company", {}).get("attributes").get("name"),
            "summary": job.get("attributes", {}).get("summary_no_html", [])
        }
        jobs.append(job_info)
    #print(jobs)
    p=pd.DataFrame(jobs)
    p.to_csv('jobs.csv', index=False)
#print(response.json())

def get_lat_lon(country_code, postal_code=None, place_name=None):
    """
    Get latitude and longitude for a postal code or place name.
    
    Args:
        country_code (str): ISO 3166-1 alpha-2 country code (e.g., "US", "FR").
        postal_code (str, optional): Postal/ZIP code.
        place_name (str, optional): Name of a place (city, town, etc.).
    
    Returns:
        tuple: (latitude, longitude) or (None, None) if not found.
    """
    nomi = pgeocode.Nominatim(country_code)
    
    # Query by postal code (preferred)
    if postal_code:
        result = nomi.query_postal_code(postal_code)
        if not pd.isna(result.latitude) and not pd.isna(result.longitude):
            return (result.latitude, result.longitude)
    
    # Query by place name (fallback)
    if place_name:
        df = nomi.query_location(place_name)
        if not df.empty:
            # Filter valid coordinates and sort by accuracy (descending)
            valid_df = df.dropna(subset=['latitude', 'longitude'])
            if not valid_df.empty:
                valid_df = valid_df.sort_values(by='accuracy', ascending=False)
                best_match = valid_df.iloc[0]
                return (best_match.latitude, best_match.longitude)
    
    return (None, None)  # Not found

# Example Usage:
country = "CA"
postal_code = ""  # Beverly Hills ZIP code
place_name = "Toronto"  # Example

# Get coordinates for postal code
#lat, lon = get_lat_lon(country, postal_code=postal_code)
#print(f"Coordinates for {postal_code}: ({lat}, {lon})")

# Get coordinates for place name
lat, lon = get_lat_lon(country, place_name=place_name)
print(f"Coordinates for {place_name}: ({lat}, {lon})")
get_jobs(lat, lon,5)