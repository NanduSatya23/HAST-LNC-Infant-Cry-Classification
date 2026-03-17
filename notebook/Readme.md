This directory contains Jupyter notebooks demonstrating the implementation and visualization of the **HAST-LNC (Hybrid Audio Spectrogram Transformer with Lightweight Neural Classifier)** framework for infant cry classification.

---

## 📁 Structure

```
notebooks/
│
├── experiment_demo.ipynb
└── visualization.ipynb
```

---

## 📓 experiment_demo.ipynb

This notebook provides a complete **end-to-end pipeline** of the proposed system.

### ✔ Includes:

* Dataset loading (placeholder or actual data)
* Audio preprocessing / feature preparation
* Feature scaling
* Model training:

  * Logistic Regression
  * MLP Classifier
* Model evaluation:

  * Accuracy
  * Classification report
  * Confusion matrix

### 🎯 Purpose:

* Demonstrates the full workflow in one place
* Enables reproducibility of results
* Useful for reviewers and beginners

---

## 📓 visualization.ipynb

This notebook focuses on **performance visualization and analysis**.

### ✔ Includes:

* Accuracy comparison plot
* ROC curve
* Training loss visualization (optional)

### 🎯 Purpose:

* Helps interpret model performance
* Provides figures for research paper and presentations

---

## 🚀 How to Use

1. Open notebooks using:

   * Jupyter Notebook / JupyterLab
   * or Google Colab

2. Run cells sequentially (top → bottom)

3. Install required dependencies:

```
pip install -r requirements.txt
```

---

## 🌐 Google Colab Support (Optional)

You can upload these notebooks to Google Colab and run them without local setup.

---

## 📌 Notes

* The current notebooks may use sample data placeholders. Replace them with actual infant cry datasets for real experiments.
* Ensure consistent preprocessing and scaling before model training.

---

## 📊 Summary

These notebooks provide both **implementation and visualization support** for the HAST-LNC framework, making it easier to understand, reproduce, and evaluate the proposed infant cry classification system.

---
