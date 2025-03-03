# Model for Copper Industry

![streamlit](https://img.shields.io/badge/streamlit-1.42.2-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-purple)
![pandas](https://img.shields.io/badge/pandas-2.2.3-red)
![pandas](https://img.shields.io/badge/numpy-2.2.3-red)
![matplotlib](https://img.shields.io/badge/matplotlib-3.10.1-blue)
![seaborn](https://img.shields.io/badge/seaborn-0.13.2-green)

## Overview

**Industrial Copper Modeling** is a predictive analytics and machine learning application that helps businesses analyze and predict key outcomes in the copper industry. 
This UI was created using Streamlit for ease of development. used light and premium looking colors for a better page.
The project consists of two primary features:
 1. **Sale Price Prediction**: Predicts the selling price of copper based on input variables such as quantity, thickness, width, country of sale, customer details, and more.
 2. **Status Prediction**: Determines whether the sale status is "Won" or "Lost" using various attributes related to the sale transaction.

## streamlit Deploynment

This application was readily was deployed in Streamlit.io
here is the link [copper-industry-model.streamlit.app](https://copper-industry-model.streamlit.app/)

---

## Features

1. **Dynamic Web Interface**
   - User-friendly Streamlit-powered GUI.
   - Inputs gathered through interactive widgets.

2. **Machine Learning-Driven Predictions**
   - Pretrained machine learning models exposed through a simple interface.
   - Sold price prediction uses regression models.
   - Status prediction uses classification models.

3. **Data Preprocessing**
   - Includes transformations such as scaling, log transformations, and one-hot encoding for categorical variables.

4. **Real-Time Analysis**
   - Swift feedback on predictions provided directly after form submission.

---

## System Requirements

1. Python: `>= 3.8`
2. Libraries:
   - `Streamlit`
   - `Scikit-learn`
   - `NumPy`
   - `Pandas`
   - `Matplotlib`
3. Supported Operating Systems:
   - Windows 10 or later
   - macOS Sonoma or later
   - Linux (Ubuntu 20.04 or later)

---

## Installation

### 1. Clone the Repository
Download the project source code by cloning the repository:
```bash
git clone https://github.com/username/Industrial-Copper-Modeling.git
cd Industrial-Copper-Modeling
```

### 2. Create a Virtual Environment
Use Python's virtual environment to isolate the project's dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate  # For macOS
# On Windows:
# .venv\Scripts\activate
```

### 3. Install the Project Requirements
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Execute the Streamlit application:
```bash
streamlit run streamlit_copper_model.py
```

The application will launch in your default browser. If it doesn’t open, navigate to the URL provided in the terminal (e.g., `http://localhost:8501`).

---

## File Descriptions

### 1. `streamlit_copper_model.py`
This file contains the **Streamlit** implementation of the application's UI and logic. It manages the following:
- Collecting user inputs via Streamlit forms.
- Transforming inputs into features for predictions.
- Using the pretrained model to predict selling price and status.

### 2. `model_function.py`
Contains all helper functions to load pretrained model artifacts, validate inputs, and apply transformations to user inputs.

Key functions:
- `load_model_artifacts(path)`:
  - Loads the model, scalers, and encoders stored as `.pkl` files.
- `input_validation()`:
  - Validates user inputs for numerical ranges and required fields.

### 3. `artifacts/`
This directory contains pre-trained models and supporting files, such as:
- `price_artifacts.pkl`: Contains model, scaler, and encoders for sale price prediction.
- `status_artifacts.pkl`: Contains model, scaler, and encoders for status prediction.

### 4. `assets/`
Stores additional static resources like logos, icons, or imagery used in the UI.

---

## Usage Instructions

### Feature 1: Sale Price Prediction
1. Open the **Sale Price Prediction** tab.
2. Fill out the following fields:
   - Status, Item Type, Country, Application, Product Reference (using dropdown menus).
   - Enter numeric values for `Quantity Tons`, `Thickness`, `Width`, and `Customer ID`.
3. Click **"PREDICT PRICE"**.
4. The predicted selling price will be displayed on the screen.

### Feature 2: Status Prediction
1. Navigate to the **Status Prediction** tab.
2. Provide the following details:
   - Quantity, Thickness, Width, Customer ID, and Selling Price (as text input).
   - Select `Item Type`, `Country`, `Application`, and `Product Reference` from dropdown menus.
3. Click **"PREDICT"**.
4. The application will display whether the sale's status is **Won** or **Lost**.

---

## Future Enhancements

1. **Expanded Predictive Models:**
   - Introduce additional features or models to predict other metrics like manufacturing time, profitability, etc.
   
2. **Improved UI/UX:**
   - Add real-time validation for inputs.
   - Provide visualizations for predicted results.

3. **Integration with Databases:**
   - Integrate with a database for historical analysis of predictions.

---

## Acknowledgments
- **Libraries Used:**
  - **Streamlit**: For an intuitive web interface.
  - **Scikit-learn**: For model preprocessing, scalers, and the core ML models.
  - **NumPy**: For matrix and numerical operations.
- **Dataset**: Not explicitly described but assumed to influence model training.

---

## License

This project is licensed under the MIT License. Make sure to provide appropriate credit and include the license when sharing or modifying the project.
