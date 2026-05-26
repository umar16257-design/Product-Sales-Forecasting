# Product Sales Forecasting

## Project Overview

## Project Overview

This project forecast daily retail sales across 365 retail stores using Machine Learning and an XGBoost regression model.

The system analyzes historical store data and forecasts expected sales based on:

- Store characteristics
- Location information
- Region
- Discounts
- Holidays
- Date features

The model is deployed using Flask API and includes a user-friendly web interface.

---

Live Demo: https://product-sales-forecasting-19pj.onrender.com
Note: The free tier sleeps after 15 min of inactivity. First request after sleep takes ~30-60 sec to wake up — please be patient on your first visit.

Tableau Dashboard: https://public.tableau.com/app/profile/sruthi.s6388/viz/ProductSalesForecasting_17768358106560/DeepDiveStoreRegion

Technical Blog (Medium): https://medium.com/@sruthiswathandran/from-raw-csv-to-live-api-a-retail-sales-forecasting-journey-d38146002b1b

---

## Business Problem

Accurate sales forecasting helps businesses:

- Improve inventory management
- Reduce stock shortages
- Optimize supply chains
- Improve financial planning
- Support marketing decisions
- Enable strategic decision-making

---

## Dataset Features

| Feature | Description |
|----------|-------------|
| Store_id | Unique store identifier |
| Store_Type | Store category |
| Location_Type | Location classification |
| Region_Code | Region identifier |
| Holiday | Holiday indicator |
| Discount | Discount availability |
| Date | Transaction date |
| Sales | Target variable |

---

## Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Hypothesis Testing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Flask Deployment

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Flask
- HTML/CSS
- GitHub

---

## Target Metric

**Primary Metric**

- RMSE (Root Mean Squared Error)

**Secondary Metrics**

- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)
- R² Score

---

## 🏆 Final Results

| Rank | Model | MAE | RMSE | MAPE | R² |
|:-----|:-------|:----|:------|:------|:-----|
| 🥇 1 | XGBoost | 8,994 | 13,239 | 26.9% | 0.572 |
| 🥈 2 | LightGBM | 9,157 | 13,425 | 28.1% | 0.560 |
| 🥉 3 | Random Forest | 9,696 | 14,445 | 29.4% | 0.491 |
| 4 | Linear Regression | 10,831 | 15,653 | 31.1% | 0.402 |

### Model Selection

XGBoost was selected as the final production model because it achieved:

- Lowest RMSE
- Lowest MAE
- Lowest MAPE
- Highest R² score

This makes it the strongest model for generalization and deployment.

---

## 🔍 Key Findings from EDA

1.Store Performance
- Store Type is the strongest predictor (**F = 35,123**)
- S4 stores generate approximately **2.2× higher sales** than S2 stores on average

2.Discounts Impact
- Discounts increase sales by approximately **32%**
- Hypothesis testing confirmed this effect is statistically significant

3.Holiday Effect
- Holidays reduce sales by approximately **19%**
- This may occur due to store closures or reduced operational hours

4.Weekly Trends
- Weekend sales increase by approximately **23%**
- Sunday shows the highest average sales performance

5.Regional Insights
- Region has relatively weak influence overall
- Region R1 dominates top-performing stores
- **8 of the top 10 stores** belong to R1

---

## 🏗️ Tech Stack

- Analysis: Python, Pandas, NumPy, SciPy
- Modeling: Scikit-Learn, XGBoost, LightGBM
- Visualization: Matplotlib, Seaborn, Tableau Public
- Deployment: Flask, Gunicorn, Render

---

## Project Structure

```text
Product_Sales_Forecasting

├── data
├── deployment
├── models
├── notebooks
├── screenshots
├── requirements.txt
├── README.md
```

---

## Author

Umar Reyaz