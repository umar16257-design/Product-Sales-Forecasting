"""
Product Sales Forecasting — Flask API
Uses trained XGBoost model to predict daily sales for a given store and date.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

# ---------------------------------------------------------------
# Load model + encoders + feature order (once, at server startup)
# ---------------------------------------------------------------
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR,
        '..',
        'models'
    )
)

print("Loading model artifacts...")
print("Model directory:", MODEL_DIR)

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        'xgboost_sales_model.pkl'
    )
)

encoders = joblib.load(
    os.path.join(
        MODEL_DIR,
        'label_encoders.pkl'
    )
)

feature_cols = joblib.load(
    os.path.join(
        MODEL_DIR,
        'feature_columns.pkl'
    )
)

print("✅ Model artifacts loaded")

app = Flask(__name__)
print("✅ Flask application initialized")


# ---------------------------------------------------------------
# Feature-building helper — takes raw user input → model-ready row
# ---------------------------------------------------------------
def build_feature_row(form_data):
    """
    Convert form input into a single-row DataFrame matching the model's
    training feature order and encoding.
    """
    date = pd.to_datetime(form_data['date'])

    row = {
        'Store_id':      int(form_data['store_id']),
        'Store_Type':    encoders['Store_Type'].transform([form_data['store_type']])[0],
        'Location_Type': encoders['Location_Type'].transform([form_data['location_type']])[0],
        'Region_Code':   encoders['Region_Code'].transform([form_data['region_code']])[0],
        'Holiday':       int(form_data['holiday']),
        'Discount':      encoders['Discount'].transform([form_data['discount']])[0],
        'Year':          date.year,
        'Month':         date.month,
        'Day':           date.day,
        'DayOfWeek':     date.dayofweek,
        'WeekOfYear': int(date.isocalendar().week),
    }

    # Build a DataFrame in the exact column order the model was trained on
    X = pd.DataFrame([row])[feature_cols]
    return X


# ---------------------------------------------------------------
# Routes
# ---------------------------------------------------------------

@app.route('/')
def home():
    """Render the HTML form with default values."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission → return prediction along with the submitted inputs."""
    try:
        form_data = {
            'store_id':      request.form['store_id'],
            'store_type':    request.form['store_type'],
            'location_type': request.form['location_type'],
            'region_code':   request.form['region_code'],
            'date':          request.form['date'],
            'holiday':       request.form['holiday'],
            'discount':      request.form['discount'],
        }

        X = build_feature_row(form_data)
        prediction = model.predict(X)[0]
        prediction = max(0, float(prediction))  # sales can't be negative

        return render_template(
            'index.html',
            prediction_text=f"Predicted Daily Sales: ₹ {prediction:,.2f}",
            input_summary=form_data,
        )

    except Exception as e:

        print("Prediction error:",str(e))
    
        return render_template(
            'index.html',
            prediction_text=f"⚠️ Error: {str(e)}",
        )


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint — for programmatic access."""
    try:
        data = request.get_json()
        X = build_feature_row(data)
        prediction = float(model.predict(X)[0])
        prediction = max(0, prediction)
        return jsonify({
            'predicted_sales': round(prediction, 2),
            'input': data,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ---------------------------------------------------------------
# Run the app
# ---------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)