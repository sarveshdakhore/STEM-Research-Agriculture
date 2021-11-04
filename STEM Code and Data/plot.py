import matplotlib.pyplot as plt
import pandas as pd

def clearAllPlots():
  plt.figure().clear()
  plt.close()
  plt.cla()
  plt.clf()

DataFrame = pd.read_csv("dataset.csv")
variableId = (DataFrame["Variable Id"].unique()) 

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
    plt.ylabel('Value')
    plt.plot(x1, y1, label = country)
    
  title=list(DataFrame.loc[(DataFrame["Variable Id"]==int(varId)),"Variable Name"])[0]
  plt.title(title) #title plotting
  
  # show a legend on the plot
  plt.legend()
  
  # function to save the plot
  plt.savefig("./Graphs/"+str(varId),dpi=2000)
  clearAllPlots()
  
  
