[README.md](https://github.com/user-attachments/files/32604939/README.md)
# 🚗 Electric Vehicle Resale Value Predictor

An end-to-end machine learning project that predicts the **resale value of electric vehicles (EVs)** using vehicle specifications, battery health, performance, usage patterns, and operating-cost features.

The project includes **data analysis, exploratory data analysis (EDA), machine learning model development, model evaluation, and an interactive Streamlit web application** deployed to the cloud.

## 🌐 Live Demo

**Streamlit App:** https://ev-resale-api-wlc3cnxggcs693p2bfq9bh.streamlit.app/

---

## 📌 Project Overview

Electric vehicle resale value depends on several factors, including the vehicle's age, manufacturer, model, battery condition, driving range, mileage, performance, charging characteristics, and ownership costs.

This project uses historical EV data to build regression models that learn relationships between these characteristics and the vehicle's resale value.

The trained model is integrated into an interactive Streamlit application where users can enter EV specifications and receive an estimated resale value.

---

## ✨ Key Features

- 📊 Exploratory Data Analysis (EDA)
- 🔍 Correlation and feature analysis
- 📈 Data visualization
- 🤖 Multiple machine learning regression models
- ⚙️ Categorical encoding and feature scaling
- 📏 Model evaluation using MSE, RMSE, MAE, and R²
- 🚗 Interactive EV resale-value prediction
- 🖥️ Streamlit web application
- ☁️ Cloud deployment
- 💾 Saved model and preprocessing artifacts

---

## 📊 Dataset

The dataset contains:

- **3,000 records**
- **25 columns**
- Target variable: `Resale_Value_USD`

### Feature Categories

#### 🚘 Vehicle Identity

- Manufacturer
- Model
- Manufacture Year
- Vehicle Type
- Region
- Usage Type

#### 🔋 Battery & Performance

- Battery Capacity (kWh)
- Battery Health (%)
- Driving Range (km)
- Charging Power (kW)
- Charging Time (hours)
- Charge Cycles
- Consumption (kWh/100 km)

#### ⚙️ Usage & Performance

- Total Distance Covered (km)
- Average Speed (km/h)
- Maximum Speed (km/h)
- 0–100 km/h (seconds)

#### 🌡️ Operating & Environmental Factors

- Average Operating Temperature (°C)
- CO₂ Saved (tons)

#### 💰 Cost Metrics

- Annual Maintenance (USD)
- Annual Insurance (USD)
- Electricity Cost ($/kWh)
- Monthly Charging Cost (USD)

#### 🎯 Target Variable

`Resale_Value_USD`

---

## 🔬 Exploratory Data Analysis

The project performs exploratory analysis to understand the structure of the EV dataset and relationships between features and resale value.

The analysis includes:

- Dataset inspection
- Descriptive statistics
- Missing-value analysis
- Numerical feature analysis
- Feature distributions
- Correlation analysis
- Correlation heatmap
- Outlier analysis
- Feature relationships
- Feature importance analysis
- Actual vs. predicted analysis
- Residual analysis

---

## ⚙️ Data Preprocessing

The following preprocessing steps were used before model training.

### 1. Categorical Encoding

Categorical variables were transformed into numerical representations using **Label Encoding**.

### 2. Feature Scaling

Numerical features were standardized using:

```python
StandardScaler()
```

### 3. Train-Test Split

The dataset was divided into:

- **80% training data**
- **20% testing data**

using:

```python
random_state = 42
```

---

## 🤖 Machine Learning Models

Three regression algorithms were trained and evaluated:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

### Model Comparison

| Model | Test R² |
|---|---:|
| Linear Regression | **0.90** |
| Random Forest | 0.89 |
| Decision Tree | 0.88 |

The models were evaluated using the same train-test split and regression evaluation metrics.

---

## 📏 Evaluation Metrics

The following metrics were used to evaluate model performance:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted resale values.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Measures the square root of MSE and expresses prediction error in the same unit as the target variable.

### R² Score

Measures the proportion of variation in resale value explained by the model.

---

## 🖥️ Streamlit Application

The trained machine learning model was integrated into an interactive Streamlit application:

### 🚗 Electric Vehicle Resale Value Predictor

The application is divided into three main sections.

### Vehicle Identity

Users can enter:

- Manufacturer
- Model
- Manufacture Year
- Vehicle Type
- Region
- Usage Type

### Battery & Performance

Users can enter:

- Battery Capacity
- Battery Health
- Driving Range
- Charging Power
- Charging Time
- Charge Cycles
- Energy Consumption

### Usage & Cost Metrics

Users can enter:

- Total Distance Covered
- Average Speed
- Maximum Speed
- 0–100 km/h Time
- Average Operating Temperature
- CO₂ Saved
- Annual Maintenance
- Annual Insurance
- Electricity Cost
- Monthly Charging Cost

After entering the required information, users can select:

**🔮 Predict Resale Value**

The application then processes the inputs using the trained preprocessing pipeline and returns an estimated EV resale value.

---

## 🏗️ Project Workflow

```text
                    EV Dataset
                        │
                        ▼
                Data Inspection
                        │
                        ▼
                 Exploratory Data
                     Analysis
                        │
                        ▼
                Data Preprocessing
                  ┌─────┴─────┐
                  │           │
                  ▼           ▼
             Encoding     Scaling
                  │           │
                  └─────┬─────┘
                        ▼
                 Train-Test Split
                        │
                        ▼
                  Model Training
             ┌──────────┼──────────┐
             ▼          ▼          ▼
        Linear       Decision    Random
       Regression      Tree       Forest
             │          │          │
             └──────────┼──────────┘
                        ▼
                 Model Evaluation
                        │
                        ▼
              Model Serialization
                        │
                        ▼
                Streamlit Application
                        │
                        ▼
             EV Resale Value Prediction
```

---

## 💾 Saved Model Artifacts

The application uses serialized machine learning and preprocessing objects.

Typical project artifacts include:

```text
model.pkl
scaler.pkl
encoders.pkl
feature_columns.pkl
```

### `model.pkl`

Stores the trained regression model.

### `scaler.pkl`

Stores the fitted `StandardScaler` used to transform numerical features.

### `encoders.pkl`

Stores the categorical encoders required to transform categorical inputs.

### `feature_columns.pkl`

Stores the expected feature structure and ordering used by the model during prediction.

These artifacts allow the deployed application to process new user inputs consistently with the training pipeline.

---

## 📁 Project Structure

```text
EV-Resale-Value-Predictor/
│
├── EV.ipynb
├── electric_vehicle_analytics.csv
│
├── model.pkl
├── scaler.pkl
├── encoders.pkl
├── feature_columns.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Web Application

- Streamlit

### Model Persistence

- Joblib

### Development

- Google Colab
- Git
- GitHub

### Deployment

- Streamlit Cloud

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EV-Resale-Value-Predictor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 📦 Requirements

The project uses Python libraries including:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
```

The complete dependency list is maintained in `requirements.txt`.

---

## 🔮 Example Input

Example EV configuration:

```text
Manufacturer: Tesla
Model: Model 3
Manufacture Year: 2022
Vehicle Type: Sedan
Region: North America
Usage Type: Personal

Battery Capacity: 81.30 kWh
Battery Health: 85.60%
Driving Range: 481 km
Charging Power: 212.80 kW
Charging Time: 1.20 hours
Charge Cycles: 1100
Consumption: 18.50 kWh/100 km

Total Distance Covered: 125000 km
Average Speed: 65 km/h
Maximum Speed: 190 km/h
0–100 km/h: 6.70 seconds

Average Operating Temperature: 15°C
CO₂ Saved: 15 tons
Annual Maintenance: $1100
Annual Insurance: $1500
Electricity Cost: $0.22/kWh
Monthly Charging Cost: $350
```

The application uses these inputs to generate an estimated resale value.

---

## 📈 Model Performance

The test-set R² scores obtained during model evaluation were:

| Model | R² Score |
|---|---:|
| Linear Regression | **0.90** |
| Random Forest | **0.89** |
| Decision Tree | **0.88** |

Additional metrics including **MAE, MSE, and RMSE** were also calculated during model evaluation.

---

## ⚠️ Limitations

The predicted resale value is a machine learning estimate based on the available dataset.

Actual EV resale prices can also be affected by factors that may not be fully represented in the dataset, such as:

- Local market demand
- Vehicle condition
- Accident history
- Regional pricing differences
- Battery replacement requirements
- Dealer pricing
- Market fluctuations
- Individual vehicle history

Therefore, the prediction should be interpreted as an **estimated resale value**, not a guaranteed market price.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Hyperparameter tuning
- Cross-validation
- Gradient Boosting and XGBoost models
- Advanced feature engineering
- SHAP-based model explainability
- Prediction uncertainty estimates
- Interactive model explanations
- Historical EV price trends
- Integration with real-time EV marketplace data
- Automated model retraining
- Docker-based deployment
- Improved handling of unseen categorical values

---

## 🎯 Learning Outcomes

This project provided practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Data visualization
- Regression modeling
- Model comparison
- Categorical encoding
- Feature scaling
- Model evaluation
- Model serialization
- Streamlit development
- Machine learning deployment

---

## 👨‍💻 Author

### Prince Bhagat

**B.Tech — Artificial Intelligence**  
**Amity University Lucknow**

#### Technical Skills Demonstrated

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Machine Learning
Regression
Exploratory Data Analysis
Streamlit
Model Deployment
Git & GitHub
