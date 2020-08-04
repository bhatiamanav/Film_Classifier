#Importing the Required Libraries
import random
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,roc_curve,auc,f1_score 

#Loading the Data for the project
data = pd.read_csv("IMDB-Movie-Data.csv")
data = data.dropna(axis=0, how='any')

#Separating the Data into the features and the labels
X = data[data.columns[6:32]]
Y = data.iloc[:,-1]

#Splitting into Train and Test Data and Scaling of the Data
X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.25,random_state=0)
scaler = StandardScaler()
X_Train = scaler.fit_transform(X_Train)
X_Test = scaler.transform(X_Test)

#Model Creation
clf = GaussianNB()

#Model Training and Prediction
y_pred = clf.fit(X_Train,Y_Train).predict(X_Test)

#Model Evaluation
conf_mat = confusion_matrix(Y_Test,y_pred)
accuracy = accuracy_score(Y_Test,y_pred)
precision = precision_score(Y_Test,y_pred)
recall = recall_score(Y_Test,y_pred)
F_measure = f1_score(Y_Test,y_pred)

#Plotting the results
false_positive_rate, true_positive_rate, thresholds = roc_curve(Y_Test, y_pred)
roc_area = auc(false_positive_rate,true_positive_rate)
plt.title('Receiver Operating Characterstic(ROC)')
plt.plot(false_positive_rate,true_positive_rate,'b',label='AUC = %0.2f'% roc_area)
plt.legend(loc='upper right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.3])
plt.ylim([-0.1,1.3])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()

#Printing the Results
print('Confusion Matrix :')
print(conf_mat)
print('\nAccuracy :')
print(accuracy)
print('\nPrecision is :')
print(precision)
print('\nRecall is: ')
print(recall)
print('\nF-measure is: ')
print(F_measure)
