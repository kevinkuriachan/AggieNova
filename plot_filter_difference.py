from processSOUSAdata import getObsList
import matplotlib.pyplot as mpl 
from sys import argv                    # command line arguments


def filterNullsFromTwoLists(a, b):
    lenA = len(a)
    lenB = len(b)

    for i in range(lenA):
        if (i < lenB):
            if (b[i].mag == None):
                a[i].mag = None


commandLineArgs = argv
if (len(commandLineArgs) != 6):
    print("usage: python3 plot_filter_v_MJD.py filename.dat x1_filter x2_filter y1_filter y2_filter")
    print("The produced plot will be (x1_filter - x2_filter) vs. (y1_filter - y2_filter)")
    exit()


data = getObsList(commandLineArgs[1])   # get data file
fil_x1 = commandLineArgs[2].upper()
fil_x2 = commandLineArgs[3].upper()

fil_y1 = commandLineArgs[4].upper()
fil_y2 = commandLineArgs[5].upper()

x1 = [item for item in data if item.obsFilter == fil_x1]
x2 = [item for item in data if item.obsFilter == fil_x2]

filterNullsFromTwoLists(x1,x2)
filterNullsFromTwoLists(x2,x1)

y1 = [item for item in data if item.obsFilter == fil_y1]
y2 = [item for item in data if item.obsFilter == fil_y2]

filterNullsFromTwoLists(y1, y2)
filterNullsFromTwoLists(y2, y1)

X1 = [item for item in x1 if item.mag != None]
X2 = [item for item in x2 if item.mag != None]
Y1 = [item for item in y1 if item.mag != None]
Y2 = [item for item in y2 if item.mag != None]

lenx1 = len(X1)
lenx2 = len(X2)
leny1 = len(Y1)
leny2 = len(Y2)

x = []
y = []

i = 0
while i < lenx1 and i < lenx2 and i < leny1 and i < leny2:
    x.append(X1[i].mag - X2[i].mag)
    y.append(Y1[i].mag - Y2[i].mag)
    i+=1


nameOfPlot = commandLineArgs[1].strip(".dat") + fil_x1 + " - " + fil_x2 + "_v_" + fil_y1 + " - " + fil_y2 +".png"


mpl.rcParams.update({'font.size': 15})

mpl.title(commandLineArgs[1].strip("_uvotB15.1.dat"))
mpl.plot(x,y,'-o')
mpl.xlabel(fil_x1 + " - " + fil_x2)
mpl.ylabel(fil_y1 + " - " + fil_y2)
mpl.savefig(nameOfPlot)
