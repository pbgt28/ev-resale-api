import streamlit as st
import requests

st.set_page_config(
    page_title="EV Resale Value Estimator",
    page_icon="🚗",
    layout="wide"
)

API_URL = "https://ev-resale-api.onrender.com/predict"

VEHICLE_CATALOG = {
    'Tesla': ['Model 3', 'Model Y', 'Model S', 'Model X'],
    'BMW': ['i4', 'iX', 'i3'],
    'Audi': ['e-tron', 'Q4 e-tron'],
    'Ford': ['Mustang Mach-E', 'F-150 Lightning'],
    'Hyundai': ['Ioniq 5', 'Kona Electric'],
    'Kia': ['EV6', 'Niro EV'],
    'Mercedes': ['EQS', 'EQC'],
    'Nissan': ['Leaf', 'Ariya'],
    'Volkswagen': ['ID.4', 'ID.3'],
    'Chevrolet': ['Bolt EV', 'Bolt EUV']
}

st.title("🚗 Electric Vehicle Resale Value Predictor")
st.markdown("Estimate the market resale value of an electric vehicle using machine learning.")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📋 Vehicle Identity")
    company = st.selectbox("Manufacturer", list(VEHICLE_CATALOG.keys()))
    model = st.selectbox("Model", VEHICLE_CATALOG[company])
    year = st.number_input("Manufacture Year", min_value=2015, max_value=2026, value=2022)
    vehicle_type = st.selectbox("Vehicle Type", ["Sedan", "SUV", "Hatchback", "Truck"])
    region = st.selectbox("Region", ["North America", "Europe", "Asia", "Australia"])
    usage_type = st.selectbox("Usage Type", ["Personal", "Commercial", "Fleet"])

with col2:
    st.subheader("🔋 Battery & Performance")
    battery_capacity = st.number_input("Battery Capacity (kWh)", min_value=20.0, max_value=150.0, value=81.3)
    battery_health = st.slider("Battery Health (%)", min_value=60.0, max_value=100.0, value=85.6)
    range_km = st.number_input("Driving Range (km)", min_value=100.0, max_value=800.0, value=481.0)
    charging_power = st.number_input("Charging Power (kW)", min_value=10.0, max_value=350.0, value=212.8)
    charging_time = st.number_input("Charging Time (hours)", min_value=0.1, max_value=15.0, value=1.2)
    charge_cycles = st.number_input("Charge Cycles", min_value=50, max_value=3000, value=1100)
    energy_consumption = st.number_input("Consumption (kWh/100km)", min_value=10.0, max_value=30.0, value=18.5)

with col3:
    st.subheader("⚙️ Usage & Cost Metrics")
    mileage_km = st.number_input("Total Distance Covered (km)", min_value=1000.0, max_value=300000.0, value=125000.0)
    avg_speed = st.number_input("Average Speed (km/h)", min_value=20.0, max_value=120.0, value=65.0)
    max_speed = st.number_input("Max Speed (km/h)", min_value=100.0, max_value=260.0, value=190.0)
    acceleration = st.number_input("0-100 km/h (seconds)", min_value=2.0, max_value=12.0, value=6.7)
    temperature = st.number_input("Avg Operating Temp (°C)", min_value=-20.0, max_value=45.0, value=15.0)
    co2_saved = st.number_input("CO2 Saved (tons)", min_value=0.5, max_value=35.0, value=15.0)
    maintenance_cost = st.number_input("Annual Maintenance (USD)", min_value=100.0, max_value=3000.0, value=1100.0)
    insurance_cost = st.number_input("Annual Insurance (USD)", min_value=400.0, max_value=3000.0, value=1500.0)
    electricity_cost = st.number_input("Electricity Cost ($/kWh)", min_value=0.05, max_value=0.50, value=0.22)
    monthly_charging = st.number_input("Monthly Charging Cost (USD)", min_value=10.0, max_value=1800.0, value=350.0)

st.divider()

if st.button("🔮 Predict Resale Value", type="primary", use_container_width=True):
    payload = {
        "Company": company,
        "Model": model,
        "Year": int(year),
        "Region": region,
        "Vehicle_Type": vehicle_type,
        "Battery_Capacity_kWh": float(battery_capacity),
        "Battery_Health_%": float(battery_health),
        "Range_km": float(range_km),
        "Charging_Power_kW": float(charging_power),
        "Charging_Time_hr": float(charging_time),
        "Charge_Cycles": int(charge_cycles),
        "Energy_Consumption_kWh_per_100km": float(energy_consumption),
        "Total_Distance_Covered_km": float(mileage_km),
        "Avg_Speed_kmh": float(avg_speed),
        "Max_Speed_kmh": float(max_speed),
        "Acceleration_0_100_kmh_sec": float(acceleration),
        "Temperature_C": float(temperature),
        "Usage_Type": usage_type,
        "CO2_Saved_tons": float(co2_saved),
        "Maintenance_Cost_USD": float(maintenance_cost),
        "Insurance_Cost_USD": float(insurance_cost),
        "Electricity_Cost_USD_per_kWh": float(electricity_cost),
        "Monthly_Charging_Cost_USD": float(monthly_charging)
    }

    with st.spinner("Connecting to model and calculating resale value..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=120)
            if response.status_code == 200:
                result = response.json()
                price = result["predicted_resale_value_USD"]
                st.balloons()
                st.success(f"### 🏷️ Estimated Resale Value: **${price:,.2f} USD**")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to API: {e}")
