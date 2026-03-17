# Methodology

The proposed system, **HAST-LNC (Hybrid Audio Spectrogram Transformer with Lightweight Neural Classifier)**, is designed to classify infant cries into categories such as *hungry*, *discomfort*, and *tired*. The methodology integrates advanced audio representation learning with efficient classification techniques.

---

## 1. Data Collection and Preprocessing

The dataset consists of infant cry audio samples collected from publicly available sources. The preprocessing pipeline includes:

* **Resampling** audio signals to a consistent sampling rate
* **Silence removal** to eliminate non-informative segments
* **Normalization** to standardize amplitude levels
* **Noise handling** to improve signal quality

These steps ensure uniformity and improve feature extraction quality.

---

## 2. Spectrogram Generation

The preprocessed audio signals are converted into **spectrogram representations**, which capture both temporal and frequency domain information. These spectrograms serve as input to the feature extraction module.

---

## 3. Transformer-Based Feature Extraction

A pretrained **Audio Spectrogram Transformer (AST)** is used to extract deep audio embeddings. This approach eliminates the need for handcrafted feature engineering.

* Captures **temporal patterns**
* Learns **spectral characteristics**
* Provides **context-aware representations**

---

## 4. Feature Scaling

The extracted features are standardized using techniques such as **StandardScaler**, ensuring consistent input distribution for machine learning models.

---

## 5. Classification

Two classifiers are used:

### Logistic Regression

* Serves as a baseline model
* Efficient and interpretable

### Multi-Layer Perceptron (MLP)

* Captures non-linear relationships
* Uses ReLU activation for hidden layers
* Uses Softmax for multi-class prediction

---

## 6. Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Matthews Correlation Coefficient (MCC)

A confusion matrix is used for class-wise performance analysis.

---

## Summary

The HAST-LNC framework combines **transformer-based feature extraction** with **lightweight classifiers**, achieving efficient and accurate infant cry classification while maintaining low computational complexity.
