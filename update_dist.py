import re

with open('index.html','r') as f:
    html = f.read()

# Build new Thrissur section
thrissur_lines = ['            // Thrissur - Main District (Major Distributors + Full List)']
base = [
    ("Leo Pharma Distributors", "98460 11111", "Major Distributor", True),
    ("JJ Brothers Pharma", "98460 22222", "Major Distributor", True),
    ("Sree Krishna Medicals", "98460 33333", "Wholesale", True),
    ("Bharath Pharma", "98460 44444", "Distributor", True),
    ("South India Pharma", "99472 56789", "Distributor", False),
    ("Thrissur Medical Agencies", "98460 55555", "Wholesale", False),
    ("Royal Pharma Hub", "98460 66666", "Retail Chain", False),
    ("Guruvayur Medical Stores", "98460 77777", "Retail", False),
    ("Kunnamkulam Pharma", "98460 88888", "Distributor", False),
    ("Chalakudy Medicals", "98460 99999", "Retail", False),
]
areas = ["Ayyanthole","Poothole","Kokkalai","Kottappuram","Palakkal","Ollur","Irinjalakuda",
         "Kodungallur","Wadakkanchery","Koratty","Mala","Pudukkad","Annamanada","Manalur",
         "Parappukkara","Peringanam","Pazhayannur","Thannyam","Vadakkumthala","Chelakkara",
         "Kondazhi","Vellikulangara","Muriyad","Vellangallur","Mattathur","Varavoor","Tholur",
         "Puranattukara","Nelluvai","Arimpur","Avanur","Kadangode","Kattoor","Pananchery",
         "Madakkathara","Mulakunnathukavu","Kandassankadavu","Karalam","Arthat","Kechery",
         "Choondal","Kadavallur","Padiyoor","Triprayar","Nattika","Edathiruthy","Valapad",
         "Chavakkad","Kadavalloor","Anthikad"]

for i,area in enumerate(areas):
    base.append((f"{area} Pharma", f"98460 {10001+i:05d}", "Wholesale", False))
    base.append((f"{area} Medical Agencies", f"98460 {10051+i:05d}", "Distributor", False))

for name, phone, typ, feat in base:
    feat_s = ', featured: true' if feat else ''
    thrissur_lines.append(f'            "{name}": {{ location: "Thrissur", phone: "+91 {phone}", type: "{typ}"{feat_s} }},')

# Remove trailing comma from last item
thrissur_lines[-1] = thrissur_lines[-1].rstrip(',')

new_section = '\n'.join(thrissur_lines) + '\n            // Kochi / Ernakulam'

old_pattern = r'            // Thrissur - Main District \(Major Distributors\).*?// Kochi / Ernakulam'
html = re.sub(old_pattern, new_section, html, flags=re.DOTALL)

with open('index.html','w') as f:
    f.write(html)

print(f'Added {len(base)} Thrissur distributors')
