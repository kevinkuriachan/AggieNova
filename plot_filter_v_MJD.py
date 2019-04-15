from processSOUSAdata import getObsList
import matplotlib.pyplot as mpl 
from sys import argv                    # command line arguments

commandLineArgs = argv
if (len(commandLineArgs) != 3):
    print("usage: python3 plot_filter_v_MJD.py filename.dat filterType")
    exit()


data = getObsList(commandLineArgs[1])   # get data file
fil = commandLineArgs[2].upper()

days = [item.time for item in data if item.obsFilter == fil]
mags = [item.mag for item in data if item.obsFilter == fil]

nameOfPlot = commandLineArgs[1].strip(".dat") + "_" + fil + ".png"

mpl.rcParams.update({'font.size': 15})
mpl.gca().invert_yaxis()

mpl.title(commandLineArgs[1].strip("_uvotB15.1.dat"))
mpl.plot(days,mags,'-o')
mpl.xlabel("time (MJD)")
mpl.ylabel("magnitude")
mpl.savefig(nameOfPlot)
