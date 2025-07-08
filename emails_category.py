import csv
import json

# Define keywords that indicate sensitive data or issues
SENSITIVE_KEYWORDS = ["password", "confidential", "ssn", "social security", "secret", "private"]
IMPORTANT_KEYWORDS = ["important", "urgent", "action required", "immediate", "asap", "critical"]
ADS_WINNER_KEYWORDS = ["winner", "congratulations", "prize", "won", "claim", "free", "offer", "promotion", "advertisement", "ad"]
SUPERMARKET_KEYWORDS = [
    "supermarket", "store", "grocery", "market", "branch", "cashier", "inventory", "aisle", "checkout", "receipt", "customer", "discount", "loyalty", "cart"
]

def contains_sensitive_data(text):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SENSITIVE_KEYWORDS)

def is_important(row):
    row_text = " ".join(row).lower()
    return any(keyword in row_text for keyword in IMPORTANT_KEYWORDS)

def is_ads_or_winner(row):
    row_text = " ".join(row).lower()
    return any(keyword in row_text for keyword in ADS_WINNER_KEYWORDS)

def is_supermarket_related(row):
    row_text = " ".join(row).lower()
    return any(keyword in row_text for keyword in SUPERMARKET_KEYWORDS)

sensitive_rows = []
non_sensitive_rows = []

with open(r"D:\Python-tester\Email Examples - Project_Manager_Send.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        row_text = " ".join(row)
        if contains_sensitive_data(row_text):
            sensitive_rows.append(row)
        else:
            non_sensitive_rows.append(row)

# ترتيب الصفوف الحساسة من الأكثر حساسية إلى الأقل
def sensitivity_score(row):
    row_text = " ".join(row).lower()
    return sum(row_text.count(keyword) for keyword in SENSITIVE_KEYWORDS)

# Separate sensitive rows into supermarket, important, normal, and ads/winner
supermarket_rows = []
important_rows = []
ads_winner_rows = []
other_sensitive_rows = []

for row in sensitive_rows:
    if is_supermarket_related(row):
        supermarket_rows.append(row)
    elif is_important(row):
        important_rows.append(row)
    elif is_ads_or_winner(row):
        ads_winner_rows.append(row)
    else:
        other_sensitive_rows.append(row)

supermarket_rows_sorted = sorted(supermarket_rows, key=sensitivity_score, reverse=True)
important_rows_sorted = sorted(important_rows, key=sensitivity_score, reverse=True)
other_sensitive_rows_sorted = sorted(other_sensitive_rows, key=sensitivity_score, reverse=True)
ads_winner_rows_sorted = sorted(ads_winner_rows, key=sensitivity_score, reverse=True)

# Final order: supermarket -> important -> other sensitive -> ads/winner
sensitive_rows_sorted = supermarket_rows_sorted + important_rows_sorted + other_sensitive_rows_sorted + ads_winner_rows_sorted

print("Sensitive Data Rows (supermarket at top, then important, ads/winner at bottom):")
for row in sensitive_rows_sorted:
    print(row)

print("\nNon-sensitive Data Rows:")
for row in non_sensitive_rows:
    print(row)

# Automated Email Categories:
CATEGORIES = [
    "supermarket_related",   # Emails related to supermarket operations, staff, inventory, etc.
    "sensitive",             # Emails containing sensitive data (passwords, confidential info, etc.)
    "important",             # Emails marked as important, urgent, or requiring immediate action
    "ads_or_winner",         # Promotional, advertisement, or "winner" type emails
    "non_sensitive"          # All other emails not matching the above categories
]

def categorize_row(row):
    if is_supermarket_related(row):
        return "supermarket_related"
    elif is_important(row):
        return "important"
    elif is_ads_or_winner(row):
        return "ads_or_winner"
    elif contains_sensitive_data(" ".join(row)):
        return "sensitive"
    else:
        return "non_sensitive"

# Prepare data for JSON export
categorized_data = []
with open(r"D:\Python-tester\Email Examples - Project_Manager_Send.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        category = categorize_row(row)
        categorized_data.append({
            "category": category,
            "row": row
        })

# Write to JSON file
with open(r"d:\Python-tester\emails_categorized.json", "w", encoding="utf-8") as jsonfile:
    json.dump(categorized_data, jsonfile, ensure_ascii=False, indent=2)