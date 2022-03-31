import matplotlib.pyplot as plt
import pandas as pd 

while True:
  try:
    dpi = int(input("\n\nDPI(max-3000, min-100): "))
    if dpi<0:
      dpi = dpi*-1
    if dpi>3000 or dpi<100:
      print("Out of limit\n")
    else:
      break
  except:
    print("Unexpected Input... Try Again\n\n")

def clearAllPlots():
  plt.figure().clear()
  plt.close()
  plt.cla()
  plt.clf()

DataFrame = pd.read_csv("dataset.csv")
variableId = (DataFrame["Variable Id"].unique()) 

def percentage(current,total):
  percent = (current*100/total)
  print(f"{percent:.1f}", end='\r')
  if int(percent) == 100:
    print("Task Completed")
  
current = 0
total = int(len(variableId))
for varId in variableId:
  current+=1
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
  plt.title(title)
  
  # show a legend on the plot
  plt.legend()
  
  # function to save the plot
  plt.savefig("./Graphs/"+str(varId),dpi=dpi)
  clearAllPlots()
  percentage(current=current,total=total)
