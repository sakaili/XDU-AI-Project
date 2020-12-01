from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data_file = pd.read_csv('Sonar.csv')
dataset = data_file.values
label = dataset[:,-0]
dataset = dataset[:,1:]

k_range = range(1, 60)
k_error = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    #cv参数决定数据集划分比例，这里是按照5:1划分训练集和测试集
    scores = cross_val_score(knn, dataset, label, cv=20, scoring='accuracy')
    k_error.append(1 - scores.mean())
plt.plot(k_range, k_error)
plt.xlabel('Value of K for KNN')
plt.ylabel('Error')
plt.show()
