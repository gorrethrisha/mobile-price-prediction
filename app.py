import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("mobile_price_scaler.pkl")

st.title("📱 Mobile Price Prediction")
st.write("Enter the mobile specifications below to predict the price category.")

# Helper function for numeric input validation
def get_numeric_input(label, min_val, max_val, data_type=float):
    value = st.text_input(label)

    if value == "":
        return None

    try:
        value = data_type(value)

        if value < min_val:
            st.warning(f"{label} must be at least {min_val}.")
            return None

        if value > max_val:
            st.warning(f"{label} must be at most {max_val}.")
            return None

        return value

    except ValueError:
        st.warning(f"Please enter a valid number for {label}.")
        return None


# Numeric Inputs
battery_power = get_numeric_input("Battery Power", 500, 2500, int)
clock_speed = get_numeric_input("Clock Speed (GHz)", 0.5, 3.5, float)
fc = get_numeric_input("Front Camera (MP)", 0, 20, int)
int_memory = get_numeric_input("Internal Memory (GB)", 2, 128, int)
m_dep = get_numeric_input("Mobile Depth", 0.1, 1.0, float)
mobile_wt = get_numeric_input("Mobile Weight (g)", 80, 250, int)
n_cores = get_numeric_input("Number of Cores", 1, 8, int)
pc = get_numeric_input("Primary Camera (MP)", 0, 30, int)
px_height = get_numeric_input("Pixel Height", 0, 2500, int)
px_width = get_numeric_input("Pixel Width", 0, 2500, int)
ram = get_numeric_input("RAM (MB)", 256, 8000, int)
sc_h = get_numeric_input("Screen Height", 5, 25, int)
sc_w = get_numeric_input("Screen Width", 0, 20, int)
talk_time = get_numeric_input("Talk Time (hours)", 2, 30, int)

# Boolean Inputs using checkboxes
blue = int(st.checkbox("Bluetooth Available"))
dual_sim = int(st.checkbox("Dual SIM Supported"))
four_g = int(st.checkbox("4G Support"))
three_g = int(st.checkbox("3G Support"))
touch_screen = int(st.checkbox("Touch Screen"))
wifi = int(st.checkbox("WiFi Available"))

# Prediction Button
if st.button("Predict Price Category"):

    inputs = [
        battery_power, clock_speed, fc, int_memory,
        m_dep, mobile_wt, n_cores, pc,
        px_height, px_width, ram, sc_h,
        sc_w, talk_time
    ]

    if any(v is None for v in inputs):
        st.error("Please enter valid values for all fields.")
    else:

        input_data = pd.DataFrame({
            'battery_power': [battery_power],
            'blue': [blue],
            'clock_speed': [clock_speed],
            'dual_sim': [dual_sim],
            'fc': [fc],
            'four_g': [four_g],
            'int_memory': [int_memory],
            'm_dep': [m_dep],
            'mobile_wt': [mobile_wt],
            'n_cores': [n_cores],
            'pc': [pc],
            'px_height': [px_height],
            'px_width': [px_width],
            'ram': [ram],
            'sc_h': [sc_h],
            'sc_w': [sc_w],
            'talk_time': [talk_time],
            'three_g': [three_g],
            'touch_screen': [touch_screen],
            'wifi': [wifi]
        })

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        price_labels = {
            0: "Low Cost",
            1: "Medium Cost",
            2: "High Cost",
            3: "Very High Cost"
        }

        result = price_labels[prediction[0]]

        st.success(f"📱 Predicted Price Category: {result}")