from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_monthly_payment(principal, apr, years):
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    return round(monthly_payment, 2)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    principal = float(request.form["principal"])
    apr = float(request.form["apr"])
    years = int(request.form["years"])

    monthly_payment = calculate_monthly_payment(principal, apr, years)
    
    return render_template("home.html", principal=principal, apr=apr, years=years, monthly_payment=monthly_payment)

if __name__ == "__main__":
    app.run(debug=True)
