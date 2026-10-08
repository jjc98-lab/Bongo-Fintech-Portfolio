transactions = [
    {"amount": 25000, "status": "successful"},
    {"amount": 15000, "status": "successful"},
    {"amount": 50000, "status": "failed"},
    {"amount": 10000, "status": "successful"},
    {"amount": 30000, "status": "failed"},
    {"amount": 40000, "status": "successful"},
    {"amount": 10000, "status": "successful"},
    {"amount": 30000, "status": "failed"},
    {"amount": 20000, "status": "successful"},
    {"amount": 25000, "status": "successful"}
]

total_value = sum(transaction["amount"] for transaction in transactions)

successful = sum(
    1 for transaction in transactions
    if transaction["status"] == "successful"
)

failed = sum(
    1 for transaction in transactions
    if transaction["status"] == "failed"
)

success_rate = (successful / len(transactions)) * 100

print("Total transaction value:", total_value)
print("Successful transactions:", successful)
print("Failed transactions:", failed)
print("Success rate:", success_rate, "%")