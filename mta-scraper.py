import datetime
import requests # Assuming you are making an API call using the requests library
import pandas as pd

def mta_outage_call_timestamp(url, headers =None):
    """
    Makes a call to the MTA elevator outage site, records the data, and saves a timestamp for the call

    """
    # Get the current timestamp before making the API call
    timestamp = datetime.datetime.now()

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()

        print(f"API call made at: {timestamp}")
        print(f"API response status: {response.status_code}")

        df = pd.json_normalize(data)
        df.to_csv(f'/Users/zoeslemmons/Desktop/MTA-elevators/outage_data/outages_{timestamp}.csv', index = False)

        return timestamp, data

        # You can also store the timestamp and other data (e.g., response content)
        # in a log file, database, or a data structure like a list of dictionaries.
        # Example:
        # log_entry = {"timestamp": timestamp.isoformat(), "url": url, "status_code": response.status_code}
        # with open("api_logs.txt", "a") as f:
        #     f.write(str(log_entry) + "\n")

    except requests.exceptions.RequestException as e:
        print(f"API call to {url} failed at: {timestamp} - Error: {e}")

url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene_equipments.json'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.mta.info',
    'priority': 'u=1, i',
    'referer': 'https://www.mta.info/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-api-key': 'UHbeYqoprP7N6LixCPVJN3TuZLAAEe0p6YxOPRJ2',
}

response = requests.get(
    'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene_equipments.json',
    headers=headers,
)

mta_outage_call_timestamp(url, headers)