import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

def clearAllPlots():
  fig = plt.figure()
  plt.figure().clear()
  plt.close()
  plt.cla()
  plt.clf()

DataFrame = pd.read_csv("dataset.csv")
variableId = (DataFrame["Variable Id"].unique()) #4100

for varId in variableId:
  filteredDataViaVariableId = DataFrame[(DataFrame["Variable Id"]==int(varId))]
  contries = (filteredDataViaVariableId["Area"].unique())
  for country in contries:
    filteredDataOfCountry = filteredDataViaVariableId[(filteredDataViaVariableId["Area"]==country)]
    
    x1 = list(filteredDataOfCountry["Year"])
    y1 = list(filteredDataOfCountry["Value"])
    
    # naming the x axis
    plt.xlabel('Year')
    # naming the y axis
    plt.ylabel('\n Value')
    plt.plot(x1, y1, label = country)
    
  title=list(DataFrame.loc[(DataFrame["Variable Id"]==int(varId)),"Variable Name"])[0]
  plt.title(title)
  
  # show a legend on the plot
  plt.legend()
  
  # function to show the plot
  plt.savefig("./Graphs/"+str(varId),dpi=2000)
  clearAllPlots()








































