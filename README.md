# Mobile Price Prediction

## Project Overview

This project develops a machine learning-based Mobile Price Prediction system to classify mobiles into different price categories using various hardware specification-related features.

## Objective

The primary objective of this project is to develop a machine learning model that can accurately predict mobile price categories while identifying the most effective classification algorithm for the problem.

## Dataset Information

- Total Records: **2,000**
- Total Features: **20**
- Target Variable: **price_range**

### Target Classes

- `0` → Low Cost
- `1` → Medium Cost
- `2` → High Cost
- `3` → Very High Cost

### Features Used for Training

- battery_power
- blue (Bluetooth)
- clock_speed (Processor speed)
- dual_sim
- fc (Front Camera)
- four_g
- int_memory (Internal memory in GB)
- m_dep (Mobile depth in cm)
- mobile_wt (Weight in gm)
- n_cores (Processor Core Count)
- pc (Primary Camera)
- px_height (Pixel Resolution Height)
- px_width (pixel Resolution Width)
- ram
- sc_h (Screen Height)
- sc_w (Screen Width)
- talk_time
- three_g
- touch_screen
- wifi

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Dataset Overview
2. Exploratory Data Analysis (EDA)
3. Feature and Target Separation
4. Train-Test Split
5. Feature Scaling
6. Model Training and Evaluation
   - Logistic Regression
   - Decision Tree Classifier
   - Random Forest Classifier
   - Support Vector Classifier (SVC)
7. Model Comparison
8. Final Model Selection
9. Prediction

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 96.5% | 97% | 96% | 96% |
| Decision Tree Classifier | 83.0% | 83% | 83% | 83% |
| Random Forest Classifier | 88.0% | 88% | 88% | 88% |
| Support Vector Classifier (SVC) | 89.5% | 90% | 90% | 90% |

## Final Model Selection

Logistic Regression, Decision Tree, Random Forest Classifier and Support Vector Classifier (SVC) models were trained and evaluated for mobile price prediction. Although SVC, Decision Tree, and Random Forest achieved good performance, Logistic Regression demonstrated superior ability in correctly classifying mobile phones across all price categories.

Among all the models, Logistic Regression achieved the best overall performance with an accuracy of 96.5% while producing the fewest classification errors.

Since accurate price prediction is important for market analysis and business decision-making, **the Logistic Regression model was selected as the final model for Mobile Phone Price Prediction.**

## Streamlit Web Application

A Streamlit-based web application was developed to provide an interactive interface for Mobile Price Prediction.

The application allows users to enter mobile hardware specifications and instantly predicts the corresponding mobile price category using the trained machine learning model.

## Project Files

- `Mobile Price Prediction.ipynb` - Complete notebook containing data preprocessing, model training, and evaluation..
- `app.py` - Streamlit web application for mobile price prediction.
- `mobile_price_model.pkl` - Saved trained machine learning model.
- `mobile_price_scaler.pkl` - Saved feature scaler used during preprocessing.
- `requirements.txt` - List of project dependencies.
- `README.md` - Project documentation.

## Conclusion

A Mobile Price Prediction system was successfully developed and multiple machine learning algorithms were trained and evaluated for prediction performance. 

The developed system can assist users in estimating mobile price categories based on device specifications and hardware features.


