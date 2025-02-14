import pandas as pd
import requests

## Historical market data for the ticket AAPL is in the following API
# I have used below API for data, as the provided API in the excercise pdf was not working
url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history?symbol=AAPL&interval=5m&diffandsplits=false"

headers = {
    "X-RapidAPI-Key": "Use your API Key",
    "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

## Get JSON responce
response = requests.get(url, headers=headers)

## Check if there are any errors in accessing the API
if response.status_code == 200:
    data = response.json()
    print("Data id Fetched!! Hoorray")

    #print("Top-level keys:", list(data.keys()))

    # Extract the second key dynamically
    second_key = list(data.keys())[1]  # Get the second key
    second_body = data[second_key]  # Extract its body (assumes it's a dictionary or list)
    
    # Convert the extracted data into a Pandas DataFrame
    df = pd.DataFrame(second_body)

    # If rows and columns are flipped, transpose the DataFrame
    if isinstance(second_body, dict):  # Check if it's a dictionary
        df = df.T  # Transpose to swap rows and columns

    # Display the last 10 rows of the DataFrame
    print(df.tail(10))

else:
    print("Failed to fetch data")
