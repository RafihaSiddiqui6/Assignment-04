import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ Try to gain some weight!"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight", "✅ You are healthy!"
    elif 25 <= bmi < 29.9:
        return "Overweight", "⚠️ Try to maintain a healthy diet & exercise!"
    else:
        return "Obese", "❗ Consult a doctor for weight management."

# Streamlit UI
st.title("BMI Calculator 💪")
st.write("### Calculate your Body Mass Index (BMI)")

# User Inputs
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, step=0.1, format="%.1f")
height = st.number_input("📏 Enter your height (m):", min_value=0.5, step=0.01, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, advice = get_bmi_category(bmi)
        st.success(f"Your BMI is: {bmi}")
        st.info(f"📌Category: {category}")
        st.warning(advice)
        st.snow() 
    else:
        st.error("❌ Please enter valid weight and height!")    
