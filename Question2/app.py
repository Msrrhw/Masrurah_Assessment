from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class BankAccount:
    def __init__(mine, account_holder, balance=0.0):
        mine.account_holder = account_holder
        mine.balance = balance

    def deposit(mine, amount):
        if amount > 0:
            mine.balance += amount
            return True, f"Deposited ${amount:.2f}."
        return False, "Deposit amount must be positive."

    def withdraw(mine, amount):
        if amount > mine.balance:
            return False, "Insufficient funds for withdrawal."
        elif amount <= 0:
            return False, "Withdrawal amount must be positive."
        else:
            mine.balance -= amount
            return True, f"Withdrew ${amount:.2f}."

    def get_balance(mine):
        return mine.balance


account = BankAccount("Masrurah", 100.0)

@app.route("/")
def index():
    return render_template("index.html", account_holder=account.account_holder)


@app.route("/api/get_balance", methods=["GET"])
def get_balance():
    return jsonify(balance=account.get_balance())


@app.route("/api/deposit", methods=["POST"])
def deposit():
    data = request.json
    amount = data.get("amount", 0.0)
    success, message = account.deposit(amount)
    return jsonify(success=success, message=message, balance=account.get_balance())


@app.route("/api/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    amount = data.get("amount", 0.0)
    success, message = account.withdraw(amount)
    return jsonify(success=success, message=message, balance=account.get_balance())


if __name__ == "__main__":
    app.run(debug=True)
