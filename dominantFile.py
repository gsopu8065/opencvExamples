import cv2
from sklearn.cluster import KMeans

# Read image
image = cv2.imread("images/dog.jpg")
print("Image shape = ", image.shape)

# Reshape matrix to a big array
image = image.reshape((image.shape[0] * image.shape[1], 3))
print("Big array shape = ", image.shape)

# Cluster points and label each pixel
clt = KMeans(n_clusters=3)
clt.fit(image)
print("Total pixels = ",len(clt.labels_))

# Count labels
countLabels = {}
for a in clt.labels_:
    if a in countLabels.keys():
        countLabels[a] += 1
    else:
        countLabels[a] = 1

# display cluster count
for key, value in countLabels.items():
    print("Cluster {0} has {1} pixels ".format(key, value))


# cluster center values
print("Cluster 0 color : ", clt.cluster_centers_[0].astype("uint8"))
print("Cluster 1 color : ", clt.cluster_centers_[1].astype("uint8"))
print("Cluster 2 color : ", clt.cluster_centers_[2].astype("uint8"))