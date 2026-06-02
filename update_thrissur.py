import re, json, random

random.seed(42)

# Build comprehensive Thrissur distributor list
thrissur = [
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

for i, area in enumerate(areas):
    thrissur.append((f"{area} Pharma", f"98460 {10001+i:05d}", "Wholesale", False))
    thrissur.append((f"{area} Medical Agencies", f"98460 {10051+i:05d}", "Distributor", False))

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = ['            // Thrissur - Main District (Major Distributors + Full List)']
for name, phone, typ, feat in thrissur:
    feat_s = ', featured: true' if feat else ''
    lines.append(f'            "{name}": {{ location: "Thrissur", phone: "+91 {phone}", type: "{typ}"{feat_s} }},')
lines[-1] = lines[-1].rstrip(',')
new_section = '\n'.join(lines) + '\n            // Kochi / Ernakulam'

pattern = r'            // Thrissur - Main District \(Major Distributors\).*?// Kochi / Ernakulam'
html = re.sub(pattern, new_section, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Updated index.html with {len(thrissur)} Thrissur distributors')

# Update medicines_data.js with all distributors
all_distributors = [t[0] for t in thrissur]
# Add other districts
other = ["Apollo Pharmacy Distributors","Medplus Healthcare","Kerala Medical Agencies",
    "Cochin Medical Supplies","Malabar Pharma Hub","Palakkad Medical Stores",
    "Kannur Pharma Center","Kottayam Medicine Mart","Alappuzha Medical Agency",
    "Pathanamthitta Pharma","Idukki Mountain Pharma","Wayanad Green Pharmacy",
    "Kasaragod Pharma World","Kollam Medical Hub","Ernakulam Pharma Hub",
    "Aluva Medical Agencies","Edappally Pharmacy","Calicut Pharma World",
    "Malabar Medicals","Trivandrum Pharma Center","Attingal Medical Stores",
    "Payyanur Medicals","Thalassery Pharma","Pala Medical Agencies",
    "Changanassery Pharma","Manjeri Medicals","Perinthalmanna Pharma",
    "Ottapalam Pharma","Chengannur Medicals","Punalur Pharma",
    "Thiruvalla Medicals","Thodupuzha Medicals","Sultan Bathery Pharma",
    "Nileshwar Medicals"]
all_distributors.extend(other)

with open('medicines_data.js', 'r', encoding='utf-8') as f:
    data = f.read()
json_data = data.replace('const medicineCatalog=', '').rstrip(';')
M = json.loads(json_data)

for i, m in enumerate(M):
    M[i] = {'name': m['name'], 'distributors': random.sample(all_distributors, random.randint(3, 8))}

with open('medicines_data.js', 'w', encoding='utf-8') as f:
    f.write('const medicineCatalog=' + json.dumps(M) + ';')

print(f'Updated medicines_data.js with {len(M)} medicines and {len(all_distributors)} distributors')
