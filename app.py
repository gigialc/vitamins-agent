import streamlit as st
import pandas as pd
import random
from PIL import Image

# Custom color scheme
PURPLE_LIGHT = "#E6E6FA"  # Lavender
PURPLE_MAIN = "#9370DB"   # Medium Purple

def load_vitamin_data():
    return pd.read_csv('data.csv')

def get_emoji_for_vitamin(vitamin):
    emoji_dict = {
        "Vitamin D": "☀️", "Vitamin B12": "🥩", "Iron": "💪",
        "Vitamin C": "🍊", "Vitamin A": "🥕", "Magnesium": "🥜",
        "Vitamin B6": "🍌", "Folate": "🥬", "Vitamin E": "🥑",
        "Zinc": "🦪", "Calcium": "🥛", "Omega-3": "🐟"
    }
    return emoji_dict.get(vitamin, "💊")

def main():
    st.set_page_config(page_title="Verve", page_icon="💜", layout="wide")
    
    # Custom CSS for purple theme
    st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            background-color: {PURPLE_LIGHT};
        }}
        .stButton>button {{
            background-color: {PURPLE_MAIN};
            color: white;
        }}
        .stSelectbox [data-baseweb="select"] {{
            background-color: {PURPLE_LIGHT};
        }}
    </style>
    """, unsafe_allow_html=True)

    st.title("💜 Check Your Nutritional Wellness with verve")
    st.write("Empowering women to understand and nurture their bodies through optimal nutrition.")

    # User name input
    user_name = st.text_input("What's your name?", "")
    if user_name:
        st.write(f"Welcome to verve, {user_name}! Let's explore your nutritional wellness together.")

    # Load data
    vitamin_data = load_vitamin_data()

    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔍 Select the signs your body is showing:")
        all_symptoms = sorted(set([symptom.strip() for symptoms in vitamin_data['Symptoms'] for symptom in symptoms.split(',')]))
        selected_symptoms = st.multiselect("Symptoms", all_symptoms)


    life_stage = st.selectbox("Which life stage are you in?", ["Adolescence", "Reproductive Age", "Pregnancy", "Postpartum", "Menopause", "Post-menopause"])

    if st.button("Reveal My Nutritional Insights"):
        if selected_symptoms:
            st.subheader("🌸 Your Personalized Nutritional Insights:")
            found_deficiencies = False
            for _, row in vitamin_data.iterrows():
                if any(symptom in row['Symptoms'] for symptom in selected_symptoms):
                    found_deficiencies = True
                    with st.expander(f"{get_emoji_for_vitamin(row['Vitamin'])} {row['Vitamin']}"):
                        st.write(f"**Signs:** {row['Symptoms']}")
                        st.write(f"**Nourishment Tips:** {row['Solutions']}")
                        
                        # Women's health facts
                        women_health_facts = [
                            f"Women's Wellness: {row['Vitamin']} is essential for {random.choice(['hormonal balance', 'bone density', 'reproductive health', 'energy levels'])}!",
                            f"Did you know? Women often need more {row['Vitamin']} during {random.choice(['pregnancy', 'menstruation', 'menopause'])}.",
                            f"Empowering Fact: Adequate {row['Vitamin']} intake can help with {random.choice(['PMS symptoms', 'fertility', 'postpartum recovery', 'menopausal comfort'])}!"
                        ]
                        st.info(random.choice(women_health_facts))
            
            if not found_deficiencies:
                st.success("Wonderful news! We didn't detect any clear signs of vitamin deficiencies. Keep nurturing your body with balanced nutrition!")
        else:
            st.warning("Oops! We need some information to provide insights. Please select at least one symptom.")
    
    # Personalized tips based on life stage
    if user_name and life_stage:
        st.subheader(f"💖 Tailored Wellness Tips for {user_name}")
        life_stage_tips = {
            "Adolescence": "Focus on calcium and vitamin D for strong bones, and iron for healthy blood.",
            "Reproductive Age": "Ensure adequate folate intake, especially if planning for pregnancy.",
            "Pregnancy": "Folic acid, iron, and omega-3s are crucial for your baby's development.",
            "Postpartum": "Continue with prenatal vitamins and focus on iron-rich foods to replenish your body.",
            "Menopause": "Calcium and vitamin D are important for bone health as estrogen levels decrease.",
            "Post-menopause": "Maintain heart health with omega-3s and antioxidant-rich foods."
        }
        st.write(life_stage_tips[life_stage])

    # Self-care reminder
    st.subheader("🌺 Your Daily Self-Care Reminder")
    self_care_tips = [
        "Take a moment for yourself today. You deserve it!",
        "Nourish your body, mind, and soul. They're all connected.",
        "Remember, your health is an investment, not an expense.",
        "Stay hydrated! Water is essential for every cell in your body.",
        "Prioritize sleep. It's your body's time to heal and rejuvenate."
    ]
    st.write(random.choice(self_care_tips))

    # Disclaimer
    st.caption("Disclaimer: verve is for educational purposes only. Always consult with a healthcare professional for medical advice.")

if __name__ == "__main__":
    main()