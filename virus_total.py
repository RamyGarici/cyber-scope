import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis .env

VT_API_KEY = os.getenv("VT_API_KEY")


def check_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_API_KEY}
    try:
        resp = requests.get(url, headers=headers)
        data = resp.json()
        return data['data']['attributes']['last_analysis_stats']
    except Exception as e:
        return f"VirusTotal Error {e}"
