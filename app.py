import streamlit as st
import numpy as np
import requests
import joblib
from io import BytesIO
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# -------------------------------
# Load the trained model from Hugging Face
# -------------------------------
@st.cache_resource
def load_model_from_hf():
    url = "https://huggingface.co/kanakrajarora/random_forest_ipl_score/resolve/main/model.pkl"  # 🔹 replace filename if needed
    #st.info("Downloading model from Hugging Face Hub... Please wait ⏳")
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"❌ Failed to download model. Status code: {response.status_code}")
        st.stop()
    return joblib.load(BytesIO(response.content))

model = load_model_from_hf()

# -------------------------------
# Team mapping (2025 → old teams)
# -------------------------------
team_map = {
    'Delhi Capitals': 'Delhi Daredevils',
    'Punjab Kings': 'Kings XI Punjab',
    'Gujarat Titans': 'Sunrisers Hyderabad',   # Similar balance
    'Lucknow Super Giants': 'Rajasthan Royals',
    'Chennai Super Kings': 'Chennai Super Kings',
    'Mumbai Indians': 'Mumbai Indians',
    'Kolkata Knight Riders': 'Kolkata Knight Riders',
    'Royal Challengers Bangalore': 'Royal Challengers Bangalore',
    'Rajasthan Royals': 'Rajasthan Royals',
    'Sunrisers Hyderabad': 'Sunrisers Hyderabad'
}

teams = list(team_map.keys())

# -------------------------------
# Streamlit App UI
# -------------------------------
st.title("🏏 IPL Score Predictor")
st.markdown("### Predict the First Innings Final Score based on Live Match Stats")

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Batting Team', teams)
with col2:
    bowling_team = st.selectbox('Bowling Team', teams)

# Prevent selecting same team
if batting_team == bowling_team:
    st.error("⚠️ Batting and Bowling team cannot be the same!")
    st.stop()

# Match inputs
col3, col4, col5 = st.columns(3)
with col3:
    overs = st.number_input('Overs completed (e.g., 10.2)', min_value=5.0, max_value=19.5, step=0.1)
with col4:
    runs = st.number_input('Current Runs', min_value=0)
with col5:
    wickets = st.number_input('Wickets fallen', min_value=0, max_value=10)

col6, col7 = st.columns(2)
with col6:
    runs_in_prev_5 = st.number_input('Runs scored in previous 5 overs', min_value=0)
with col7:
    wickets_in_prev_5 = st.number_input('Wickets fallen in previous 5 overs', min_value=0, max_value=5)

# -------------------------------
# Prediction
# -------------------------------
if st.button('Predict Final Score'):
    # Map new teams → old ones
    bat = team_map[batting_team]
    bowl = team_map[bowling_team]

    # One-hot encoding based on OLD 8 teams
    teams_old = [
        'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
        'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
        'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
    ]

    temp_array = []

    # Batting team one-hot
    for team in teams_old:
        temp_array.append(1 if team == bat else 0)

    # Bowling team one-hot
    for team in teams_old:
        temp_array.append(1 if team == bowl else 0)

    # Append numeric inputs
    temp_array.extend([overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5])

    # Convert to numpy array
    final_input = np.array([temp_array])

    # Predict
    prediction = int(model.predict(final_input)[0])
    lower_limit = prediction - 10
    upper_limit = prediction + 5

    st.success(f"🏏 Predicted Final Score Range: **{lower_limit} – {upper_limit}**")


