import json
import random

# Generic medicine distributors (molecule names)
generic_distributors = {
    'Thrissur': [
        ('Acceedee Agencies', '0487-2345678', 'Generic Distributor'),
        ('Unique Pharma', '0487-2456789', 'Generic Wholesaler'),
        ('Aiswarya Pharma', '0487-2567890', 'Generic Distributor'),
        ('Charlsons Medisales', '0485-2345678', 'Generic Wholesale'),
        ('Acceedee Pharma', '0484-2345678', 'Generic Distributor'),
        ('Medi Agencies', '0487-2567811', 'Generic Distributor'),
        ('Santevita', '0487-2567812', 'Generic Wholesaler'),
    ]
}

# Ethical medicine distributors (brand names)
ethical_distributors = {
    'Thrissur': [
        ('UMA', '0488-2345678', 'Ethical Distributor'),
        ('LEO', '0487-2234567', 'Ethical Wholesaler'),
        ('BALAJI', '0480-2345678', 'Ethical Pharmacy'),
        ('JJ', '0487-2123456', 'Ethical Distributor'),
        ('MMA', '0482-2345678', 'Ethical Distributor'),
        ('ALLIED PHARMA', '0487-2012345', 'Ethical Retail Chain'),
        ('MEDICO', '0487-2901234', 'Ethical Retail'),
        ('GRACE', '0480-2234567', 'Ethical Pharmacy'),
        ('KALPANA ENTER', '0487-2890123', 'Ethical Distributor'),
        ('THOMSON', '0487-2678901', 'Ethical Wholesaler'),
        ('BINU', '0487-2567800', 'Ethical Pharma'),
        ('SUBHA', '0487-2567801', 'Ethical Distributor'),
        ('PANIKULAM AGENCIES', '0480-2567802', 'Ethical Distributor'),
        ('PANIKULAM PHARMA', '0487-2567803', 'Ethical Pharmacy'),
        ('TRICHUR PHARMA', '0487-2567804', 'Ethical Wholesaler'),
        ('INTER PHARMA', '0487-2567805', 'Ethical Pharma'),
        ('SATHYA', '0487-2567806', 'Ethical Distributor'),
        ('SURYA', '0487-2567807', 'Ethical Pharmaceutical'),
        ('ELMA', '0487-2567808', 'Ethical Healthcare'),
        ('US PHARMA', '0487-2567809', 'Ethical Distributor'),
        ('CITY DRUGS', '0487-2567810', 'Ethical Retail'),
    ]
}

