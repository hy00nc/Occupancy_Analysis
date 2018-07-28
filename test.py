from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import file_read

features_train, labels_train = file_read.makeData("training")
features_test, labels_test = file_read.makeData("test")

#clf=KNeighborsClassifier(n_neighbors=3)
#clf=AdaBoostClassifier(n_estimators=50)
clf=RandomForestClassifier(n_estimators=100,min_samples_split=5)

clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print("acc:",accuracy_score(pred,labels_test))
