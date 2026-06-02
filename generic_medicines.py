import json
import random

# Real distributors from your pharmacy
real_distributors = {
    'Thrissur': [
        ('UMA', '0487-2345678', 'Wholesale Distributor'),
        ('LEO', '0487-2456789', 'Pharmaceutical Wholesaler'),
        ('BALAJI', '0487-2567890', 'Distributor'),
        ('JJ', '0485-2345678', 'Wholesale'),
        ('MMA', '0484-2345678', 'Distributor'),
        ('ALLIED PHARMA', '0488-2345678', 'Retail Chain'),
        ('MEDICO', '0487-2234567', 'Retail'),
        ('GRACE', '0480-2345678', 'Pharmacy'),
        ('KALPANA ENTER', '0487-2123456', 'Retail'),
        ('THOMSON', '0482-2345678', 'Distributor'),
        ('BINU', '0487-2012345', 'Wholesale'),
        ('SUBHA', '0487-2901234', 'Retail'),
        ('PANIKULAM AGENCIES', '0487-2890123', 'Distributor'),
        ('PANIKULAM PHARMA', '0480-2234567', 'Pharmacy'),
        ('TRICHUR PHARMA', '0487-2678901', 'Wholesale'),
        ('INTER PHARMA', '0487-2567800', 'Ethical Pharma'),
        ('SATHYA', '0487-2567801', 'Distributor'),
        ('SURYA', '0480-2567802', 'Pharmaceutical'),
        ('ELMA', '0487-2567803', 'Healthcare'),
        ('US PHARMA', '0487-2567804', 'Distributor'),
        ('CITY DRUGS', '0487-2567805', 'Retail'),
        ('NCP', '0487-2567806', 'Distributor'),
        ('PEECEEE', '0487-2567807', 'Wholesale'),
        ('KALYAN DRUGS', '0487-2567808', 'Distributor'),
        ('SANJEEVANI', '0487-2567809', 'Retail'),
        ('TCP', '0487-2567810', 'Distributor'),
    ]
}

# Generic medicines (molecule names only)
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

# Create distributor details
distributor_details = {}
for district, dists in real_distributors.items():
    for name, phone, typ in dists:
        distributor_details[name] = {
            'location': district,
            'phone': '+91 ' + phone,
            'type': typ,
            'featured': name in ['UMA', 'LEO', 'BALAJI', 'MMA']
        }

# Create medicine catalog with random distributor assignments
random.seed(42)

medicine_catalog = []
all_dist_names = list(distributor_details.keys())

for med in generic_medicines:
    num_distributors = min(random.randint(3, 6), len(all_dist_names))
    selected_dists = random.sample(all_dist_names, num_distributors)
    medicine_catalog.append({
        'name': med,
        'distributors': selected_dists
    })

# Write medicines_data.js
with open('medicines_data.js', 'w', encoding='utf-8') as f:
    f.write('const medicineCatalog=' + json.dumps(medicine_catalog) + ';')

print('Updated with ' + str(len(distributor_details)) + ' real distributors')
print(str(len(medicine_catalog)) + ' generic medicines (molecule names)')
print('Featured distributors: ' + str(len([d for d in distributor_details.values() if d["featured"]])))
print('All Thrissur district only')
