from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn import clone

import file_read

tmp_features_train, labels_train = file_read.makeData("training")
features_test, labels_test = file_read.makeData("test")


clf=KNeighborsClassifier(n_neighbors=3)
#clf=AdaBoostClassifier(n_estimators=50)
#clf=RandomForestClassifier(n_estimators=100,min_samples_split=5)





n_classes = 3
n_estimators = 30
emap = plt.cm.RdYlBu
plot_step = 0.02
plot_step_coarser = 0.5
RANDOM_SEED = 13

features_train = list()
for line in tmp_features_train:
    features_train.append(line[2:4])

23.18,27.272,426,721.25,

clf.fit(features_train,labels_train)
scores = clf.score(features_train,labels_train)

plt.scatter(np.array(features_train)[:, 0], np.array(features_train)[:, 1], c=np.array(labels_train),
                    cmap=ListedColormap(['r', 'y', 'b']),
                    edgecolor='k', s=20)

plt.suptitle("Classifiers on features subsets")
plt.show()
