import os

filterList = ["V", "B", "U", "UVW1", "UVM2", "UVW2"]

class observation:
    obsFilter = ""
    time = 0.0
    mag = 0.0
    magErr = 0.0
    sigMagLim3 = 0.0 
    satLim = 0.0
    rate = 0.0
    rateErr = 0.0
    ap = 0.0
    frametime = 0.0
    exp = 0.0
    telapse = 0.0

    def __init__(self, line):
        info = line.split()
        self.obsFilter = info[0]
        self.time = float(info[1])
        if (info[2] != "NULL"):
            self.mag = float(info[2])
        else:
            self.mag = None
        if (info[3] != "NULL"):
            self.magErr = float(info[3])
        else:
            self.magErr = None
        if (info[4] != "NULL"):
            self.sigMagLim3 = float(info[4])
        else:
            self.sigMagLim3 = None

        if (info[5] != "NULL"):
            self.satLim = float(info[5])
        else:
            self.satLim = None
        
        if (info[6] != "NULL"):
            self.rate = float(info[6])
        else:
            self.rate = None

        if (info[7] != "NULL"):
            self.rateErr = float(info[7])
        else:
            self.rateErr = None

        if (info[8] != "NULL"):
            self.ap = float(info[8])
        else:
            self.ap = None
        
        if (info[9] != "NULL"):
            self.frametime = float(info[9])
        else:
            self.frametime = None

        if (info[10] != "NULL"):
            self.exp = float(info[10])
        else:
            self.exp = None

        if (info[11] != "NULL" and info[11] != "**********"):
            self.telapse = float(info[11])
        else:
            self.telapse = None


    def printInfo(self):
        print("---------------------------------")
        print("Filter: \t ", self.obsFilter)
        print("MJD[days]: \t ", self.time)
        print("Mag: \t \t ", self.mag)
        print("MagErr: \t ", self.magErr)
        print("3SigMagLim: \t ", self.sigMagLim3)
        print("0.98SatLim[mag]: ", self.satLim)
        print("Rate[c/s]: \t ", self.rate)
        print("RateErr[c/s]: \t ", self.rateErr)
        print("Ap[arcsec]: \t ", self.ap)
        print("Frametime[s]: \t ", self.frametime)
        print("Exp[s]: \t ", self.exp)
        print("Telpse[s]: \t ", self.telapse)
        print("---------------------------------")
    
'''
# TO DO : create supernovae class 
class supernova:
    name = ""
    observations = list()

    __init__(self):
        pass 

    addObs(self, observation obs):
        pass
    

class novaeData:
    novae = dict()
'''


def getFilesCurrentDirectory(extension):
    datFiles = []
    for root, dirs, files in os.walk("."):  #current all items in current directory    
        for filename in files:
            if (filename.endswith(extension)):
                datFiles.append(filename)
    return datFiles

def getFiles(extension, option):
    filesToRead = []
    if (option == "A"):         #   read one file 
        fileName = input("which file? : " )
        while (not fileName.endswith(extension)):
            fileName = input("choose a *.dat file: ")
        filesToRead.append(fileName)
    elif (option == "B"):       #   read many files
        filesToRead = getFilesCurrentDirectory(extension)
    return filesToRead


def isValidLine(line):
    if (len(line) <= 1):
        return False
    if (line[0] not in filterList):
        return False
    return True


def getObsList(fileName):
    obs = []
    with open(fileName) as datFile:
        for line in datFile:
            if isValidLine(line):
                obs.append(observation(line))
    return obs 


def countMaxOccurance():
    
    print("A: read 1 (one) specific file")
    print("B: read all files in the current directory")
    validOptions = ["A", "B"]
    option = input("What do you want to do: ")
    while option.upper() not in validOptions:
        option = input("Choose one of the above options: ")

    option = option.upper()

    filesToRead = getFiles(".dat", option)
    
    obsList = []

    fileNameToObs = dict()

    for fileName in filesToRead:
        print(fileName)
        fileNameToObs.setdefault(fileName,getObsList(fileName))

    
    
    maxObsFil = ""
    maxObsFile = ""
    maxObsCount = 0

    for f in fileNameToObs:
        filterToCount = dict()
        filterList = ["V", "B", "U", "UVW1", "UVM2", "UVW2"]
        for fil in filterList:
            filterToCount.setdefault(fil, 0)

        for obs in fileNameToObs[f]:
            filterToCount[obs.obsFilter] += 1
        
        maxF = 0
        maxFil = ""

        for key in filterToCount:
            if filterToCount[key] > maxF:
                maxF = filterToCount[key]
                maxFil = key

        if maxF > maxObsCount:
            maxObsCount = maxF
            maxObsFil = maxFil
            maxObsFile = f

                    
        
    print("--------------------------")
    print(maxObsFile)
    print(maxObsFil)
    print(maxObsCount)


#below is a sample of usage:

'''
def main():
    
    print("A: read 1 (one) specific file")
    print("B: read all files in the current directory")
    validOptions = ["A", "B"]
    option = input("What do you want to do: ")
    while option.upper() not in validOptions:
        option = input("Choose one of the above options: ")

    option = option.upper()

    filesToRead = getFiles(".dat", option)
    
    obsList = []
    for fileName in filesToRead:
        print(fileName)
        obsList += getObsList(fileName)
    for obs in obsList:
       obs.printInfo() 

main()
'''

#countMaxOccurance()
    