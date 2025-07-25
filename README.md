🕵️ CyberScope — Cybersecurity Investigation Bot
Author: Ramy Garici

CyberScope is an automated cybersecurity investigation tool written in Python. Given a domain name or IP address, it performs multiple reconnaissance steps and generates a detailed PDF report with the findings.

🚀 Features
🔎 Domain resolution (get IP from a domain)

🧠 WHOIS data lookup

🛡️ VirusTotal reputation check

🧱 Port scanning (common ports)

🛰️ Shodan integration (currently not functioning — see note below)

📄 PDF report generation

⚙️ Technologies Used
Python 3.x

socket

python-whois

VirusTotal API

Shodan API

fpdf

📁 Project Structure
bash
Copier
Modifier
cyber-scope/
├── main.py                # Main execution script
├── report_generator.py    # PDF generation
├── scanner.py             # Port scan
├── virus_total.py         # VirusTotal lookup
├── shodan_api.py          # Shodan data fetch
├── who_is.py              # whois
├── who_is.py              # whois
├── .env                   # Contains API keys (DO NOT SHARE)
└── README.md              # This file
🔐 Environment Setup
Create a .env file in the project root to store your API keys:

env
Copier
Modifier
VT_API_KEY=your_virustotal_api_key
SHODAN_API_KEY=your_shodan_api_key
Install required packages:

bash
Copier
Modifier
pip install -r requirements.txt
Run the tool:

bash
Copier
Modifier
python main.py
⚠️ Note about Shodan
Shodan integration is currently not working due to issues with the free API or network restrictions. All other features (VirusTotal, WHOIS, port scanning) work properly.

🧪 Coming Soon
A front-end interface  is planned to make the tool more user-friendly and accessible.
