from django.shortcuts import render;
#Importing Required Libraries.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request, "home.html")



def predict(request):
    return render(request, "predict.html")


def result(request):
    # Loading the Dataset.
    data = pd.read_csv(r"C:\Users\roho_ract\Desktop\House_Price_Prediction_System\USA_Housing.csv")

    # Dropaddresscolumn
    data = data.drop(["Address"], axis=1)

    # train test split
    X = data.drop("Price", axis=1)
    Y = data["Price"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.30)

    # training and prediction
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))

    pred = round(pred[0])

    price = "The Predicted Price is $"+str(pred)



    return render(request, "predict.html",{"result2":price})