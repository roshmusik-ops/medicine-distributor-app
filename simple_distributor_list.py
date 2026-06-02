import json

# Generic medicine distributors
generic_distributors = [
    {'name': 'Acceedee Agencies', 'phone': '0487-2345678', 'type': 'Generic Distributor', 'featured': True},
    {'name': 'Unique Pharma', 'phone': '0487-2456789', 'type': 'Generic Wholesaler', 'featured': True},
    {'name': 'Aiswarya Pharma', 'phone': '0487-2567890', 'type': 'Generic Distributor', 'featured': False},
    {'name': 'Charlsons Medisales', 'phone': '0485-2345678', 'type': 'Generic Wholesale', 'featured': False},
    {'name': 'Acceedee Pharma', 'phone': '0484-2345678', 'type': 'Generic Distributor', 'featured': False},
    {'name': 'Medi Agencies', 'phone': '0487-2567811', 'type': 'Generic Distributor', 'featured': False},
    {'name': 'Santevita', 'phone': '0487-2567812', 'type': 'Generic Wholesaler', 'featured': False},
]

# Ethical medicine distributors
ethical_distributors = [
    {'name': 'UMA', 'phone': '0488-2345678', 'type': 'Ethical Distributor', 'featured': True},
    {'name': 'LEO', 'phone': '0487-2234567', 'type': 'Ethical Wholesaler', 'featured': True},
    {'name': 'BALAJI', 'phone': '0480-2345678', 'type': 'Ethical Pharmacy', 'featured': True},
    {'name': 'JJ', 'phone': '0487-2123456', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'MMA', 'phone': '0482-2345678', 'type': 'Ethical Distributor', 'featured': True},
    {'name': 'ALLIED PHARMA', 'phone': '0487-2012345', 'type': 'Ethical Retail Chain', 'featured': False},
    {'name': 'MEDICO', 'phone': '0487-2901234', 'type': 'Ethical Retail', 'featured': False},
    {'name': 'GRACE', 'phone': '0480-2234567', 'type': 'Ethical Pharmacy', 'featured': False},
    {'name': 'KALPANA ENTER', 'phone': '0487-2890123', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'THOMSON', 'phone': '0487-2678901', 'type': 'Ethical Wholesaler', 'featured': False},
    {'name': 'BINU', 'phone': '0487-2567800', 'type': 'Ethical Pharma', 'featured': False},
    {'name': 'SUBHA', 'phone': '0487-2567801', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'PANIKULAM AGENCIES', 'phone': '0480-2567802', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'PANIKULAM PHARMA', 'phone': '0487-2567803', 'type': 'Ethical Pharmacy', 'featured': False},
    {'name': 'TRICHUR PHARMA', 'phone': '0487-2567804', 'type': 'Ethical Wholesaler', 'featured': False},
    {'name': 'INTER PHARMA', 'phone': '0487-2567805', 'type': 'Ethical Pharma', 'featured': False},
    {'name': 'SATHYA', 'phone': '0487-2567806', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'SURYA', 'phone': '0487-2567807', 'type': 'Ethical Pharmaceutical', 'featured': False},
    {'name': 'ELMA', 'phone': '0487-2567808', 'type': 'Ethical Healthcare', 'featured': False},
    {'name': 'US PHARMA', 'phone': '0487-2567809', 'type': 'Ethical Distributor', 'featured': False},
    {'name': 'CITY DRUGS', 'phone': '0487-2567810', 'type': 'Ethical Retail', 'featured': False},
]

# Write distributors.js
all_distributors = {
    'generic': generic_distributors,
    'ethical': ethical_distributors
}

with open('distributors.js', 'w', encoding='utf-8') as f:
    f.write('const allDistributors=' + json.dumps(all_distributors) + ';')

print('Generic Distributors: ' + str(len(generic_distributors)))
print('Ethical Distributors: ' + str(len(ethical_distributors)))
print('Total: ' + str(len(generic_distributors) + len(ethical_distributors)))
