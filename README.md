
# 🕵️ CyberScope — Cybersecurity Investigation Bot  
**Author: Ramy Garici**

CyberScope is an automated cybersecurity investigation tool written in Python.  
Given a domain name or IP address, it performs multiple reconnaissance steps and generates a detailed PDF report with the findings.

---

## 🚀 Features

- 🔎 Domain resolution (get IP from a domain)
- 🧠 WHOIS data lookup
- 🛡️ VirusTotal reputation check
- 🧱 Port scanning (common ports)
- 🛰️ Shodan integration *(currently not functioning — see note below)*
- 📄 PDF report generation

---

## ⚙️ Technologies Used

- Python 3.x
- `socket`
- `python-whois`
- VirusTotal API
- Shodan API
- `fpdf`

---

## 📁 Project Structure

```
cyber-scope/
├── main.py                # Main execution script
├── utils.py               # Resolve domain
├── report_generator.py    # PDF generation
├── scanner.py             # Port scan<<<<<<< HEAD
├── scanner.py             # Port scan logic
├── virus_total.py         # VirusTotal lookup
├── shodan_api.py          # Shodan data fetch
├── who_is.py              # WHOIS lookup
=======
├── scanner.py             # Port scan
├── virus_total.py         # VirusTotal lookup
├── shodan_api.py          # Shodan data fetch
├── who_is.py              # whois
├── who_is.py              # whois
>>>>>>> 9d927df21966b4fee72343ce814a82310d388fbd
├── .env                   # Contains API keys (DO NOT SHARE)
└── README.md              # This file
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root to store your API keys:

```env
VT_API_KEY=your_virustotal_api_key
SHODAN_API_KEY=your_shodan_api_key
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the tool:

```bash
python main.py
```

---

## ⚠️ Note about Shodan

Shodan integration is currently not working due to issues with the free API tier or local network restrictions.  
All other features (VirusTotal, WHOIS, port scanning) work correctly.

---

## 🧪 Coming Soon

A front-end interface  is planned to make the tool more user-friendly and accessible.
