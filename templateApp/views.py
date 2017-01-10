from django.template import RequestContext
from django.shortcuts import render_to_response

from templateApp.models import *
from templateApp.templateAppObjs import *
from templateApp.templateAppConstants import *

import pandas as pd

from bokeh.embed import components
import seaborn as sns

import json
import matplotlib.pyplot as plt

from django.conf import settings

from lola.lola.runs.render import Render

import os, sys, traceback

#@login_required
def landing(request):
    '''Landing'''
    return render_to_response("templateApp/landing.html", {

    },  RequestContext(request))

#@login_required
def handleUpload(request):
    ''' Handle uploaded files'''

    plot_script = ''
    plot_div = ''

    plotTypeId = request.POST.get("plotTypeId","" ) 
    
    jsonFile = ''
    
    try:

        jsonFile = request.FILES['uploadFilePath']
    
        jsonData = str(jsonFile.read(), 'utf-8')   
        
        renderer = Render(jsonData)  

    except:
        pass
    
    #print (" json file = " + str(jsonFile))
    
    if jsonFile == '':
    
        uriFilePath = request.POST.get("uriFilePath","" )    
        fileType = request.POST.get("fileType","" )  
        
        jsonData = json.loads(open(settings.PROJECT_BASE_PATH + "lola/plots/url_csv.json").read())
    
        jsonData["data"]["url"] = uriFilePath
        jsonData["data"]["formatType"] = fileType
        
        renderer = Render(json.dumps(jsonData))    
    
    if plotTypeId == "0":
        plotType = "Line_Plot"
 
    elif plotTypeId == "1":
        plotType = "Scatter_Plot"
        
    elif plotTypeId == "2":

        plotType = "Box_Plot"
        
    elif plotTypeId == "3":

        plotType = "HeatMap_Plot"
        
    elif plotTypeId == "4":
        
        plotType = "Bar_Chart"

    elif plotTypeId == "5":
        
        plotType = "Cluster_Map"
        
    plotName = "outputFig.png" 
    plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName 

    if os.path.isfile(plotPath):
        os.remove(plotPath)        
        
    # seaborn plot
    plt.clf()
    
    #renderer = Render(json.dumps(jsonData))    

    renderer.render()        

    plt.savefig(plotPath)            

    ## bokeh plots
    plot_script, plot_div = components(renderer.render( client_side=True))  
    
    # data fields 
    # none if color not specified
    
    colFlag = True

    x,y,col = renderer.get_fields()
    
    print (" x = " + str(x))
    print (" y = " + str(y))
    print (" col = " + str(col))
    
    if col is None:
        
        colFlag = False
        
    valueList = ''

    xValues,yValues,colorValues = renderer.get_field_values()
        
    if colFlag:
    
        valueList = zip(xValues,yValues,colorValues)
        
    else:

        valueList = zip(xValues,yValues)

    return render_to_response('templateApp/displayPlot.html', {
        "plotTypeId": plotTypeId,
        "plotType":plotType,
        "plot_div":plot_div,
        "plot_script":plot_script,
        "plotPath":plotPath,
        "plotName":plotName,
        
        "x":x,
        "y":y,
        "col":col,

        "valueList":valueList,        
        
    },  RequestContext(request)) 

