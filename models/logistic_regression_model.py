from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    solver='lbfgs',
    multi_class='multinomial'
)
return model
