# Eco-Friendly Product Sales Prediction | Machine Learning & Streamlit

## Project Overview

Eco-Friendly Product Sales Prediction is an end-to-end Machine Learning project that forecasts weekly sales of eco-friendly products using historical business, marketing, seasonal, and customer behavior data.

The project includes data preprocessing, feature engineering, model training, evaluation, and deployment through an interactive Streamlit web application. Multiple regression algorithms were compared, and the best-performing model was selected for production use.

---

## Live Demo

**Streamlit Application:**
[https://linearregression-xstnzqsg3twcretyibre6z.streamlit.app/]

---

## Key Features

* Weekly Sales Prediction
* Monthly Sales Estimation
* Quarterly Sales Estimation
* Yearly Sales Estimation
* Multiple Regression Model Comparison
* Best Model Selection
* Automated Feature Engineering
* Interactive Streamlit Dashboard
* End-to-End Machine Learning Pipeline

---

## Dataset Features

### Business Information

* Region
* Week Start Date

### Marketing & Customer Information

* Marketing Spend
* Store Visits
* Google Trend Score
* Holiday Flag

### Environmental Information

* Average Temperature

### Target Variable

* Weekly Sales

---

## Feature Engineering

Several custom features were created to improve model performance.

### Time-Based Features

* Year
* Month
* Quarter
* Week Number

### Interaction Features

**Marketing × Google Trend**

```python
marketing_spend * google_trend_score
```

Measures the combined effect of marketing campaigns and online customer interest.

**Marketing × Store Visits**

```python
marketing_spend * store_visits
```

Represents the relationship between marketing investment and customer footfall.

**Holiday Marketing**

```python
marketing_spend * holiday_flag
```

Captures the impact of marketing campaigns during holiday periods.

**Visit Trend Ratio**

```python
store_visits / (google_trend_score + 1)
```

Measures how effectively online search interest converts into store visits.

---

## Machine Learning Models Evaluated

| Model                         | Status                |
| ----------------------------- | --------------------- |
| Linear Regression             | Evaluated             |
| Ridge Regression              | Evaluated             |
| Lasso Regression              | Evaluated             |
| ElasticNet Regression         | Evaluated             |
| K-Nearest Neighbors Regressor | Evaluated             |
| Polynomial Regression         | Best Performing Model |

---

## Best Performing Model

### Polynomial Regression

Polynomial Regression achieved the highest predictive performance and was selected as the final production model.

### Evaluation Metrics

| Metric                         | Score  |
| ------------------------------ | ------ |
| R² Score                       | 0.9048 |
| Adjusted R² Score              | 0.9002 |
| Mean Absolute Error (MAE)      | 14.95  |
| Mean Squared Error (MSE)       | 358.95 |
| Root Mean Squared Error (RMSE) | 18.95  |

---

## Business Impact

This solution helps businesses:

* Forecast future eco-friendly product sales
* Optimize marketing expenditure
* Understand seasonal sales patterns
* Improve inventory planning
* Support data-driven decision-making
* Enhance demand forecasting accuracy

---

## Technology Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn

### Deployment

* Streamlit

### Model Storage

* Joblib

---

## Application Screenshots

<h3 align="center">Home Page</h3>
<p align="center">
  <img src="Images/Home Page.png" width="800">
</p>

<h3 align="center">Prediction Result</h3>
<p align="center">
  <img src="Images/Prediction Image.png" width="800">
</p>

## Application Output

The Streamlit application provides:

* Weekly Sales Prediction
* Monthly Sales Estimation
* Quarterly Sales Estimation
* Yearly Sales Estimation
* Input Summary Dashboard
* Interactive Prediction Interface

---

## Future Improvements

* Hyperparameter Tuning
* Ensemble Learning Models
* Real-Time Data Integration
* Cloud Deployment
* Advanced Business Analytics Dashboard

---

## Author

**Hiren Vaghela**

Data Science Enthusiast | Data Analyst

LinkedIn: https://www.linkedin.com/in/hiren-vaghela-dev/

---

If you found this project useful, consider giving the repository a star.
