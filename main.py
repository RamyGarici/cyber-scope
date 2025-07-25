from utils import resolve_domain
from who_is import get_whois_info
from scanner import scan_ports
from virus_total import check_ip
from shodan_api import get_shodan_info
from report_generator import generate_pdf


domain = input("Enter a domain name:\n").strip()
ip = resolve_domain(domain)
print(f"IP: {ip}")

# Pass domain to WHOIS (not IP)
whois_info = get_whois_info(domain)
open_ports = scan_ports(ip)
vt_info = check_ip(ip)
# shodan_info = get_shodan_info(ip)

generate_pdf(domain, ip, whois_info, open_ports, vt_info, None) 
print("Report generated successfully.")