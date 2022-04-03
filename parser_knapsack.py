#Author: Aikaterini Kentroti

import pandas as pd


def read_inputData(filename,sep,prints=False):
  """ reads files of type File, which contain input data (instance) of the 1-D knapsack problem and returns the whole dataset,
  the number of items, capacity, profits and weights
  Input parameters: file name, seperator"""
  # Read the file with the input data as a pandas dataframe
  df=pd.read_csv(filename,sep)

  #convert string to integers
  df = df.astype(int)

  #number of items
  n=int(list(df.columns)[0])

  #capacity of the knapsack
  capacity=int(list(df.columns)[1])

  #holds the profit for each item
  pr=df.iloc[:,0]
  pr.name="profit"

  #stores the weight of each item
  w=df.iloc[:,1]
  w.name="weight"

  if prints == True:
      print("dataset:\n{} ".format(df),"number of items:\n{}".format(n),"maximum knapsack capacity:\n{}".format(capacity),"profits:\n{}".format(pr),"weights:\n{}".format(w),sep="\n")

  return df,n,capacity,pr,w


#testing the function
# data,n,capacity,pr,w=read_inputData("f10_l-d_kp_20_879", ' ')
# print("dataset:\n{} ".format(data),"number of items:\n{}".format(n),"maximum knapsack capacity:\n{}".format(capacity),"profits:\n{}".format(pr),"weights:\n{}".format(w),sep="\n")