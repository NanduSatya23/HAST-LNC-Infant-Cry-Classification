X_train, X_test, y_train, y_test = train_test_split(
    X_np,
    y_np,
    test_size=0.2,
    random_state=42,
    stratify=y_np
)

print("\n TRAIN–TEST SPLIT")
print("Training samples:", len(y_train))
print("Testing samples:", len(y_test))
