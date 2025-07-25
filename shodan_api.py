from shodan import Shodan, exception
from dotenv import load_dotenv
import os

load_dotenv()  

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

def get_shodan_info(ip):
    if not SHODAN_API_KEY:
        return "Shodan API key not found"
    
    try:
        # Initialize Shodan API
        api = Shodan(SHODAN_API_KEY)
        host = api.host(ip)
        
        # Format the response nicely
        info = []
        info.append(f"IP: {host.get('ip_str', 'N/A')}")
        info.append(f"Organization: {host.get('org', 'N/A')}")
        info.append(f"ISP: {host.get('isp', 'N/A')}")
        info.append(f"Country: {host.get('country_name', 'N/A')}")
        info.append(f"City: {host.get('city', 'N/A')}")
        info.append(f"Ports: {', '.join(map(str, host.get('ports', [])))}")
        
        # Add service information
        if 'data' in host and host['data']:
            services = []
            for item in host['data'][:3]:  # Limit to first 3 services
                port = item.get('port', 'Unknown')
                product = item.get('product', 'Unknown')
                services.append(f"Port {port}: {product}")
            if services:
                info.append(f"Services: {'; '.join(services)}")
        
        return "\n".join(info)
        
  
    except Exception as e:
        return f"Shodan Error {e}"