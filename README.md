# Crop-Prediction
---
title: "Crop Prediction System"
author: "Aman Kumar"
description: "A machine learning-based system that predicts the best crop based on environmental and soil conditions."
tags: [machine learning, agriculture, crop recommendation, random forest]
date: 2025-07-11
license: MIT
---

# 🌱 Crop Prediction System

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

A machine learning-based crop recommendation tool that suggests the most suitable crop based on soil and weather parameters. This helps farmers make data-driven agricultural decisions.

---

## 🚀 Demo

![Sample Output](https://github.com/Amankar003/Crop-Prediction/blob/main/screenshots/sample_output.png)

*Note: Replace this screenshot with your actual result output if needed.*

---

## 🧠 Features

- Predicts optimal crop based on user input
- High accuracy (~99%) using Random Forest Classifier
- Clean and simple notebook-based implementation
- Easy to extend into a full web or mobile application

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn, matplotlib  
- **Model:** Random Forest Classifier  
- **Environment:** Jupyter Notebook  

---

## 📂 Project Structure


---

## 📊 Input Parameters

| Parameter    | Description                  |
|--------------|------------------------------|
| N            | Nitrogen content (ppm)       |
| P            | Phosphorus content (ppm)     |
| K            | Potassium content (ppm)      |
| Temperature  | Ambient temperature (°C)     |
| Humidity     | Relative humidity (%)        |
| pH           | Soil pH value                |
| Rainfall     | Average rainfall (mm)        |

---

## 📈 Model Details

- **Algorithm:** Random Forest Classifier  
- **Train-Test Split:** 80:20  
- **Accuracy:** ~99%  
- **Evaluation:** Classification Report and Confusion Matrix used

---

## ▶️ How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/Amankar003/Crop-Prediction.git
   cd Crop-Prediction


## Install Dependencies
- pip install -r requirements.txt

## Run the Jupyter Notebook
- jupyter notebook Crop_Recommendation.ipynb

## Future Enhancement
- Deploy as web application using Streamlit or Flask
- Integrate real-time weather and geolocation APIs
- Improve dataset with more region-specific crop data
- Export trained model for production use

## 🙌 Credits
- Dataset from Kaggle
- ML Model built using Scikit-learn
- Inspired by Gitdocify-style documentation

## 🧑‍💻 Author
Aman Kumar
- GitHub: @Amankar003
