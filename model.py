# model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data: Square footage (in sq ft), Number of bedrooms, and Price (in $)
data = {
    'SquareFootage': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'Bedrooms': [3, 3, 3, 4, 4, 4, 5, 5, 5, 5],
    'Price': [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Split the dataset into training and testing sets
X = df[['SquareFootage', 'Bedrooms']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

def predict_price(sqft, bedrooms):
    return model.predict([[sqft, bedrooms]])[0]
