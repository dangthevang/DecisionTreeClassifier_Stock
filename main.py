from Process.Caculater import EMA,MACD,RSI,SMA
from TranformData import transform as t
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
def dudoan(symbol, vitri):
  try:
    Com = t.Company(symbol)
    Com.SetupDataSet()
    data = Com.Data_Real
    MACD(data)
    RSI(data)
    data["SMA"] = SMA(data)
    data["EMA"] = EMA(data)
    data = data[29:]
    keep_column = ["close","open","low","MACD","RSI","SMA","EMA","signal_Line"]
    X = data[keep_column].values
    Y = data["result"].values
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
    tree = DecisionTreeClassifier().fit(X_train,Y_train)
    arr = tree.predict(X_test)
    return arr[vitri] == Y_test[vitri]
  except:
    pass
data_symbol = pd.read_csv("TranformData\InforCom.csv")

ngay = 0
while ngay <10:
  dudoandung = 0
  soluong = 0
  for i in data_symbol[data_symbol["Exchange"]=="hose"]['Company']:
    tree = dudoan(i,ngay)
    if tree == None:
      continue
    if tree == True:
      dudoandung +=1
    soluong+=1
  print(ngay,dudoandung/soluong,soluong)
  ngay +=1
  # break
  
  # print(tree.predict(X_test))
  # print(Y_test)