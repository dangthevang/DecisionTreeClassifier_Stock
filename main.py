from Process.Caculater import EMA,MACD,RSI,SMA
from TranformData import transform as t
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def dudoan(symbol):
  # try:
    Com = t.Company(symbol)
    Com.SetupDataSet()
    data = Com.Data_Real
    MACD(data)
    RSI(data)
    data["SMA"] = SMA(data)
    data["EMA"] = EMA(data)
    data = data[29:]
    keep_column = ["close","MACD","RSI","SMA","EMA","signal_Line"]
    X = data[keep_column].values
    Y = data["result"].values
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=2)
    print(X_test,Y_test)
    tree = DecisionTreeClassifier().fit(X_train,Y_train)
    return tree.score(X_test,Y_test)
  # except:
  #   pass
data_symbol = pd.read_csv("TranformData\InforCom.csv")

for i in data_symbol[data_symbol["Exchange"]=="hose"]['Company']:
  print(i,end=" ")
  print(dudoan(i))
  
  # print(tree.predict(X_test))
  # print(Y_test)