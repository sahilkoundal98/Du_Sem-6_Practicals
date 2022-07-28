import pandas as pd
import numpy as np
ds=pd.read_csv('wdbc.data')
ds.shape
col=[i for i in range(32)]
ds.columns=col
ds
X=ds.values[:,[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]]
Y=ds.values[:,1]
print(X.shape)
print(Y.shape)
from sklearn.model_selection import train_test_split
# Trainig data is 75% Testing is 25%(Holdout)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
DTclassifer = DecisionTreeClassifier()
#Induction
DTclassifer.fit(X_train,Y_train)
#Prediction(deduction)
predictions=DTclassifer.predict(X_test)
predictions
accuracy_score(Y_test,predictions)
confusion_matrix(Y_test,predictions)
from sklearn.neighbors import KNeighborsClassifier
KNclassifer = KNeighborsClassifier(n_neighbors=3)
#Induction
KNclassifer.fit(X_train,Y_train)
#Prediction(deduction)
predictions=KNclassifer.predict(X_test)
predictions
accuracy_score(Y_test,predictions)
confusion_matrix(Y_test,predictions)
from sklearn.naive_bayes import GaussianNB 
BNclassifer = GaussianNB()
#Induction
BNclassifer.fit(X_train,Y_train)
#Prediction(deduction)
predictions=BNclassifer.predict(X_test)
predictions
accuracy_score(Y_test,predictions)
confusion_matrix(Y_test,predictions)
Val_size=0.33
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = Val_size)
deciTree = DecisionTreeClassifier()
deciTree.fit(X_train, Y_train)
predictions = deciTree.predict(X_test)
print("Accuracy on the Test Data(Decesion Tree) ")
print(accuracy_score(Y_test, predictions))
KNclassifer = KNeighborsClassifier(n_neighbors=3)
#Induction
KNclassifer.fit(X_train,Y_train)
#Prediction(deduction)
predictions=KNclassifer.predict(X_test)
print("Accuracy on the Test Data(K Nearest) ")
print(accuracy_score(Y_test, predictions))
BNclassifer.fit(X_train,Y_train)
#Prediction(deduction)
predictions=BNclassifer.predict(X_test)
print("Accuracy on the Test Data(Naive bayes) ")
print(accuracy_score(Y_test, predictions))
from sklearn.utils import resample #test size is how much rest is training 
itr=10
Val_size=0.25
random_seed=3 #randomly chosing
accDT=[]
accKM=[]
accBN=[]
for i in range(itr):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size =Val_size,random_state=random_seed)
    deciTree = DecisionTreeClassifier()
    deciTree.fit(X_train, Y_train)
    predictions = deciTree.predict(X_test)
    accDT.append(accuracy_score(Y_test, predictions))

    KNclassifer = KNeighborsClassifier(n_neighbors=3)

    #Induction

    KNclassifer.fit(X_train,Y_train)

    #Prediction(deduction)

    predictions=KNclassifer.predict(X_test)
    accKM.append(accuracy_score(Y_test, predictions))
    BNclassifer.fit(X_train,Y_train)
    #Prediction(deduction)
    predictions=BNclassifer.predict(X_test)
    accBN.append(accuracy_score(Y_test, predictions))
print("Accuracy on the Test Data(Decesion Tree) ")
print(sum(accDT)/len(accDT))
print("Accuracy on the Test Data(K Nearest) ")
print(sum(accKM)/len(accDT))
print("Accuracy on the Test Data(Naive bayes) ")
print(sum(accBN)/len(accDT))
from sklearn.utils import resample #test size is how much rest is training itr=10
Val_size=0.33
random_seed=3 #randomly chosing
accDT=[]
accKM=[]
accBN=[]
for i in range(itr):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size =Val_size,random_state=random_seed)
    deciTree = DecisionTreeClassifier()
    deciTree.fit(X_train, Y_train)
    predictions = deciTree.predict(X_test)
    accDT.append(accuracy_score(Y_test, predictions))
    KNclassifer = KNeighborsClassifier(n_neighbors=3)
    #Induction
    KNclassifer.fit(X_train,Y_train)
    predictions=KNclassifer.predict(X_test)
    accKM.append(accuracy_score(Y_test, predictions))
    BNclassifer.fit(X_train,Y_train)
    #Prediction(deduction)
    predictions=BNclassifer.predict(X_test)
    accBN.append(accuracy_score(Y_test, predictions))
print("Accuracy on the Test Data(Decesion Tree) ")
print(sum(accDT)/len(accDT))
print("Accuracy on the Test Data(K Nearest) ")
print(sum(accKM)/len(accDT))
print("Accuracy on the Test Data(Naive bayes) ")
print(sum(accBN)/len(accDT))
from sklearn.model_selection import cross_val_score
dt=cross_val_score(DTclassifer,X,Y).mean()
kn=cross_val_score(KNclassifer,X,Y).mean()
ba=cross_val_score(BNclassifer,X,Y).mean()
print("Accuracy on the Test Data(Decesion Tree): ",dt)
print("Accuracy on the Test Data(K Nearest): ",kn)
print("Accuracy on the Test Data(Naive Bayes): ",ba)
from sklearn.model_selection import KFold, cross_val_score
kf = KFold(n_splits=len(ds)-1)
dt=cross_val_score(DTclassifer,X,Y,cv=kf).mean()
kn=cross_val_score(KNclassifer,X,Y,cv=kf).mean()
ba=cross_val_score(BNclassifer,X,Y,cv=kf).mean()
print("Accuracy on the Test Data(Decesion Tree): ",dt)
print("Accuracy on the Test Data(K Nearest): ",kn)
print("Accuracy on the Test Data(Naive Bayes): ",ba)
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()
DTclassifer = DecisionTreeClassifier() #Induction DTclassifer.fit(X_train,Y_train) #Prediction(deduction) predictions=DTclassifer.predict(X_test)
print("Accuracy on the Test Data(Decesion Tree) ") 
print(accuracy_score(Y_test, predictions))