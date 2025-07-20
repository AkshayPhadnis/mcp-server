import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_salesforce_token():
    url = os.getenv("SF_AUTH_URL")
    params = {
        "grant_type": "password",
        "client_id": os.getenv("SF_CLIENT_ID"),
        "client_secret": os.getenv("SF_CLIENT_SECRET"),
        "username": os.getenv("SF_USERNAME"),
        "password": os.getenv("SF_PASSWORD") + os.getenv("SF_SECURITY_TOKEN")
    }

    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()["access_token"], response.json()["instance_url"]
    else:
        raise Exception(f"Token error: {response.text}")

def get_salesforce_data(user_message):
    try:
        access_token, instance_url = get_salesforce_token()
        query = "SELECT Name, StageName FROM Opportunity LIMIT 5"
        url = f"{instance_url}/services/data/v59.0/query"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers, params={"q": query})
        if response.status_code == 200:
            records = response.json()["records"]
            return [f"{r['Name']} - {r['StageName']}" for r in records]
        else:
            return f"Error: {response.text}"

        return {"account_name": "Acme Corp"}
    except Exception as e:
        return f"Salesforce error: {e}"
