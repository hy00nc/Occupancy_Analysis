from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from re import sub


#clf=KNeighborsClassifier(n_neighbors=3)
#clf=AdaBoostClassifier(n_estimators=50)
clf=RandomForestClassifier(n_estimators=100,min_samples_split=5)

file = open("datatraining.txt",mode='r',encoding='utf-8')

lines = file.readlines()

features_train = list()
labels_train = list()

for line in lines:
    splitted_line = line.split(',')
    features_train.append(splitted_line[0:-1])
    changed_splitted_label = sub('\n', '', splitted_line[-1])
    try:
        labels_train.append(int(changed_splitted_label))
    except:
        pass


#print(features_train)
print(labels_train)




'''
feature_test

labels_test


clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print "acc:",accuracy_score(pred,labels_test)
'''
