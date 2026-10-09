from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [8, 8], [9, 8.5], [1, 0.5], [9, 10]])

model = KMeans(n_clusters=2, n_init=12)
model.fit(X)

print(model.labels_)
print(model.cluster_centers_)
