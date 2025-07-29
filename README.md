# 📡 Modulation Classification App

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Colab](https://img.shields.io/badge/Open%20in-Google%20Colab-orange?logo=googlecolab)](https://colab.research.google.com/)
[![Stars](https://img.shields.io/github/stars/mayurjalan/modulation-classifier?style=social)](https://github.com/mayurjalan/modulation-classifier/stargazers)
[![Forks](https://img.shields.io/github/forks/mayurjalan/modulation-classifier?style=social)](https://github.com/mayurjalan/modulation-classifier/network/members)
[![Issues](https://img.shields.io/github/issues/mayurjalan/modulation-classifier?color=blue)](https://github.com/mayurjalan/modulation-classifier/issues)
[![Last Commit](https://img.shields.io/github/last-commit/mayurjalan/modulation-classifier)](https://github.com/mayurjalan/modulation-classifier/commits/main)


---

## 🚀 Project Overview

**Modulation Classification** is a machine learning app that predicts the type of modulation (e.g., BPSK, QPSK, QAM, etc.) used in a given noisy complex baseband signal.

It includes:
- 📊 **Feature extraction** using signal statistics (mean, std, skew, kurtosis)
- 🤖 **Training on models** like Random Forest and SVM
- 🎯 **Evaluation** with confusion matrix and ROC curves
- 🌐 **Streamlit app** for real-time signal classification using `.npy` files
- ☁️ **Google Colab support** for training and exporting models

---

## 📁 Folder Structure

```bash
modulation_classifier/
│
├── streamlit_app/
│   ├── app.py                  # Streamlit frontend
│   ├── best_rf_model.pkl       # Trained Random Forest model
│   └── requirements.txt        # Python dependencies
│
├── colab/
│   └── train_model.ipynb       # Model training and export notebook
│
├── .gitignore
├── README.md
```

---


## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/modulation_classifier.git
cd modulation_classifier/streamlit_app
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## 🧪 Test It

To test your app, upload a sample `.npy` file containing a **complex-valued baseband signal**:
```python
# Generate a test signal (example)
np.save("test_signal.npy", bpsk_gen(np.random.randint(0, 2, 1000)))
```

---

## 🧠 Modulation Classes Supported

- BPSK
- QPSK
- 8PSK
- 16QAM
- 64QAM
- 4ASK
- FSK

---

## 🤝 Contribution

Feel free to fork, contribute, or raise issues!
