# Audio Preprocessing Instructions

The infant cry audio recordings undergo several preprocessing steps before feature extraction and model training.

## 1. Resampling

All audio files are resampled to a uniform sampling rate of **16 kHz** to maintain consistency across recordings.

## 2. Silence Removal

Non-informative silent segments are removed to focus on the actual cry signal.

## 3. Noise Handling

Basic noise filtering is applied to reduce background disturbances present in real-world recordings.

## 4. Spectrogram Generation

The cleaned audio signals are converted into **Mel-Spectrogram representations**, which capture both frequency and temporal characteristics of the cry signals.

## 5. Transformer Embedding Extraction

The spectrogram inputs are processed using a **pretrained Audio Spectrogram Transformer (AST)** to extract deep audio embeddings.

These embeddings are then used as input features for the **Logistic Regression and MLP classifiers** used in the proposed system.
