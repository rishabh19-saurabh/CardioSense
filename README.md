# ❤️ CardioSense: Early Heart Disease Detection using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![KNN](https://img.shields.io/badge/Model-KNN-success)
![License](https://img.shields.io/badge/License-MIT-green)

A full-stack Machine Learning web application for early heart disease risk prediction. The platform combines healthcare analytics, machine learning, data visualization, and patient record management to provide an intelligent decision-support system for cardiovascular disease screening.

---

# 📌 Project Highlights

✔ Heart Disease Prediction using Machine Learning

✔ Interactive Flask Web Application

✔ MongoDB Database Integration

✔ Exploratory Data Analysis (EDA)

✔ Patient Data Management (CRUD Operations)

✔ Real-Time Prediction Dashboard

✔ Feature Visualization & Comparison Charts

✔ Model Persistence using Joblib

✔ Production-Ready Project Structure

✔ Research-Oriented Healthcare Analytics

---

# 🏥 Problem Statement

Cardiovascular diseases remain one of the leading causes of death worldwide. Early diagnosis can significantly improve treatment outcomes and reduce mortality rates.

This project leverages machine learning techniques to analyze clinical attributes and predict the likelihood of heart disease at an early stage. The system assists healthcare professionals and researchers by providing fast and data-driven risk assessments.

---

# 🎯 Objectives

- Predict heart disease risk using clinical parameters
- Provide an intuitive web interface for diagnosis
- Store patient records securely in MongoDB
- Visualize health indicators for better interpretation
- Support healthcare research through data analytics

---

# 📂 Repository Structure

```text
CardioSense/
│
├── app.py
├── database.py
├── prediction.py
├── modelbuild.py
├── visualization.py
├── requirements.txt
│
├── templates/
│   ├── disease.html
│
├── notebooks/
│   ├── Early Detection of Heart Disease Using Big Data Approach.ipynb
│   ├── Heart Disease Detection Using Big Data Approach.ipynb
│   └── Heart_Disease_Prediction.ipynb
│
├── reports/
│   ├── EDA_heart_Disease.html
│   └── EDA_heart_Disease.pdf
│
├── models/
│   └── heartmodel.pkl
│
└── README.md
```

---

# 📊 Dataset Information

### Dataset Summary

| Attribute | Value |
|------------|--------|
| Records | 303 |
| Features | 13 |
| Missing Values | 0 |
| Duplicate Records | 1 |
| Target Variable | Heart Disease Presence |

### Clinical Features

| Feature | Description |
|----------|-------------|
| age | Patient Age |
| sex | Gender |
| cp | Chest Pain Type |
| trestbps | Resting Blood Pressure |
| chol | Cholesterol |
| fbs | Fasting Blood Sugar |
| restecg | Resting ECG Results |
| thalach | Maximum Heart Rate |
| exang | Exercise-Induced Angina |
| oldpeak | ST Depression |
| slope | ST Segment Slope |
| ca | Major Vessels Count |
| thal | Thalassemia Status |

---

# 🔍 Exploratory Data Analysis

The project includes detailed EDA reports generated using Pandas Profiling.

### Dataset Statistics

- Total Records: 303
- Total Features: 14
- Missing Values: 0%
- Duplicate Records: 0.3%
- Average Age: 54.36 years
- Average Cholesterol: 246.26 mg/dL

The EDA report explores:

- Feature distributions
- Correlation analysis
- Outlier detection
- Missing value analysis
- Target distribution
- Clinical feature relationships

---

# 🤖 Machine Learning Pipeline

## Data Preprocessing

- Feature Encoding
- Duplicate Removal
- Normalization using MinMaxScaler
- Train-Test Split (80/20)

## Model Training

The system uses:

### K-Nearest Neighbors (KNN)

```python
KNeighborsClassifier(n_neighbors=7)
```

Workflow:

1. Data Collection
2. Data Cleaning
3. Feature Scaling
4. Model Training
5. Evaluation
6. Model Persistence
7. Deployment

---

# ⚙️ Technology Stack

## Backend

- Flask
- Python

## Machine Learning

- Scikit-Learn
- NumPy
- Pandas
- Joblib

## Database

- MongoDB

## Visualization

- Matplotlib
- Seaborn

## Deployment

- Gunicorn

---

# 📈 Application Features

### Prediction Module

- Heart disease risk prediction
- Clinical feature processing
- Real-time inference

### Database Module

- Store patient records
- Update records
- Delete records
- Retrieve patient history

### Analytics Module

- Health comparison charts
- Patient vs normal benchmark analysis
- Data visualization dashboard

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/CardioSense.git

cd CardioSense
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_LINK=your_mongodb_connection_string
```

## Run Application

```bash
python app.py
```

Application will start at:

```text
http://localhost:5000
```

---

# 📷 Screenshots

Add screenshots here:

- Home Page
- Prediction Form
- Prediction Results
- Analytics Dashboard
- EDA Visualizations

---

# 📚 Research Foundation

This project was developed as part of a Big Data Analytics academic project focusing on early cardiovascular disease detection through machine learning and healthcare analytics.

The implementation combines:

- Machine Learning
- Healthcare Data Mining
- Predictive Analytics
- Clinical Decision Support Systems

---

# 🔮 Future Improvements

- Deep Learning Models
- XGBoost Integration
- SHAP Explainability
- Patient Authentication
- Cloud Deployment
- REST API Support
- Real-Time IoT Health Monitoring
- Docker Support

---

# 👨‍💻 Author

**Rishabh Saurabh**

B.Tech CSE (AI & ML)

Sharda University

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider starring the repository.