import pandas as pd

ts1 = pd.Timestamp.now()
ts2 = pd.Timestamp.now()

pts1 = ts1.to_pydatetime()
pts2 = ts2.to_pydatetime()

data = [["15",pts1],["16",pts2]]

df1 = pd.DataFrame(data, columns = ["BatLevel","Timestamp"])

print(df1)

df1.to_csv("out.csv", mode = 'a', index= False, header= False )