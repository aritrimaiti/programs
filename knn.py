from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
iris=datasets.load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.4)
print("Dataset is split into training and testing...")
print("Size of the training data and its label",x_train.shape,y_train.shape)
print("Size of the training data and its label",x_test.shape,y_test.shape)
for i in range(len(iris.target_names)):
    print("Label",i,"-",str(iris.target_names[1]))
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("Results of Classification using K-NN with K=3")
for r in range(0,len(x_test)):
    print("Sample:",str(x_test[r]),"Actual-label:",str(y_test[r]),"Predicted-label:",str(y_pred[r]))
print("Classification Accurancy:",classifier.score(x_test,y_test)*100);