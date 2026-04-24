# 🌊 Smart AI Irrigation System (95.8% Accuracy)

This project is an AI-powered irrigation controller developed on a **Raspberry Pi** using machine learning to optimize water usage in agriculture.

## 🚀 Recent Update: Breaking 95.8% Accuracy!
Originally started with a Random Forest model (95.3%), I have now optimized the system using **XGBoost**, reaching a high-precision score of **0.95878** on the Kaggle irrigation dataset.

## ✨ Key Features
* **AI-Driven Logic:** Uses advanced Gradient Boosting (XGBoost) to determine soil irrigation needs with extreme precision.
* **Hardware Integration:** Developed on **Raspberry Pi** with **Robot Hat** library for real-time hardware control.
* **Data-Informed:** Trained on a large dataset (270,000+ samples) featuring soil moisture, temperature, and rainfall data.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Machine Learning:** XGBoost, Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Hardware:** Raspberry Pi, Robot Hat Library



## 📊 Performance Comparison
| Model | Accuracy |
| :--- | :--- |
| Random Forest | 93.09% |
| Optimized Random Forest | 95.35% |
| **XGBoost (Final)** | **95.87% 🏆** |

## 📁 Repository Structure
* `train_xgb.py`: Script to train the XGBoost model.
* `smart_irrigation.py`: Main logic for hardware control and prediction.
* `label_encoder.pkl`: Saved labels for Low, Medium, and High irrigation needs.

---
*Developed by Mulugeta Gebere*

