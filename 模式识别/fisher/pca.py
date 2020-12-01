from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import pandas as pd
import matplotlib.pyplot as plt

sonar = pd.read_csv('Sonar.csv')
sonar = sonar.values
sonar_data = sonar[:, 1:]
sonar_label = sonar[:, -0]
sonar_data = sonar_data.reshape((60, 207))

pca = PCA(n_components=10)
pca.fit(sonar_data)
plt.figure()
plt.plot(pca.explained_variance_, 'k', linewidth=2)
plt.show()
# print(pca.explained_variance_) # 输出特征根
# print(pca.explained_variance_ratio_) # 输出解释方差比
ans = pca.components_