# Generic medicines (molecule names)
generic_medicines = [
    'Atorvastatin', 'Metformin', 'Amoxicillin', 'Paracetamol', 'Ibuprofen',
    'Omeprazole', 'Amlodipine', 'Lisinopril', 'Enalapril', 'Ramipril',
    'Losartan', 'Valsartan', 'Glipizide', 'Gliclazide', 'Pioglitazone',
    'Sitagliptin', 'Allopurinol', 'Febuxostat', 'Colchicine', 'Indomethacin',
    'Diclofenac', 'Meloxicam', 'Celecoxib', 'Naproxen', 'Aspirin',
    'Clopidogrel', 'Ticagrelor', 'Warfarin', 'Dabigatran', 'Rivaroxaban',
    'Apixaban', 'Enoxaparin', 'Heparin', 'Simvastatin', 'Pravastatin',
    'Rosuvastatin', 'Fenofibrate', 'Gemfibrozil', 'Niacin', 'Ezetimibe',
    'Levothyroxine', 'Propranolol', 'Atenolol', 'Metoprolol', 'Carvedilol',
    'Bisoprolol', 'Labetalol', 'Hydralazine', 'Minoxidil', 'Verapamil',
    'Diltiazem', 'Nifedipine', 'Felodipine', 'Isradipine', 'Nicardipine',
    'Perindopril', 'Quinapril', 'Moexipril', 'Captopril', 'Benazepril',
    'Fosinopril', 'Trandolapril', 'Irbesartan', 'Olmesartan', 'Telmisartan',
    'Candesartan', 'Eprosartan', 'Azilsartan', 'Chlorthalidone', 'Hydrochlorothiazide',
    'Furosemide', 'Torsemide', 'Bumetanide', 'Ethacrynic Acid', 'Spironolactone',
    'Amiloride', 'Triamterene', 'Acetazolamide', 'Dorzolamide', 'Brinzolamide',
    'Mannitol', 'Glycerol', 'Urea', 'Sodium Bicarbonate', 'Sodium Chloride',
    'Potassium Chloride', 'Magnesium Sulfate', 'Calcium Gluconate', 'Dextrose',
    'Lactated Ringer', 'Normal Saline', 'Albumin', 'Fresh Frozen Plasma',
    'Tranexamic Acid', 'Epsilon Aminocaproic Acid', 'Aprotinin', 'Desmopressin',
    'Vasopressin', 'Terlipressin', 'Octreotide', 'Lanreotide', 'Pasireotide',
    'Somatostatin', 'Glucagon', 'Epinephrine', 'Norepinephrine', 'Dopamine',
    'Dobutamine', 'Isoproterenol', 'Phenylephrine', 'Metaraminol', 'Mephentermine',
    'Methoxamine', 'Midodrine', 'Pseudoephedrine', 'Phenylpropanolamine', 'Ephedrine',
    'Amphetamine', 'Methylphenidate', 'Modafinil', 'Armodafinil', 'Caffeine',
    'Theophylline', 'Theobromine', 'Pentoxifylline', 'Cilostazol', 'Dipyridamole',
    'Ticlopidine', 'Prasugrel', 'Cangrelor', 'Vorapaxar', 'Fondaparinux',
    'Dalteparin', 'Tinzaparin', 'Certoparin', 'Nadroparin', 'Parnaparin',
    'Reviparin', 'Bemiparin', 'Gabapentin', 'Pregabalin', 'Baclofen',
    'Tizanidine', 'Cyclobenzaprine', 'Methocarbamol', 'Carisoprodol', 'Chlorzoxazone',
    'Metaxalone', 'Orphenadrine', 'Dantrolene', 'Levodopa', 'Carbidopa',
    'Benserazide', 'Amantadine', 'Rimantadine', 'Bromocriptine', 'Pergolide',
    'Pramipexole', 'Ropinirole', 'Rotigotine', 'Apomorphine', 'Lisuride',
    'Cabergoline', 'Quinagolide', 'Entacapone', 'Tolcapone', 'Rasagiline',
    'Selegiline', 'Moclobemide', 'Phenelzine', 'Tranylcypromine', 'Isocarboxazid',
    'Fluoxetine', 'Sertraline', 'Paroxetine', 'Citalopram', 'Escitalopram',
    'Fluvoxamine', 'Venlafaxine', 'Duloxetine', 'Milnacipran', 'Levomilnacipran',
    'Desvenlafaxine', 'Bupropion', 'Mirtazapine', 'Nefazodone', 'Trazodone',
    'Vilazodone', 'Vortioxetine', 'Amitriptyline', 'Nortriptyline', 'Doxepin',
    'Imipramine', 'Desipramine', 'Clomipramine', 'Trimipramine', 'Protriptyline'
]

# Create distributor details with type
distributor_details = {}

# Add generic distributors
for district, dists in generic_distributors.items():
    for name, phone, typ in dists:
        distributor_details[name] = {
            'location': district,
            'phone': '+91 ' + phone,
            'type': typ,
            'featured': name in ['Acceedee Agencies', 'Unique Pharma'],
            'medicine_type': 'Generic'
        }

# Add ethical distributors
for district, dists in ethical_distributors.items():
    for name, phone, typ in dists:
        distributor_details[name] = {
            'location': district,
            'phone': '+91 ' + phone,
            'type': typ,
            'featured': name in ['UMA', 'LEO', 'BALAJI', 'MMA'],
            'medicine_type': 'Ethical'
        }

# Create medicine catalog with random distributor assignments (only generic distributors for generic medicines)
random.seed(42)

medicine_catalog = []
generic_dist_names = [d for d in distributor_details.keys() if distributor_details[d]['medicine_type'] == 'Generic']

for med in generic_medicines:
    num_distributors = min(random.randint(2, 4), len(generic_dist_names))
    selected_dists = random.sample(generic_dist_names, num_distributors)
    medicine_catalog.append({
        'name': med,
        'distributors': selected_dists,
        'type': 'Generic'
    })

# Write medicines_data.js
with open('medicines_data.js', 'w', encoding='utf-8') as f:
    f.write('const medicineCatalog=' + json.dumps(medicine_catalog) + ';')

# Write distributor_details.js
with open('distributor_details.js', 'w', encoding='utf-8') as f:
    f.write('const distributorDetails=' + json.dumps(distributor_details) + ';')

print('Generic Distributors: 7')
print('Ethical Distributors: 21')
print('Total Distributors: ' + str(len(distributor_details)))
print('Generic Medicines: ' + str(len(medicine_catalog)))
print('All Thrissur district only')
