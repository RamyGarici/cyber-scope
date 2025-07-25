import whois
from datetime import datetime

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        
        # Format the whois information into a readable string
        if domain_info:
            info_lines = []
            
            # Extract key information
            if hasattr(domain_info, 'domain_name') and domain_info.domain_name:
                domain_name = domain_info.domain_name
                if isinstance(domain_name, list):
                    domain_name = domain_name[0]
                info_lines.append(f"Domain: {domain_name}")
            
            if hasattr(domain_info, 'registrar') and domain_info.registrar:
                info_lines.append(f"Registrar: {domain_info.registrar}")
            
            # Format dates properly
            if hasattr(domain_info, 'creation_date') and domain_info.creation_date:
                creation_date = domain_info.creation_date
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                if isinstance(creation_date, datetime):
                    creation_date = creation_date.strftime("%Y-%m-%d")
                info_lines.append(f"Created: {creation_date}")
            
            if hasattr(domain_info, 'expiration_date') and domain_info.expiration_date:
                expiration_date = domain_info.expiration_date
                if isinstance(expiration_date, list):
                    expiration_date = expiration_date[0]
                if isinstance(expiration_date, datetime):
                    expiration_date = expiration_date.strftime("%Y-%m-%d")
                info_lines.append(f"Expires: {expiration_date}")
            
            if hasattr(domain_info, 'updated_date') and domain_info.updated_date:
                updated_date = domain_info.updated_date
                if isinstance(updated_date, list):
                    updated_date = updated_date[0]
                if isinstance(updated_date, datetime):
                    updated_date = updated_date.strftime("%Y-%m-%d")
                info_lines.append(f"Updated: {updated_date}")
            
            if hasattr(domain_info, 'org') and domain_info.org:
                info_lines.append(f"Organization: {domain_info.org}")
            
            if hasattr(domain_info, 'country') and domain_info.country:
                info_lines.append(f"Country: {domain_info.country}")
            
            # Format status information
            if hasattr(domain_info, 'status') and domain_info.status:
                status = domain_info.status
                if isinstance(status, list):
                    # Take only first 3 status entries to avoid clutter
                    status = status[:3]
                    status_str = "; ".join([s.split()[0] for s in status])
                    info_lines.append(f"Status: {status_str}")
                else:
                    info_lines.append(f"Status: {status}")
            
            return "\n".join(info_lines) if info_lines else "No WHOIS information available"
        else:
            return "No WHOIS information available"
            
    except Exception as e:
        return f"Error retrieving WHOIS info for {domain}: {e}"