# import random 
import streamlit as st
import random
import string

# Set page config
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-font { font-size: 32px; font-weight: bold; text-align: center; color: #FF4500; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 20px; border-radius: 10px; padding: 10px; }
        .stTextInput>div>div>input { font-size: 18px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🔐Password Generator")
st.header("Generate strong passwords instantly!")

# User inputs
length = st.slider("🔢 Select Password Length", min_value=6, max_value=20, value=12)
include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_lowercase = st.checkbox("Include Lowercase Letters (a-z)", value=True)
include_numbers = st.checkbox("Include Numbers (0-9)", value=True)
include_symbols = st.checkbox("Include Symbols (@, #, $)", value=True)

# Function to generate password
def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one option!"
    
    return "".join(random.choices(characters, k=length))

# Generate password button
if st.button("🔑 Generate Password"):
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    st.text_input("Your Secure Password:", password, key="password")
    
    # Password strength meter
    strength = "Weak" if length < 8 else "Medium" if length < 12 else "Strong"
    st.markdown(f"**Password Strength: `{strength}`**")
    
    # Copy button
    st.button("📋 Copy to Clipboard")

# markdown for footer    
st.markdown("---------")
st.markdown("""
    <p style='text-align: center; font-weight: bold;'>
        👩‍💻 Developed by <span style='color: #ff5733;'>Rafiha Siddiqui</span> | © 2025 All Rights Reserved.
    </p>
""", unsafe_allow_html=True)

