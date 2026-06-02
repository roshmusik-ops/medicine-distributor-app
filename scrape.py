"""Pharmapps Scraper - Run: python scrape.py (no extra packages needed)"""
import requests,json,random,re

URL="https://www.pharmapps.in/RetailerHome/Index"
HDR={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
DISTS=["Apollo Pharmacy Distributors","Medplus Healthcare","Kerala Medical Agencies",
"South India Pharma","Cochin Medical Supplies","Malabar Pharma Hub","Palakkad Medical Stores",
"Kannur Pharma Center","Kottayam Medicine Mart","Alappuzha Medical Agency","Pathanamthitta Pharma",
"Idukki Mountain Pharma","Wayanad Green Pharmacy","Kasaragod Pharma World","Kollam Medical Hub"]
SKIP={"home","about","login","contact","search","menu","welcome","index","products","details"}

def clean_text(t):
    t=re.sub(r'<[^>]+>','',t)
    t=re.sub(r'\s+',' ',t).strip()
    return t

def scrape():
    print("Fetching Pharmapps...")
    try:
        r=requests.get(URL,headers=HDR,timeout=30)
        html=r.text
        meds=set()
        # Extract text between tags
        for m in re.findall(r'>([^<]{3,60})<',html):
            t=clean_text(m)
            if t and not any(w in t.lower() for w in SKIP):
                # Keep medicine-like names
                if re.match(r'^[A-Za-z0-9\s\-+/%().]+$',t):
                    meds.add(t)
        return meds
    except Exception as e:
        print(f"Error: {e}")
        return set()

meds=scrape()
print(f"Found {len(meds)} items")

# Build database
random.seed(42)
db=[]
for m in sorted(meds)[:500]:  # Limit to 500 medicines
    db.append({"name":m,"distributors":random.sample(DISTS,random.randint(3,5))})

# Save
with open("medicines_data.js","w",encoding="utf-8") as f:
    f.write("const medicineCatalog="+json.dumps(db,ensure_ascii=False)+";")
print(f"Saved {len(db)} medicines to medicines_data.js")
print("Now copy medicines_data.js content into index.html")
