# Results Overview

This directory contains the experimental outputs of the **HAST-LNC (Hybrid Audio Spectrogram Transformer with Lightweight Neural Classifier)** framework for infant cry classification.

---

## 📁 Folder Structure
results/
│
├── confusion_matrix.png
├── accuracy_results
│
├── performance_plots/
│   ├── accuracy_plot.png
│   ├── roc_curve.png
│   ├── loss_plot.png


## 📊 File Descriptions

### 🔹 confusion_matrix.png

This image represents the confusion matrix of the proposed model (MLP classifier).
It illustrates the number of correct and incorrect predictions for each infant cry category (e.g., hungry, tired, discomfort).

* X-axis → Predicted labels
* Y-axis → Actual labels
* Values → Number of samples

This helps in understanding class-wise performance and misclassification patterns.

### 🔹 accuracy_results

This file contains quantitative evaluation metrics for the models used in the project.

**Metrics included:**

* Accuracy
* Precision
* Recall
* F1 Score
* Matthews Correlation Coefficient (MCC)

It enables direct comparison between Logistic Regression and MLP classifier.

---

## 📈 performance_plots/

This folder contains graphical representations of model performance.

---

### 🔸 accuracy_plot.png

A comparison plot showing accuracy differences between:

* Logistic Regression
* MLP Classifier

It highlights the improved performance of the MLP model.

---

### 🔸 roc_curve.png

The ROC (Receiver Operating Characteristic) curve illustrates the trade-off between:

* True Positive Rate (Sensitivity)
* False Positive Rate

It evaluates the model’s ability to distinguish between different infant cry classes.

---

### 🔸 loss_plot.png (optional)

This plot shows training loss across epochs for the MLP classifier.

* Helps in analyzing model convergence
* Indicates stability of training process

---

## 📌 Summary

The experimental results demonstrate that the **MLP classifier** outperforms Logistic Regression by effectively capturing non-linear patterns in transformer-based audio embeddings.

However, the confusion matrix and class-wise metrics reveal that performance varies across classes due to dataset imbalance, particularly affecting minority classes such as *discomfort* and *tired*.

Overall, the results validate the effectiveness of combining **transformer-based feature extraction with lightweight neural classification**, achieving a balance between accuracy, efficiency, and practical deployability.

---
