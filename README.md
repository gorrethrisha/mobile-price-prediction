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
| Logistic Regression | 0.965 | 0.97 | 0.96 | 0.96 |
| Decision Tree Classifier | 0.830 | 0.83 | 0.83 | 0.83 |
| Random Forest Classifier | 0.880 | 0.88 | 0.88 | 0.88 |
| Support Vector Classifier (SVC) | 0.895 | 0.90 | 0.90 | 0.90 |

## Final Model Selection

Logistic Regression, Decision Tree, Random Forest Classifier and Support Vector Classifier (SVC) models were trained and evaluated for mobile price prediction. Although SVC, Decision Tree, and Random Forest achieved good performance, Logistic Regression demonstrated superior ability in correctly classifying mobile phones across all price categories.

Among all the models, Logistic Regression achieved the best overall performance with an accuracy of 96.5% while producing the fewest classification errors.

Since accurate price prediction is important for market analysis and business decision-making, **the Logistic Regression model was selected as the final model for Mobile Phone Price Prediction.**

## Conclusion

A Mobile Price Prediction system was successfully developed and multiple machine learning algorithms were trained and evaluated for prediction performance. The developed system can assist manufacturers, retailers, and consumers in estimating mobile price categories based on device specifications and hardware features.
