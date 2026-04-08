from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []

def categorize(text):
    text = text.lower()
    if "food" in text or "pizza" in text:
        return "Food"
    elif "electricity" in text or "bill" in text:
        return "Bills"
    elif "bus" in text or "travel" in text:
        return "Travel"
    else:
        return "Other"

@app.route("/")
def home():
    return "Smart Expense Tracker Running"

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.json
    text = data.get("text")
    amount = data.get("amount")

    category = categorize(text)

    expense = {
        "text": text,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    return jsonify(expense)

@app.route("/all")
def get_all():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
