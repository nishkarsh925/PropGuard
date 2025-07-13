import re
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Known party roles
known_roles = ["seller", "buyer", "witness"]

def extract_transaction_amount(text):
    match = re.search(r"(INR|₹)\s?[0-9,]+", text)
    return match.group(0) if match else None

def extract_property_address(text):
    match = re.search(r"located at (.*?)(?: is being sold|\.|\n)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_names_and_roles(doc, text, address):
    names = []
    roles = set()
    address_lower = address.lower() if address else ""

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            if name.lower() not in known_roles and name.lower() not in address_lower:
                names.append(name)

    manual_roles = re.findall(r"\((Buyer|Seller|Witness)\)", text, re.IGNORECASE)
    roles.update(role.capitalize() for role in manual_roles)

    return names, list(roles)

def extract_present_documents(text):
    document_keywords = {
        "sale_deed": ["sale deed"],
        "title_deed": ["title deed"],
        "ec": ["encumbrance certificate", "ec"],
        "mutation_certificate": ["mutation certificate", "khata", "mutation"],
        "tax_receipt": ["tax receipt", "property tax", "tax paid"],
        "building_plan": ["approved building plan", "sanction plan"],
        "possession_letter": ["possession letter", "occupancy certificate", "oc"],
        "rera_certificate": ["rera certificate", "rera id", "rera approved"],
        "power_of_attorney": ["power of attorney"],
        "id_proof": ["aadhaar", "pan card", "passport", "id proof"]
    }

    found_docs = {}
    text_lower = text.lower()
    for key, keywords in document_keywords.items():
        found_docs[key] = any(k in text_lower for k in keywords)

    return found_docs

def process_text(text):
    doc = nlp(text)
    amount = extract_transaction_amount(text)
    address = extract_property_address(text)
    names, roles = extract_names_and_roles(doc, text, address)
    documents_found = extract_present_documents(text)

    return {
        "transaction_amount": amount,
        "property_address": address,
        "names": names,
        "roles": roles,
        "documents_present": documents_found
    }

# Read input from sample.txt
if __name__ == "__main__":
    with open("output/sample.txt", "r", encoding="utf-8") as f:
        text = f.read()

    result = process_text(text)
    for key, value in result.items():
        print(f"{key}: {value}")



# Load text from a file
with open("output/sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
result = process_text(text)
f = open("output/processed_output.txt", "w")
con = f.write(str(result))
print(result)
# Print the extracted information
