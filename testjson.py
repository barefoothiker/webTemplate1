import json
import matplotlib.pyplot as plt
import pandas as pd
from lola.lola.runs.render import Render

jsonData = json.loads(open("/Users/mitras/projects/webTemplate/lola/plots/url_csv.json").read())

del jsonData["data"]["url"] 
del jsonData["encoding"]["color"] 

del jsonData["data"]["formatType"]

#jsonData["data"]["url"] = "file:///Users/mitras/projects/webTemplate/data/outData.csv"

df = pd.DataFrame.from_csv("/Users/mitras/projects/webTemplate/data/outData.csv", index_col = None)

df = df[:50]

xValues = df["Rep_333_1_IN"].tolist()
yValues = df["Rep_333_1_IP"].tolist()

jsonData["data"]["values"] = [dict(zip(["Rep_333_1_IN","Rep_333_1_IP"], [xVal,yVal])) for xVal,yVal in zip(xValues, yValues)]

#print (str([dict(zip(["Rep_333_1_IN","Rep_333_1_IP"], [xVal,yVal])) for xVal,yVal in zip(xValues, yValues)]))

#jsonData["data"]["url"] = "file:///Users/mitras/projects/webTemplate/data/outData.csv"

jsonData["mark"] = "point"


jsonData["encoding"]["x"]["field"] = "Rep_333_1_IN"
jsonData["encoding"]["x"]["type"] ="quantitative"

jsonData["encoding"]["y"]["field"] = "Rep_333_1_IP"
jsonData["encoding"]["y"]["type"] ="quantitative"

jsonData["description"] = "Scatter Plot of Rep_333_1_IN vs Rep_333_1_IP"
print (str(json.dumps(jsonData)))

renderer = Render(json.dumps(jsonData))  

renderer.render()