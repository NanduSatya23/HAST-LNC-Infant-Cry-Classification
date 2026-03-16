from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def normalize_embeddings(embeddings):
    return scaler.fit_transform(embeddings)
