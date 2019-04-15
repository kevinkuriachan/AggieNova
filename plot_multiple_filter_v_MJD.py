from processSOUSAdata import getObsList
import matplotlib.pyplot as mpl 
from sys import argv                    # command line arguments

commandLineArgs = argv
if (len(commandLineArgs) <= 3):
    print("usage: python3 plot_filter_v_MJD.py filename.dat filterType1 filterType2 filterType3, ..., filterTypeN")
    exit()

numFils = len(commandLineArgs) - 3

pltColors = ['b','r','k','g','c','m']
pltColorPtr = 0

if (numFils > len(pltColors)):
    print("too many")
    exit()


nameOfPlot = commandLineArgs[1].strip(".dat") 
legendList = []

for i in range(2,len(commandLineArgs)):

    data = getObsList(commandLineArgs[1])   # get data file
    fil = commandLineArgs[i].upper()

    print(fil)

    nameOfPlot += "_" + fil

    days = [item.time for item in data if item.obsFilter == fil]
    mags = [item.mag for item in data if item.obsFilter == fil]

    legendList.append(fil)

    mpl.rcParams.update({'font.size': 15})

    mpl.plot(days,mags,'-o')


mpl.title(commandLineArgs[1].strip("_uvotB15.1.dat"))
mpl.gca().invert_yaxis()

nameOfPlot += ".png"
mpl.xlabel("time (MJD)")
mpl.ylabel("magnitude")
mpl.legend(legendList)
mpl.savefig(nameOfPlot)
