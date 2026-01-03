# 🎬 Simple Movie Recommendation System

This project is a **content-based movie recommendation system** that suggests movies similar to a selected movie using only the **movie overview (description)**.

The system computes similarity between movies based on textual content and provides recommendations through a **Streamlit web interface**.

---

## 📌 Project Description

- Uses the **TMDB 5000 Movies dataset**
- Recommendations are generated **only from the `overview` feature**
- Text data is converted into numerical form using **Bag of Words**
- **Cosine similarity** is used to measure similarity between movies
- A simple and clean **Streamlit UI** allows users to select a movie and view recommendations
- This project marks the **first Streamlit UI built** as part of learning end-to-end ML applications

---


## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Framework:** Streamlit  

---



## ▶️ How to Run This Project on Your Local Computer

Clone the repository, create a virtual environment, install dependencies, and run the Streamlit application using the commands below.

# Clone the repository
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install required dependencies

# Run the Streamlit application
streamlit run app.py


