from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt


def build_model(X_train,y_train):
    model = LogisticRegression()
    model.fit(X_train,y_train)

    return model

def evaluate_model(model, y_test, X_test, X):
    predict_test = model.predict(X_test)
    print("El modelo ha evaluado correctamente un " + str(round(metrics.accuracy_score(y_test,predict_test),2)*100) +"% de los datos")

    weigths = pd.Series(model.coef_[0],  
                   index = X.columns.values)

    print(weigths.sort_values(ascending=False)[:10].plot(kind='bar'))

    weigths = pd.Series(model.coef_[0],  
                   index = X.columns.values)

    print(weigths.sort_values(ascending=False)[-10:].plot(kind='bar'))

    fig = plt.figure(figsize=(11,11))
    cm = confusion_matrix(y_test,predict_test, labels = model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=model.classes_)
    disp.plot(cmap='mako')
    plt.grid(False)
    plt.show()