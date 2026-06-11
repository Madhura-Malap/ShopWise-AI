# 🛒 ShopWise AI

An intelligent shopping assistant that recommends the most suitable products based on user requirementS.

The application understands user requirements such as budget, category, brand, and purpose, then recommends the most suitable products with a match score and detailed explanations.

---

## 🚀 Features

* - Natural Language Query Processing
* Budget-aware recommendations
* Category detection
* Brand detection
* Purpose-based filtering
* Intelligent Product Ranking and Match Scoring
* Product image integration
* Interactive web interface using Flask
* Dynamic recommendation cards
* Responsive user interface

---

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* HTML
* CSS

---

## 📂 Project Structure

```text
ShopWise-AI
│
├── static
│   ├── images
│   └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── shopping_engine.py
├── generate_dataset.py
├── products.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd ShopWise-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## 🔍 Example Queries

* Need a gaming laptop under 70000
* Need a phone under 25000
* Need earbuds under 5000
* Need a camera for photography under 80000

---

## 🎯 How It Works

1. User enters a product requirement.
2. NLP logic extracts:

   * Budget
   * Category
   * Brand
   * Purpose
3. Products are filtered from the dataset.
4. A match score is calculated.
5. Top recommendations are displayed with:

   * Product Image
   * Price
   * Rating
   * Features
   * Recommendation Reasons

---

## 🔮 Future Improvements

* Real e-commerce product integration
* Machine Learning-based recommendation models
* User accounts and saved searches
* Product comparison feature
* Amazon API integration
* Deployment on cloud platforms
* User preference learning
* Personalized recommendations

---

## 👨‍💻 Author

Developed to explore recommendation systems, natural language processing, and full-stack application development using Python and Flask.
