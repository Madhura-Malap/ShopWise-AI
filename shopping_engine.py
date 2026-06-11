import pandas as pd
import re

products = pd.read_csv("products.csv")

def get_recommendations(query):

    budget_match = re.search(r'\d+', query)

    if budget_match:
        budget = int(budget_match.group())
    else:
        budget = 999999

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

    brands = [
        "HP","Acer","Lenovo","ASUS","Dell",
        "Samsung","Xiaomi","iQOO","Realme","OnePlus",
        "Sony","JBL","Boat","Noise","Zebronics",
        "Apple","Logitech","LG","BenQ","Canon",
        "Nikon","WD","Crucial","SanDisk",
        "TP-Link","Netgear","D-Link","Epson","Ambrane"
    ]

    brand = None

    for b in brands:
        if b.lower() in query.lower():
            brand = b
            break

    recommended = products[
        products["Price"] <= budget
    ]

    if category:
        recommended = recommended[
            recommended["Category"].str.contains(
                category,
                case=False
            )
        ]

    if purpose:
        recommended = recommended[
            recommended["Purpose"].str.contains(
                purpose,
                case=False
            )
        ]

    if recommended.empty:
        return []

    recommendations = []

    for index, product in recommended.iterrows():

        score = 30

        if budget > 0:

            price_bonus = (
                (budget - product["Price"]) / budget
            ) * 20

            score += max(price_bonus, 0)

        if purpose and purpose.lower() in product["Purpose"].lower():
            score += 30

        if brand and brand.lower() == product["Brand"].lower():
            score += 20

        score += product["Rating"] * 10

        match_percentage = min(
            round(score),
            100
        )

        reasons = []

        if product["Price"] <= budget:
            reasons.append("Fits your budget")

        if product["Rating"] >= 4.5:
            reasons.append("Excellent ratings")

        if purpose and purpose.lower() in product["Purpose"].lower():
            reasons.append(f"Suitable for {purpose}")

        category_map = {
            "Laptop": "laptop",
            "Smartphone": "phone",
            "Tablet": "tablet",
            "Smartwatch": "smartwatch",
            "Headphones": "headphones",
            "Earbuds": "earbuds",
            "Monitor": "monitor",
            "Keyboard": "keyboard",
            "Mouse": "mouse",
            "Camera": "camera",
            "SSD": "ssd",
            "Printer": "printer",
            "Speaker": "speaker",
            "Power Bank": "powerbank",
            "Router": "router"
        }

        brand_name = (
            product["Brand"]
            .lower()
            .replace("-", "")
        )

        suffix = category_map.get(
            product["Category"],
            ""
        )

        image_name = f"{brand_name}_{suffix}.jpg"

        recommendations.append(
            {
                "name": product["Product_Name"],
                "brand": product["Brand"],
                "price": product["Price"],
                "rating": product["Rating"],
                "match": match_percentage,
                "category": product["Category"],
                "image": image_name,
                "feature1": product["Feature1"],
                "feature2": product["Feature2"],
                "feature3": product["Feature3"],
                "reasons": reasons
            }
        )

    recommendations = sorted(
        recommendations,
        key=lambda x: x["match"],
        reverse=True
    )

    return recommendations[:3]