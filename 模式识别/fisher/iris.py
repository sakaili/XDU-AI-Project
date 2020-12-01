from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
random_seed = np.random.randint(0, 9)


# print(data_file['frames'])


def load_data():
    data_file = load_iris()
    iris_data = data_file['data']
    iris_label = data_file['target']
    return train_test_split(iris_data, iris_label, test_size=0.2, random_state=random_seed)


if __name__ == '__main__':
    train_data, test_data, train_label, test_label = load_data()
    clf = LinearDiscriminantAnalysis()
    acc = []
    for i in range(0,4):
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
x_axis = np.arange(0, 4)
y_axis = acc
plt.figure()
plt.xlabel('dimension')
plt.ylabel('accuracy')
plt.plot(x_axis, y_axis)
plt.show()

