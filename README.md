 # IPL Score Predictor (2025)

A **Streamlit web app** that predicts the **final score of an IPL first innings** based on current match conditions. Built with **Random Forest Regression** and deployed on **Streamlit Cloud**.

---

## Features

* Predicts first innings final score from mid-match stats
* Supports updated **IPL 2025 teams** with internal mapping to historical teams
* Real-time, interactive UI built using **Streamlit**
* Model trained using **Random Forest Regressor** for highest accuracy
* Backend model loaded from **Hugging Face** for efficient access

---

## Model Info

* **Model Type:** RandomForestRegressor
* **Evaluation Metrics:**

  * MAE: 4.45
  * MSE: 58.02
  * RMSE: 7.61
* **Dataset:** IPL match data 
* **Trained Using:** Python (scikit-learn, pandas, numpy)

---

## How It Works

### Input Parameters

* **Batting Team** (Dropdown)
* **Bowling Team** (Dropdown)
* **Overs Completed** (Float: 5.0–19.5)
* **Runs Scored** (Integer)
* **Wickets Fallen** (0–10)
* **Runs in Previous 5 Overs**
* **Wickets in Previous 5 Overs**

### Output

* Predicted **Final Score Range** = [Prediction − 10, Prediction + 5]

---

## Tech Stack

| Component | Technology                   |
| --------- | ---------------------------- |
| Frontend  | Streamlit                    |
| Model     | Random Forest (scikit-learn) |
| Backend   | Python 3.12                  |
| Hosting   | Streamlit Cloud              |
| Data      | IPL CSV Dataset   |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/kanakrajarora/ipl_score_predictor.git
cd ipl_score_predictor

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## Requirements

```
numpy==2.3.4
streamlit==1.44.0
pandas==2.2.2
scikit-learn==1.6.1
joblib==1.4.2
requests==2.32.3
```

---

## Deployment

The app is deployed live at:
 **[iplscorepredict.streamlit.app](https://iplscorepredict.streamlit.app)**

Model file hosted on Hugging Face:
 **[kanakrajarora/random_forest_ipl_score](https://huggingface.co/kanakrajarora/random_forest_ipl_score)**

---

## Author

**Kanak Raj Arora**
📧 Email: [kanakrajarora@gmail.com](mailto:kanakrajarora@gmail.com)

---

## Future Improvements

* Integrate live IPL data for dynamic predictions
* Add visualization for run rate progression
* Deploy API endpoint for mobile integration

---

> “Predicting the game before it ends — one over at a time!” 🏏
