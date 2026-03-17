# System Architecture

The HAST-LNC system follows a modular pipeline designed for efficient infant cry classification.

---

## Overview

The architecture consists of the following stages:

```
Audio Input → Preprocessing → Spectrogram → AST Embeddings → Feature Scaling → Classifier → Output Prediction
```

---

## 1. Input Layer

* Raw infant cry audio signals
* Collected from datasets

---

## 2. Preprocessing Module

* Resampling
* Noise reduction
* Silence removal
* Normalization

This stage ensures clean and standardized input.

---

## 3. Feature Representation

### Spectrogram Conversion

Transforms audio signals into visual time-frequency representations.

### AST Embedding Layer

* Uses pretrained transformer model
* Extracts deep features automatically
* Captures both local and global dependencies

---

## 4. Feature Scaling

* Standardization using statistical normalization
* Improves model convergence

---

## 5. Classification Layer

Two classifiers are used:

* **Logistic Regression** (baseline)
* **MLP Classifier** (proposed lightweight neural model)

The MLP consists of:

* Input layer
* Hidden layers with ReLU activation
* Output layer with Softmax activation

---

## 6. Output Layer

* Produces probability scores for each class
* Final prediction is the class with highest probability

---

## Key Advantages

* Reduced dependency on handcrafted features
* Efficient computation with lightweight models
* Scalable and suitable for real-time applications

---

## Summary

The system architecture efficiently integrates **transformer-based feature extraction** with **simple yet powerful classifiers**, enabling accurate and interpretable infant cry classification.
