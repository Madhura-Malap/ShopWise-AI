import pandas as pd
import random

categories = {
    "Laptop": ["HP", "Dell", "Lenovo", "ASUS", "Acer"],
    "Smartphone": ["Samsung", "OnePlus", "Xiaomi", "Realme", "iQOO"],
    "Tablet": ["Samsung", "Apple", "Lenovo"],
    "Smartwatch": ["Apple", "Samsung", "Noise"],
    "Headphones": ["Sony", "JBL", "Boat"],
    "Earbuds": ["Boat", "Noise", "Sony"],
    "Monitor": ["LG", "BenQ", "Dell"],
    "Keyboard": ["Logitech", "HP", "Dell"],
    "Mouse": ["Logitech", "HP", "Dell"],
    "Camera": ["Canon", "Nikon", "Sony"],
    "SSD": ["WD", "Crucial", "SanDisk"],
    "Printer": ["HP", "Canon", "Epson"],
    "Speaker": ["JBL", "Sony", "Boat"],
    "Power Bank": ["Mi", "Ambrane", "Realme"],
    "Router": ["TP-Link", "D-Link", "Netgear"]
}

price_ranges = {
    "Laptop": (35000, 100000),
    "Smartphone": (10000, 80000),
    "Tablet": (15000, 70000),
    "Smartwatch": (1500, 30000),
    "Headphones": (1000, 15000),
    "Earbuds": (800, 12000),
    "Monitor": (5000, 40000),
    "Keyboard": (500, 8000),
    "Mouse": (300, 5000),
    "Camera": (25000, 150000),
    "SSD": (2000, 15000),
    "Printer": (4000, 30000),
    "Speaker": (1000, 25000),
    "Power Bank": (500, 5000),
    "Router": (1000, 10000)
}

purpose_map = {
    "Laptop": ["Gaming", "Coding", "Student", "Office"],
    "Smartphone": ["Photography", "Gaming", "Daily Use"],
    "Tablet": ["Student", "Work", "Streaming"],
    "Smartwatch": ["Fitness", "Daily Use"],
    "Headphones": ["Music", "Gaming"],
    "Earbuds": ["Music", "Daily Use"],
    "Monitor": ["Gaming", "Coding", "Office"],
    "Keyboard": ["Coding", "Gaming"],
    "Mouse": ["Gaming", "Work"],
    "Camera": ["Photography", "Professional"],
    "SSD": ["Storage", "Professional"],
    "Printer": ["Office", "Work"],
    "Speaker": ["Music", "Entertainment"],
    "Power Bank": ["Travel", "Daily Use"],
    "Router": ["Work", "Streaming"]
}

features = {
    "Laptop": ["16GB RAM", "512GB SSD", "Ryzen 7", "Intel i7"],
    "Smartphone": ["50MP Camera", "6000mAh", "120Hz Display", "8GB RAM"],
    "Tablet": ["Stylus Support", "10-inch Display", "128GB Storage"],
    "Smartwatch": ["Heart Rate Monitor", "GPS", "AMOLED Display"],
    "Headphones": ["Noise Cancellation", "40hr Battery", "Bluetooth 5.2"],
    "Earbuds": ["ANC", "Touch Controls", "Fast Charging"],
    "Monitor": ["144Hz", "IPS Panel", "2K Resolution"],
    "Keyboard": ["Mechanical Keys", "RGB Lighting", "Wireless"],
    "Mouse": ["Wireless", "16000 DPI", "RGB"],
    "Camera": ["4K Video", "Mirrorless", "24MP Sensor"],
    "SSD": ["NVMe", "1TB Storage", "High Speed"],
    "Printer": ["Wireless Printing", "Color Print", "Duplex"],
    "Speaker": ["Bluetooth", "Deep Bass", "Portable"],
    "Power Bank": ["Fast Charging", "20000mAh", "USB-C"],
    "Router": ["WiFi 6", "Dual Band", "High Speed"]
}

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

products = []

product_id = 1

for category, brands in categories.items():

    for i in range(10):

        brand = random.choice(brands)

        product_name = f"{brand} {category} {i+1}"

        min_price, max_price = price_ranges[category]

        price = random.randint(
            min_price,
            max_price
        )

        rating = round(random.uniform(3.8, 4.9), 1)

        purpose = random.choice(
            purpose_map[category]
        )

        selected_features = random.sample(
            features[category],
            3
        )

        feature1 = selected_features[0]
        feature2 = selected_features[1]
        feature3 = selected_features[2]

        products.append([
            f"P{product_id:03}",
            product_name,
            category,
            brand,
            price,
            rating,
            purpose,
            feature1,
            feature2,
            feature3
        ])

        product_id += 1

columns = [
    "Product_ID",
    "Product_Name",
    "Category",
    "Brand",
    "Price",
    "Rating",
    "Purpose",
    "Feature1",
    "Feature2",
    "Feature3"
]

df = pd.DataFrame(products, columns=columns)

df.to_csv("products.csv", index=False)

print("Dataset Created Successfully!")
print("Total Products:", len(df))