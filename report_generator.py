from fpdf import FPDF

def generate_pdf(domain, ip, whois_info, open_ports, vt_info, shodan_info):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Titre
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt=f"Security report : {domain}", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"IP address : {ip}", ln=True)
    pdf.ln(5)

 
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Open Ports :", ln=True)
    pdf.set_font("Arial", size=12)
    ports_text = ', '.join(str(p) for p in open_ports) if open_ports else "No open port detected."
    pdf.multi_cell(0, 10, ports_text)
    pdf.ln(3)

    # VirusTotal
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "VirusTotal Results :", ln=True)
    pdf.set_font("Arial", size=12)
    vt_text = str(vt_info) if vt_info is not None else "No VirusTotal information available"
    pdf.multi_cell(0, 10, vt_text)
    pdf.ln(3)

    # Shodan
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Shodan Data :", ln=True)
    pdf.set_font("Arial", size=12)
    shodan_text = str(shodan_info) if shodan_info is not None else "No Shodan information available"
    pdf.multi_cell(0, 10, shodan_text)
    pdf.ln(3)

    # WHOIS
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Infos WHOIS :", ln=True)
    pdf.set_font("Arial", size=12)
    whois_text = str(whois_info) if whois_info is not None else "No WHOIS information available"
    pdf.multi_cell(0, 10, whois_text)
    pdf.ln(3)

    # Sauvegarde
    filename = f"report_{domain.replace('.', '_')}.pdf"
    pdf.output(filename)
    print(f"Report Saved As : {filename}")