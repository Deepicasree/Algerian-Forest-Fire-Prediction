# 🔥 Algerian Forest Fire Prediction using Machine Learning

## 📌 Project Overview

This project predicts the **Fire Weather Index (FWI)** using a **Ridge Regression** machine learning model. The application is built with **Flask** and provides a simple web interface where users can enter weather-related parameters and receive a predicted FWI value.

---

## 🚀 Features

* Predicts the **Fire Weather Index (FWI)**
* Flask-based web application
* User-friendly HTML interface
* Data preprocessing using **StandardScaler**
* Machine Learning model trained using **Ridge Regression**
* Model and scaler saved using Pickle

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* NumPy
* Pandas
* HTML
* CSS
* Pickle

---

## 📂 Project Structure

```
Algerian-Forest-Fire-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── ridge.pkl
├── scaler.pkl
├── templates/
│   └── home.html
├── 2.0-EDA And FE Algerian Forest Fires.ipynb
└── 3.0-Model Training.ipynb
```

---

## 📊 Input Features

The model uses the following features for prediction:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* ISI
* Classes
* Region

---

## 🎯 Output

* **Fire Weather Index (FWI)**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Deepicasree/Algerian-Forest-Fire-Prediction.git
```

Move into the project folder:

```bash
cd Algerian-Forest-Fire-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Preprocessing
5. Feature Scaling
6. Ridge Regression Model Training
7. Model Serialization using Pickle
8. Flask Deployment

---

## 📈 Future Improvements

* Deploy the application on Render
* Improve the user interface
* Add additional machine learning models for comparison
* Display prediction confidence and visualizations

---

## 👩‍💻 Author

**Deepicasree S**

* GitHub: https://github.com/Deepicasree

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
