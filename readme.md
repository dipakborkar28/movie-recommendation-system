# 🎬 Movie Recommendation System

A content-based movie recommendation web application built with Python, Streamlit, and machine learning. Select a movie and discover five similar movies from the available movie collection.

## 🚀 Live Demo

**Try the application:** [Movie Recommendation System](https://movie-recommendation-system-ysg6yzlnqwplbs5eucxhow.streamlit.app/)

## 📌 Project Overview

Finding movies similar to the ones we enjoy can be difficult when there are many choices. This project provides a simple interactive application that recommends similar movies based on a selected title.

The project uses vectorized movie data and a nearest-neighbors model to identify similar movies.

## ✨ Features

- 🎥 Select a movie from a dropdown list.
- 🤖 Find five similar movie recommendations.
- ⚡ Use a precomputed model for recommendations.
- 🌐 Access the application through a web browser.
- 🖥️ Interactive interface built with Streamlit.

## 🛠️ Technologies Used

- **Python** — core programming language
- **Pandas** — movie data handling
- **NumPy** — numerical operations
- **Scikit-learn** — machine learning and nearest-neighbors functionality
- **Joblib** — loading the saved recommendation model
- **Streamlit** — interactive web application

## 🧠 How It Works

1. Movie information is loaded and prepared in a Jupyter notebook.
2. Movie data is transformed into numerical vectors using a vectorization method.
3. A nearest-neighbors model identifies movies similar to the selected movie.
4. The Streamlit application loads the saved recommendation data.
5. When a user selects a movie and clicks **Recommend Movies**, the application displays five similar titles.

## 📂 Project Structure

```text
movie-recommendation-system/
├── app.py
├── main.ipynb
├── model.pkl
├── movie_recommender.pkl
├── requirements.txt
├── tmdb_5000_credits.csv
├── tmdb_5000_movies.csv
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/dipakborkar28/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

**Note:** The application expects the saved `movie_recommender.pkl` file to be present in the project root. The repository also contains `model.pkl`; verify whether it is needed by your current application before removing it.

## 📊 Dataset

The repository includes two CSV files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These files are used for movie information and credits in the project. Check the dataset's original source and applicable usage terms before redistributing the data.

## 🎯 Learning Outcomes

Through this project, I practised:

- Working with movie datasets using Pandas.
- Preparing data for machine learning.
- Applying vectorization and nearest-neighbors techniques.
- Saving and loading model artifacts.
- Building an interactive application with Streamlit.
- Deploying a Python application online.

## 🔮 Future Improvements

- Display movie posters and descriptions.
- Include genres and additional movie information.
- Improve the interface and recommendation explanations.
- Add tests and evaluate recommendation quality.
- Improve error handling and application performance.

## 👨‍💻 Author

**Dipak Borkar**

GitHub: [@dipakborkar28](https://github.com/dipakborkar28)

---

If you find the project useful, feel free to explore the repository and share feedback.
