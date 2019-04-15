from processSOUSAdata import * 
import matplotlib.pyplot as mpl 
from sys import argv                    # command line arguments

from matplotlib.font_manager import FontProperties

markersList = [".", "o", "v", "^", "<", ">", "1", "2", "3", "4", "x"]
numMarkers = len(markersList)

def filterNullsFromTwoLists(a, b):
    lenA = len(a)
    lenB = len(b)

    for i in range(lenA):
        if (i < lenB):
            if (b[i].mag == None):
                a[i].mag = None
            if (a[i].mag == None):
                b[i].mag = None


commandLineArgs = argv
if (len(commandLineArgs) != 5):
    print("usage: python3 plot_color_v_color_multiple_supernovae.py x1_filter x2_filter y1_filter y2_filter")
    print("The produced plot will be (x1_filter - x2_filter) vs. (y1_filter - y2_filter)")
    exit()

filesToPlot = getFiles(".dat", "B")

fil_x1 = commandLineArgs[1].upper()
fil_x2 = commandLineArgs[2].upper()

fil_y1 = commandLineArgs[3].upper()
fil_y2 = commandLineArgs[4].upper()

namePrefix = ""
plotTitle = ""
legendList = []

marker_ind = 0

for file in filesToPlot:
    data = getObsList(file)   # get data file
    namePrefix += file.strip("_uvotB15.1.dat")
    plotTitle += file.strip("_uvotB15.1.dat")
    legLabel = file.strip("_uvotB15.1.dat")
    legLabel = legLabel.strip("_uvotB15.1.all.dat")

    legendList.append(legLabel)

    x1 = [item for item in data if item.obsFilter == fil_x1]
    x2 = [item for item in data if item.obsFilter == fil_x2]

    filterNullsFromTwoLists(x1,x2)
    filterNullsFromTwoLists(x2,x1)

    y1 = [item for item in data if item.obsFilter == fil_y1]
    y2 = [item for item in data if item.obsFilter == fil_y2]

    filterNullsFromTwoLists(y1, y2)
    filterNullsFromTwoLists(y2, y1)
    
    
    X1 = [item.mag for item in x1 if item.mag != None]
    X2 = [item.mag for item in x2 if item.mag != None]
    Y1 = [item.mag for item in y1 if item.mag != None]
    Y2 = [item.mag for item in y2 if item.mag != None]

    
    print(legLabel)
    

    lenx1 = len(X1)
    lenx2 = len(X2)
    leny1 = len(Y1)
    leny2 = len(Y2)

    x = []
    y = []

    i = 0
    while i < lenx1 and i < lenx2 and i < leny1 and i < leny2:
        x.append(X1[i] - X2[i])
        y.append(Y1[i] - Y2[i])
        i+=1

    marker_mark = "-" + markersList[marker_ind]
    marker_ind = (marker_ind+1)%numMarkers

    mpl.plot(x,y,marker_mark)


nameOfPlot = namePrefix + fil_x1 + " - " + fil_x2 + "_v_" + fil_y1 + " - " + fil_y2 +".png"
nameOfPlot = "test_output"


mpl.title("Color vs. Color")
mpl.xlabel(fil_x1 + " - " + fil_x2)
mpl.ylabel(fil_y1 + " - " + fil_y2)
mpl.legend(legendList, loc=(.84,.01), prop={'size':6})
mpl.savefig(nameOfPlot)