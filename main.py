from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(title="EV Resale Value Prediction API")

# Load artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")
feature_columns = joblib.load("feature_columns.pkl")


class EVInput(BaseModel):
    Company: str
    Model: str
    Year: int
    Region: str
    Vehicle_Type: str
    Battery_Capacity_kWh: float
    Battery_Health_pct: float = Field(..., alias="Battery_Health_%")
    Range_km: float
    Charging_Power_kW: float
    Charging_Time_hr: float
    Charge_Cycles: int
    Energy_Consumption_kWh_per_100km: float
    Total_Distance_Covered_km: float
    Avg_Speed_kmh: float
    Max_Speed_kmh: float
    Acceleration_0_100_kmh_sec: float
    Temperature_C: float
    Usage_Type: str
    CO2_Saved_tons: float
    Maintenance_Cost_USD: float
    Insurance_Cost_USD: float
    Electricity_Cost_USD_per_kWh: float
    Monthly_Charging_Cost_USD: float

    model_config = {
        "populate_by_name": True
    }


@app.get("/")
def home():
    return {"message": "EV Resale Value Prediction API is running"}


@app.post("/predict")
def predict(data: EVInput):
    # Convert input using aliases so "Battery_Health_%" matches training
    input_dict = data.model_dump(by_alias=True)
    df = pd.DataFrame([input_dict])

    # Encode categorical columns
    categorical_columns = ["Company", "Model", "Region", "Vehicle_Type", "Usage_Type"]
    for col in categorical_columns:
        df[col] = encoders[col].transform(df[col])

    # Ensure feature alignment
    df = df[feature_columns]

    # Scale features and predict
    scaled_data = scaler.transform(df)
    prediction = model.predict(scaled_data)[0]

    return {
        "predicted_resale_value_USD": round(float(prediction), 2)
    }
