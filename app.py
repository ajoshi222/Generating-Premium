from flask import Flask, escape, request, render_template, jsonify

import json

import csv


def load_rate_card_data():
    rate_card_data = []
    with open('Rate-Card-Data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rate_card_data.append(row)

    with open('insurance.premiums.json', 'w') as jsonfile:
        json.dump(rate_card_data, jsonfile, indent=4)

# Call the function to load rate card data
load_rate_card_data()
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict')
def predict():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/calculate_premium', methods=['POST'])
def calculate_premium_route():
    age = int(request.form['age'])
    sum_insured = int(request.form['sum_insured'])
    city_tier = request.form['city_tier']
    tenure = int(request.form['tenure'])

    premium = calculate_premium(age, sum_insured, city_tier, tenure)

    return render_template('result.html', premium=premium)


def calculate_premium(age, sum_insured, city_tier, tenure):
    # Implement your logic here to calculate the premium
    # based on the user inputs

    # Example calculation logic:
    base_rate = 14676
    floater_discount = 0 if age >= 45 else 50
    discounted_rate = base_rate * (1 - floater_discount/100)
    total = discounted_rate * sum_insured

    return total


if __name__ == "__main__":
    app.run(debug=True)