#@login_required
def processLanding(request):

    ''' Processes landing'''
    templateHomeButton = request.POST.get("templateHomeButton","0" )
    
    plot_script = ''
    plot_div = ''
    
    print (" in landing !!!! ")       

    try:

        if templateHomeButton == "0":
            plotType = "Line_Plot"
            
            print (str(settings.PROJECT_BASE_PATH + "lola/plots/line.json"))
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/line.json","r")
      
        elif templateHomeButton == "1":
            plotType = "Scatter_Plot"
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/scatter.json","r")
            
        elif templateHomeButton == "2":
      
            plotType = "Box_Plot"
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/boxplot.json","r")
            
        elif templateHomeButton == "3":
      
            plotType = "HeatMap_Plot"
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/heatmap.json","r")
            
        elif templateHomeButton == "4":
            
            plotType = "Bar_Chart"
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/barchart.json","r")
        
        elif templateHomeButton == "5":
            
            plotType = "Cluster_Map"
            jsonFile = open(settings.PROJECT_BASE_PATH + "lola/plots/clustermap.json","r")
            
        jsonData = json.load(jsonFile)
            
        plotName = "outputFig.png" 
        plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName 
      
        if os.path.isfile(plotPath):
            os.remove(plotPath)        
            
        # seaborn plot
        plt.clf()
        
        renderer = Render(json.dumps(jsonData))    
      
        renderer.render()        
      
        plt.savefig(plotPath)            
      
        ### bokeh plots
        
        plot_script = ''
        plot_div = ''        

        if plotType != "Cluster_Map":
            plot_script, plot_div = components(renderer.render( client_side=True))  
        
        # data fields 
        # none if color not specified
      
        x,y,col = renderer.get_fields()
        
        #print (renderer.get_fields())
        
        colFlag = True
        
        if col is None:
            colFlag = False
        
        #print (" x = " + str(x))
        #print (" y = " + str(y))
        #print (" col = " + str(col))
      
        xValues,yValues,colorValues = renderer.get_field_values()
        
        valueList = ''
        
        if colFlag:
            
            valueList = zip(xValues, yValues, colorValues)
            
        else:
            
            valueList = zip(xValues, yValues)
        
    except:
      
        traceback.print_exc(file=sys.stdout)		      

        
    return render_to_response('templateApp/displayPlot.html', {
        "plotTypeId": templateHomeButton,
        "plotType":plotType,
        "plot_div":plot_div,
        "plot_script":plot_script,
        "plotPath":plotPath,
        "plotName":plotName,

        "x":x,
        "y":y,
        "col":col,
        
        "colFlag":colFlag,


        "valueList":valueList,

    },  RequestContext(request))        

