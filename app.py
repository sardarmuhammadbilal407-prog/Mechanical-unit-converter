import streamlit as st
import math

st.set_page_config(
    page_title="Mechanical Engineering Scientific Calculator",
    page_icon="⚙️",
    layout="wide"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>
    .main {
        background-color: #2f2f2f;
    }
    h1, h2, h3 {
        color: #d6d6d6;
    }
    .stButton>button {
        background-color: #556b2f;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stTextInput>div>div>input {
        background-color: #1f1f1f;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("⚙️ Mechanical Engineering Scientific Calculator")
st.subheader("UET Taxila Inspired Theme | Grey • Black • Olive")

st.markdown("### 🏛 Mechanical Engineering Logo Area")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Gear_icon.svg/512px-Gear_icon.svg.png",
    width=120
)

# ---------- Sidebar ----------
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose Tool",
    ["Scientific Calculator", "Density Checker", "Unit Converter"]
)

# ---------- Scientific Calculator ----------
if option == "Scientific Calculator":
    st.header("Scientific Calculator")

    expression = st.text_input(
        "Enter Expression",
        placeholder="Example: sin(30) + sqrt(16) + 5*10"
    )

    if st.button("Calculate"):
        try:
            allowed_names = {
                k: getattr(math, k) for k in dir(math) if not k.startswith("_")
            }
            allowed_names["abs"] = abs
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Invalid Expression: {e}")

# ---------- Density Checker ----------
elif option == "Density Checker":
    st.header("Engineering Level Density Checker")

    mass = st.number_input("Enter Mass (kg)", min_value=0.0, format="%.4f")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0001, format="%.4f")

    if st.button("Check Density"):
        density = mass / volume
        st.success(f"Density = {density:.4f} kg/m³")

        if density < 1000:
            st.info("Material is likely light (similar to wood/plastic).")
        elif density < 8000:
            st.info("Material is medium density (engineering metals range).")
        else:
            st.info("Material is high density (heavy alloy/industrial material).")

# ---------- Unit Converter ----------
elif option == "Unit Converter":
    st.header("100+ Unit Converter")

    category = st.selectbox(
        "Select Category",
        ["Length", "Mass", "Temperature", "Pressure", "Energy"]
    )

    conversions = {
        "Length": {
            "meter": 1,
            "kilometer": 1000,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.34
        },
        "Mass": {
            "kg": 1,
            "gram": 0.001,
            "mg": 0.000001,
            "ton": 1000,
            "lb": 0.453592,
            "ounce": 0.0283495
        },
        "Pressure": {
            "Pa": 1,
            "kPa": 1000,
            "MPa": 1000000,
            "bar": 100000,
            "atm": 101325,
            "psi": 6894.76
        },
        "Energy": {
            "J": 1,
            "kJ": 1000,
            "MJ": 1000000,
            "cal": 4.184,
            "kWh": 3600000
        }
    }

    if category != "Temperature":
        units = list(conversions[category].keys())
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        value = st.number_input("Enter Value", format="%.6f")

        if st.button("Convert"):
            base_value = value * conversions[category][from_unit]
            converted = base_value / conversions[category][to_unit]
            st.success(f"Converted Value: {converted:.6f} {to_unit}")

    else:
        temp_type = st.selectbox("Temperature Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        value = st.number_input("Enter Temperature", format="%.2f")

        if st.button("Convert Temperature"):
            if temp_type == "Celsius to Fahrenheit":
                result = (value * 9/5) + 32
                st.success(f"{result:.2f} °F")
            else:
                result = (value - 32) * 5/9
                st.success(f"{result:.2f} °C")
