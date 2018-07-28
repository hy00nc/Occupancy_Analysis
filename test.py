from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from re import sub


#clf=KNeighborsClassifier(n_neighbors=3)
#clf=AdaBoostClassifier(n_estimators=50)
clf=RandomForestClassifier(n_estimators=100,min_samples_split=5)

'''
feature_test

labels_test


clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print "acc:",accuracy_score(pred,labels_test)
'''
