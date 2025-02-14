# API Troubleshooting Guide

This guide provides troubleshooting solutions for common API issues, using an actual API response to illustrate potential errors. For reference, we are using OpenWeatherAPI.

---

# 1. 401 Unauthorized Errors
### Potential Causes
- **Invalid API Key**: The provided API key is incorrect or mistyped.
- **Missing API Key**: The request does not include an API key.
- **Expired API Key**: The API key is outdated or has been revoked.
- **IP Restriction**: The API key might be restricted to specific IP addresses.
- **Incorrect API Endpoint**: Using the wrong URL or an 
https://api.openweathermap.org/data/2.5/weather?q=Austin&appid=YOUR_API_KEY


✅ **Check API Key Permissions**  
- Some API keys require additional setup (e.g., premium features, rate limits).  
- Log in to the API provider portal and verify key permissions.  

✅ **Test with a New API Key**  
- Generate a new API key and test if the issue persists.  

✅ **Check for IP Restrictions**  
- Some APIs restrict access based on IP addresses. If using a VPN or proxy, disable it and retry.  

✅ **Inspect API Response**  
If the API returns:  
```json
{
"cod": 401,
"message": "Invalid API key"
}
```

The key is likely incorrect.

# 2. Slow API Response Times  
### Potential Causes  
- **High Server Load**: The API provider’s servers may be experiencing heavy traffic.  
- **Network Latency**: Slow internet connections or server location issues.  
- **Large Payloads**: Retrieving excessive or unnecessary data.  
- **Rate Limiting**: Exceeding API request limits causes throttling.  

### Solutions  
✅ **Check API Provider Status**  
- Visit OpenWeatherMap’s [status page](https://openweathermap.org/api/one-call-3#errorstructure) for maintenance alerts.  

✅ **Test with a Smaller Request**  
Instead of:  

https://api.openweathermap.org/data/2.5/weather?q=Austin&appid=YOUR_API_KEY&fields=name,temp,wind

- If applicable, use API parameters to limit response fields.  

✅ **Measure Response Time in Python**  
```python
import time
start_time = time.time()
response = requests.get(url)
end_time = time.time()
print(f"Response Time: {end_time - start_time} seconds")
```

✅ Implement Caching

Reduce API calls by storing responses locally.
Use tools like Redis or store data in a database.
✅ Contact API Provider

If slow responses persist, report the issue to the API provider.


# 3. Incorrect JSON Responses (Missing Fields)
### Potential Causes
- **API Changes**: The API provider may have updated the response format.
- **Incorrect Request Parameters**: Some required parameters might be missing.
- **Data Availability Issues**: Certain data points (e.g., `humidity`, `wind`) may be unavailable in specific locations.
- **Incorrect JSON Parsing**: The code might be incorrectly handling missing fields.

### Solutions
✅ **Validate API Response**  
Check the full API response for missing fields:  
```python
import json
print(json.dumps(response.json(), indent=2))

{
  "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds"}],
  "main": {"temp": 279.02, "humidity": 68},
  "wind": {"speed": 2.06},
  "name": "Austin"
}
```

If a field (e.g., "visibility") is missing, the API might not provide it for that location.

✅ Handle Missing Fields Gracefully
Modify the script to avoid KeyErrors:
data = response.json()
visibility = data.get("visibility", "Data not available")
pressure = data.get("main", {}).get("pressure", "Data not available")

✅ Check API Documentation for Changes

Visit OpenWeatherMap’s API documentation to confirm field availability.
✅ Ensure Correct Request Parameters

Some API fields require additional query parameters. Example:
https://api.openweathermap.org/data/2.5/weather?q=Austin&appid=YOUR_API_KEY&units=metric

Adding units=metric ensures temperature is returned in Celsius instead of Kelvin.

✅ Contact API Support

If the missing field is critical and should be present, report it to OpenWeatherMap.

For more details, visit OpenWeatherMap API Documentation here https://openweathermap.org/api/one-call-3#errorstructure