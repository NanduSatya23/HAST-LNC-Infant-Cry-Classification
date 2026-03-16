from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt

def plot_roc_curve(y_true, y_scores):

    fpr, tpr, _ = roc_curve(y_true, y_scores)

    roc_auc = auc(fpr, tpr)

    plt.figure()

    plt.plot(fpr, tpr, label="ROC curve (AUC = %0.2f)" % roc_auc)

    plt.plot([0,1], [0,1], linestyle="--")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve for Infant Cry Classification")

    plt.legend(loc="lower right")

    plt.show()
