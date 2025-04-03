import streamlit as st

# Set the page title for the browser tab
st.set_page_config(page_title="Dress & Hijab Color Combination Recommender")

# Title
st.title("🧕 Dress & Hijab Color Combination Recommender")

# Description
st.write("Select your dress color and get AI-suggested hijab combinations!")

# Dress Color Options
dress_colors = {
    "Black": ["White", "Beige", "Gold", "Maroon"],
    "White": ["Pastel Pink", "Blue", "Grey", "Black"],
    "Red": ["Black", "White", "Gold", "Nude"],
    "Blue": ["White", "Silver", "Beige", "Grey"],
    "Green": ["Gold", "Brown", "White", "Navy Blue"]
}

# User Input
dress_choice = st.selectbox("Choose Your Dress Color:", list(dress_colors.keys()))

# Show Recommended Hijab Colors
if dress_choice:
    st.subheader("✨ Recommended Hijab Colors:")
    for hijab in dress_colors[dress_choice]:
        st.write(f"✅ {hijab}")
