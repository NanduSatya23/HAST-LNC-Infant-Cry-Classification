from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define classifier
classifier = MLPClassifier(
    hidden_layer_sizes=(256, 128),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)
