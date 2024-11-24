from flask import Flask, request, render_template, jsonify
from model import predict_price
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        # JSON request
        data = request.get_json()
        sqft = data['sqft']
        bedrooms = data['bedrooms']
        predicted_price = predict_price(sqft, bedrooms)
        return jsonify(price=predicted_price)
    else:
        # Form submission
        sqft = float(request.form['sqft'])
        bedrooms = int(request.form['bedrooms'])
        predicted_price = predict_price(sqft, bedrooms)
        return render_template('result.html', price=predicted_price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