#@login_required
def selectColumnsSubmit(request):

    try:
        
        datafilePath = request.POST.get("datafilePath",0 )   
        
        columnNames = request.POST.getlist("columnName" )  
        
        labelColumn = request.POST.get("labelColumn" ,"0" )          

        labelValuesString = request.POST.get("labelValues","" )        
        
        labelValues = labelValuesString.split(",") 
        
        print (" labelValues = " + str(labelValues))
        
        columnNames = [x.replace("\r","").replace("\n","") for x in columnNames]
        
        print (str(columnNames))
        
        fileType = request.POST.get("fileType","" )   
        
        plotTypeId = request.POST.get("plotTypeId", 0 )           
    
        filePath = settings.DATA_OUTPUT_FOLDER
                 
        df = pd.DataFrame.from_csv(filePath + "/" + str(datafilePath) +".csv" , index_col = None ) 
        
        print (df [labelColumn])
        
        print (df )        
        
        dfSelected = df[ df [labelColumn].isin(labelValues)  ]

        print (" dfSelected = " + str(dfSelected))
        
        jsonData = json.loads(open(settings.PROJECT_BASE_PATH + "lola/plots/url_csv.json").read())        

        del jsonData["data"]["url"] 
        del jsonData["encoding"]["color"] 
        
        del jsonData["data"]["formatType"]
        
        jsonData["metadata"] = {}
        
        jsonData["metadata"]["labels"] = []
        
        for index, selectedRow in dfSelected.iterrows():
            
            jsonData["metadata"]["labels"].append([selectedRow[labelColumn],selectedRow[columnNames[0]],selectedRow[columnNames[0]] ]) 
            
            print (" adding " + str([selectedRow[labelColumn],selectedRow[columnNames[0]],selectedRow[columnNames[0]] ]))
        
        xValues = df[columnNames[0]].tolist()
        yValues = df[columnNames[1]].tolist()
        
        jsonData["data"]["values"] = [dict(zip(columnNames, [xVal,yVal])) for xVal,yVal in zip(xValues, yValues)]
        
        jsonData["mark"] = "point"
        
        jsonData["encoding"]["x"]["field"] = columnNames[0]
        jsonData["encoding"]["x"]["type"] ="quantitative"
        
        jsonData["encoding"]["y"]["field"] = columnNames[1]
        jsonData["encoding"]["y"]["type"] ="quantitative"
        
        jsonData["description"] = "Scatter Plot of " + str(columnNames[0]) + " vs " + str(columnNames[1])
        
        print (str(json.dumps(jsonData)))
        
        renderer = Render(json.dumps(jsonData))  
        
        renderer.render()
    
        if plotTypeId == "0":
            plotType = "Line_Plot"
     
        elif plotTypeId == "1":
            plotType = "Scatter_Plot"
            
        elif plotTypeId == "2":
    
            plotType = "Box_Plot"
            
        elif plotTypeId == "3":
    
            plotType = "HeatMap_Plot"
            
        elif plotTypeId == "4":
            
            plotType = "Bar_Chart"
            
        elif plotTypeId == "5":
            
            plotType = "Cluster Map"
            
        plotName = "outputFig.png" 
        plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName 
    
        if os.path.isfile(plotPath):
            os.remove(plotPath)        
            
        # seaborn plot
        plt.clf()
    
        renderer.render()        
    
        plt.savefig(plotPath)            
    
        ## bokeh plots
        plot_script, plot_div = components(renderer.render( client_side=True))  
        
        # data fields 
        # none if color not specified
        
        colFlag = True
    
        x,y,col = renderer.get_fields()
        
        if col is None:
            
            colFlag = False
            
        valueList = ''
    
        xValues,yValues,colorValues = renderer.get_field_values()
        
        if len (xValues) > 500:
            
            xValues = xValues[:500]
            yValues = yValues[:500]
            
        if colFlag:

            if len (colorValues) > 500:
                
                colorValues = colorValues[:500]
        
            valueList = zip(xValues,yValues,colorValues)
            
        else:
    
            valueList = zip(xValues,yValues)
            
    except:
  
        traceback.print_exc(file=sys.stdout)
  
    return render_to_response('templateApp/displayPlot.html', {

        "plotTypeId": plotTypeId,
        "plotType":plotType,
        "plot_div":plot_div,
        "plot_script":plot_script,
        "plotPath":plotPath,
        "plotName":plotName,

        "x":x,
        "y":y,
        "col":col,

        "valueList":valueList,
    
     },  RequestContext(request))

#@login_required
def selectColumns(request):
    
    print (" ************** file path = " )    
  
    try:
        
      datafilePath = request.FILES['uploadFilePath']
      
      plotTypeId = request.POST.get('plotTypeId',0)    
      
      fileType = request.POST.get('fileType','')
      
      print (" ************** file path = " + str(datafilePath))       
  
      data = str( datafilePath.read(),'utf-8')
      
      #print (str(data))
         
      datafileLines = data.split("\n")
       
      valueList = []
      
      columns = []
      
      print (str(len(datafileLines)))
      
      for index, line in enumerate ( datafileLines ) :
        
        print (line) 
 
        if fileType == "csv":
          
            values = line.replace("\t","").split(",")
            
        else: 
          
            values = line.split("\t")
  
        if index == 0:
            
          #print (" columns are " + str(columns) )
               
          columns = values
          
        else:    
          valueList.append(values[:len(columns)])
  
      filePath = settings.DATA_OUTPUT_FOLDER
               
      if not os.path.isdir( filePath ):
        os.mkdir(filePath)
      
      df = pd.DataFrame(valueList, columns = columns)
  
      valueList = valueList[:DISPLAY_LIST_MAX_NUM]
      
      df.to_csv(filePath + "/" + str(datafilePath) + ".csv" , index = False )    
  
    except:
      traceback.print_exc(file=sys.stdout)
  
    return render_to_response('templateApp/selectColumns.html', {
  
        "columns": columns,
        "valueList":valueList[:DISPLAY_LIST_MAX_NUM],
        "datafilePath":datafilePath,
        "plotTypeId":plotTypeId,
        "fileType":fileType,        
    },  RequestContext(request))
