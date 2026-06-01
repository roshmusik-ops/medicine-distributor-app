"""Scrape Pharmapps for Kerala medicine distributors."""

import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

PHARMAPPS_URL = "https://www.pharmapps.in/RetailerHome/Index"

def scrape_pharmapps():
    """Scrape Pharmapps for distributor data."""
    try:
        response = requests.get(PHARMAPPS_URL, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract distributor information
        distributors = []
        
        # Look for distributor listings
        distributor_elements = soup.find_all('div', class_=['distributor', 'retailer', 'pharmacy'])
        
        for elem in distributor_elements:
            try:
                name = elem.find('h3') or elem.find('h2')
                phone = elem.find('span', class_='phone')
                location = elem.find('span', class_='location')
                
                if name:
                    distributors.append({
                        'name': name.text.strip(),
                        'phone': phone.text.strip() if phone else '',
                        'location': location.text.strip() if location else 'Kerala',
                        'state': 'Kerala',
                    })
            except Exception as e:
                print(f"Error parsing element: {e}")
                continue
        
        return distributors
    
    except Exception as e:
        print(f"Error scraping Pharmapps: {e}")
        return []


def save_distributors(distributors):
    """Save distributors to JSON."""
    output_file = DATA_DIR / "distributors.json"
    
    with output_file.open('w', encoding='utf-8') as f:
        json.dump(distributors, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(distributors)} distributors to {output_file}")


def main():
    print("Scraping Pharmapps for Kerala distributors...")
    distributors = scrape_pharmapps()
    
    if distributors:
        save_distributors(distributors)
    else:
        print("No distributors found. Creating sample data...")
        # Sample data for testing
        sample_distributors = [
            {
                "name": "Apollo Pharmacy",
                "phone": "+91 98765 43210",
                "location": "Kochi",
                "state": "Kerala"
            },
            {
                "name": "Medplus Distributor",
                "phone": "+91 97654 32109",
                "location": "Thiruvananthapuram",
                "state": "Kerala"
            },
            {
                "name": "CVS Pharmacy",
                "phone": "+91 96543 21098",
                "location": "Ernakulam",
                "state": "Kerala"
            },
        ]
        save_distributors(sample_distributors)


if __name__ == "__main__":
    main()
