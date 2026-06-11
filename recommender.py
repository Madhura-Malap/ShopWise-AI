import pandas as pd
import re

# Load dataset
products = pd.read_csv("products.csv")

# User Query
query = input("What are you looking for? ")

# ---------------- BUDGET DETECTION ----------------

budget_match = re.search(r'\d+', query)

if budget_match:
    budget = int(budget_match.group())
else:
    budget = 999999

# ---------------- PURPOSE DETECTION ----------------

purposes = [
    "Gaming",
    "Coding",
    "Student",
    "Photography",
    "Music",
    "Office",
    "Work",
    "Daily Use",
    "Streaming",
    "Professional"
]
purpose = None

for p in purposes:
    if p.lower() in query.lower():
        purpose = p
        break

# ---------------- CATEGORY DETECTION ----------------

category_keywords = {
    "Laptop": ["laptop", "lappy"],
    "Smartphone": ["smartphone", "phone", "mobile"],
    "Tablet": ["tablet", "ipad"],
    "Smartwatch": ["smartwatch", "watch"],
    "Headphones": ["headphones"],
    "Earbuds": ["earbuds", "buds"],
    "Monitor": ["monitor"],
    "Keyboard": ["keyboard"],
    "Mouse": ["mouse"],
    "Printer": ["printer"],
    "Speaker": ["speaker"],
    "Camera": ["camera"],
    "Power Bank": ["power bank"],
    "Router": ["router"],
    "SSD": ["ssd"]
}

category = None

for cat, keywords in category_keywords.items():

    for keyword in keywords:

        if keyword.lower() in query.lower():
            category = cat
            break

    if category:
        break

# ---------------- BRAND DETECTION ----------------

brands = [
    "HP",
    "Acer",
    "Lenovo",
    "ASUS",
    "Dell",
    "Samsung",
    "Xiaomi",
    "iQOO",
    "Realme",
    "OnePlus",
    "Sony",
    "JBL",
    "Boat",
    "Noise",
    "Zebronics",
    "Apple",
    "Logitech",
    "LG",
    "BenQ",
    "Canon",
    "Nikon",
    "WD",
    "Crucial",
    "SanDisk",
    "TP-Link",
    "Netgear",
    "D-Link",
    "Epson",
    "Ambrane"
]

brand = None

for b in brands:
    if b.lower() in query.lower():
        brand = b
        break

# ---------------- FILTER PRODUCTS ----------------

recommended = products[
    products["Price"] <= budget
]

# Category Filter
if category:
    recommended = recommended[
        recommended["Category"].str.contains(
            category,
            case=False
        )
    ]

# Purpose Filter
if purpose:
    recommended = recommended[
        recommended["Purpose"].str.contains(
            purpose,
            case=False
        )
    ]

# ---------------- SCORING ENGINE ----------------

recommendations = []

for index, product in recommended.iterrows():

    score = 0

    # Budget Match
    score += 30

    # Price Bonus
    if budget > 0:

        price_bonus = (
            (budget - product["Price"]) / budget
        ) * 20

    score += max(price_bonus, 0)

    # Purpose Match
    if purpose and purpose.lower() in product["Purpose"].lower():
        score += 30

    # Brand Match
    if brand and brand.lower() == product["Brand"].lower():
        score += 20

    # Rating Contribution
    score += product["Rating"] * 10

    match_percentage = min(
    round(score),
    100
    )

    recommendations.append(
        {
            "Product": product,
            "Score": match_percentage
        }
    )

if recommended.empty:

    print("\nNo matching products found.")

    exit()

# ---------------- SORT BY SCORE ----------------

recommendations = sorted(
    recommendations,
    key=lambda x: x["Score"],
    reverse=True
)

# ---------------- TOP 3 ----------------

top3 = recommendations[:3]

# ---------------- OUTPUT ----------------

print("\n==============================")
print(" TOP RECOMMENDATIONS ")
print("==============================")

for item in top3:

    product = item["Product"]

    print("\n🏆 Recommended Product")

    print("Product :", product["Product_Name"])
    print("Brand   :", product["Brand"])
    print("Price   : ₹", product["Price"])
    print("Rating  :", product["Rating"])

    print(f"Match Percentage : {item['Score']}%")

    print("\nWhy Recommended?")

    if product["Price"] <= budget:
        print("✓ Fits your budget")

    if product["Rating"] >= 4.5:
        print("✓ Excellent customer ratings")
    else:
        print("✓ Good customer ratings")

    if purpose and purpose.lower() in product["Purpose"].lower():
        print(f"✓ Suitable for {purpose}")

    if brand and brand.lower() == product["Brand"].lower():
        print(f"✓ Matches preferred brand ({brand})")

# ---------------- DEBUG INFO ----------------

print("\nDetected Values")
print("----------------")
print("Budget   :", budget)
print("Purpose  :", purpose)
print("Category :", category)
print("Brand    :", brand)