from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import file_read

features_train, labels_train = file_read.makeDataWithoutHumidity("training")
features_test, labels_test = file_read.makeDataWithoutHumidity("test")

#clf=KNeighborsClassifier(n_neighbors=7)
#clf=AdaBoostClassifier(n_estimators=5)
clf=RandomForestClassifier(n_estimators=100,min_samples_split=3)



clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print("accuracy of the prediction:",accuracy_score(pred,labels_test))

def getFittedClf(features_train, labels_train):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(features_train, labels_train)
