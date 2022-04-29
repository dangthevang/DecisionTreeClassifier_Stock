import pandas as pd
import numpy as np
from TranformData.uils import caculater_real,formatDate,getChangeClose
class Company():
  def __init__(self,symbol):
    self.symbol = symbol
    self.Data_Close = pd.read_csv("Data/Close/{}.csv".format(symbol))
    self.Data_Dividend =  pd.read_csv("Data/Diviend/{}.csv".format(symbol))
    self.Data_Real = None
  
  def Transform(self):
    self.Data_Close = self.Data_Close[["date","open","high","low","close"]]
    self.Data_Dividend = self.Data_Dividend.rename(columns={"time":"date"})
    self.Data_Real = self.Data_Close
    self.Data_Real = self.Data_Close.merge(self.Data_Dividend, how='outer', on='date').drop(columns=["Unnamed: 0"])

  def SetupDataSet(self):
    self.Transform()
    arr = np.array(self.Data_Real["close"])
    arr = np.insert(arr,0,1)
    self.Data_Real["close_future"] = arr[:len(arr)-1]
    self.Data_Real["result"] = self.Data_Real.apply(lambda row: caculater_real(row["close"],row["close_future"]),axis=1)
    self.Data_Real["date"] = self.Data_Real.apply(lambda row: formatDate(row["date"]),axis=1)
    # self.Data_Real["change"] = self.Data_Real.apply(lambda row: getChangeClose(row["change_perc"]),axis=1)

  
  def CreateTrainTest(self,startDate = "",startEnd=""):
    self.SetupDataSet()
    Train = self.Data_Real[(self.Data_Real['date'] <= startEnd) & (self.Data_Real['date'] >=startDate)].reset_index(drop=True)
    Test = self.Data_Real[(self.Data_Real['date'] >startEnd)].reset_index(drop=True)
    return Train,Test

if __name__ != "__main__":
    DataSymbol = pd.read_csv("TranformData/InforCom.csv")