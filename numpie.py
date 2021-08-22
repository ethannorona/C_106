import csv
import numpy as np

def getDataSource(data_path):
    iceCream_sales = []
    coldDrink_sales = []

    with open(data_path) as csv_file:
      df = csv.DictReader(csv_file)
      
      for row in df: 
        iceCream_sales.append(float(row["Temperature"])) 
        coldDrink_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
        
    return {"x" : iceCream_sales, "y" : coldDrink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between tempertaure vs ice cream: ", correlation[0,1] )
    
def setup():
    data_path = "./data/ice_cream_and_temperature.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    
setup()