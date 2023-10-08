import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

data = pd.read_csv("your dataset here")
y = data.iloc[:, 16:17].values
X = data.iloc[:, 24:28].values
y1 = np.where(y >= 1, 1, 0)

X_train, X_test, y_train, y_test = train_test_split(X, y1, test_size = 0.25, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = SVC(kernel = 'linear', C = 10, random_state = 0)
classifier.fit(X_train, y_train.ravel())
y_pred = classifier.predict(X_test)

y_test = pd.DataFrame(y_test)
y_pred = pd.DataFrame(y_pred)
result = pd.concat([y_test, y_pred], axis = 1, sort = False)

cm = confusion_matrix(y_test, y_pred)
score = classifier.score(X_test, y_test)

accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train.ravel(), cv = 10)
Mean = accuracies.mean()
Variance = accuracies.std()
