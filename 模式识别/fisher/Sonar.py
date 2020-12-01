from sklearn import datasets, discriminant_analysis
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import matplotlib.pyplot as plt


random_seed = np.random.randint(0, 9)
print(random_seed)


def load_data():
    sonar = pd.read_csv('Sonar.csv')
    sonar = sonar.values
    sonar_data = sonar[:, 1:]
    sonar_label = sonar[:, -0]
    return train_test_split(sonar_data, sonar_label, test_size=0.2, random_state=random_seed)


if __name__ == '__main__':
    train_data, test_data, train_label, test_label = load_data()
    clf = LinearDiscriminantAnalysis()
    acc = []
    for i in range(60):
        clf = clf.fit(train_data[:, i:], train_label)
        pre = np.array(clf.predict(test_data[:, i:]))
        count = 0
        for j in range(len(pre)):
            if pre[j] == test_label[j]:
                count += 1
            else:
                continue
        acc.append(count / len(pre))
        acc.reverse()
x_axis = np.arange(0, 60)
y_axis = acc
plt.figure()
plt.xlabel('dimension')
plt.ylabel('accuracy')
plt.plot(x_axis, y_axis)
plt.show()
