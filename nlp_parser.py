import re

query = input("What are you looking for? ")

# Extract budget
budget_match = re.search(r'\d+', query)

if budget_match:
    budget = int(budget_match.group())
else:
    budget = None

# Extract purpose
purposes = ["Gaming", "Coding", "Student"]

purpose = None

for p in purposes:
    if p.lower() in query.lower():
        purpose = p
        break

print("Budget:", budget)
print("Purpose:", purpose)