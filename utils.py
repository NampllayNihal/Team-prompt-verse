# Simple demo database for medicines
DRUG_DATABASE = {
    "Paracetamol": {"dosage": "500mg every 6-8 hours", "alternatives": ["Ibuprofen", "Aspirin"]},
    "Ibuprofen": {"dosage": "200-400mg every 6 hours", "alternatives": ["Paracetamol"]},
    "Amoxicillin": {"dosage": "250-500mg every 8 hours", "alternatives": ["Azithromycin", "Cefalexin"]},
}

# Fake drug interaction database
INTERACTIONS = {
    ("Paracetamol", "Ibuprofen"): "Mild interaction: Monitor liver and kidney functions.",
    ("Amoxicillin", "Ibuprofen"): "No major interaction reported.",
    ("Paracetamol", "Amoxicillin"): "Safe to use together.",
}


def check_drug_interactions(medicines):
    results = []
    for i in range(len(medicines)):
        for j in range(i + 1, len(medicines)):
            pair = (medicines[i].strip(), medicines[j].strip())
            reverse_pair = (pair[1], pair[0])
            if pair in INTERACTIONS:
                results.append(f"{pair[0]} + {pair[1]}: {INTERACTIONS[pair]}")
            elif reverse_pair in INTERACTIONS:
                results.append(f"{reverse_pair[0]} + {reverse_pair[1]}: {INTERACTIONS[reverse_pair]}")
    if not results:
        results.append("No interactions found.")
    return results


def get_dosage_and_alternatives(medicines, age):
    results = {}
    for med in medicines:
        med = med.strip()
        if med in DRUG_DATABASE:
            dosage = DRUG_DATABASE[med]["dosage"]
            alternatives = DRUG_DATABASE[med]["alternatives"]

            # Adjust dosage for children under 12
            if age < 12:
                dosage = "Child dosage: Half of adult dose"
            
            results[med] = {"dosage": dosage, "alternatives": alternatives}
        else:
            results[med] = {"dosage": "Not found", "alternatives": []}
    return results

