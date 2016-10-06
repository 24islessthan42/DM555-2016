list1 = ["ABE","BD","CDF","ABD","ACE","BCEF","ACE","ABCE","ABCDF","BCDE"]
list2 = ["BEGH","ABCEGH","ABCEFH","BCDEFGHL","ABEKH","BEFGHIK","ABDGH","ABDG","BDFG","CEF","ACEFH","ABEG"]

prevPruned = []

def apriori(listi,threshold):
    frequentSets = 0
    print "Given Threshold:", threshold
    print "Given Domain", listi
    di = createDict(listi)
    di = pruner(di,threshold)
    while len(di.items()) != 0:
        print "\nFrequent S", len(di.items()[0][0]), di
    #    dictToLatexTabel(di,"S" + str(len(di.items()[0][0])))
        frequentSets = frequentSets + len(di.items())
        di = updateDict(cN(di),listi,threshold)
    print "All Pruned Sets: ", prevPruned
    print "FrequentSets: ", frequentSets

def maxItem(listi):
    maxlen = 0
    maxstr = ""
    for i in listi:
        if len(i) > maxlen:
            maxlen = len(i)
            maxstr = i
    print "Max str = ", maxstr, "\nLenght = ", maxlen

#Creates the initial dictionary containing subsets of length 1
def createDict(listi):
    dictunary = {}
    resDict = {}
    for l in listi:
        for i in l:
            if(dictunary.has_key(i)):
                dictunary[i] = dictunary[i] + 1
            else :
                dictunary.update({i : 1})
    return dictunary

#Runs through the dictionary and discards objects with a to small threshold
def pruner(dicti,threshold):
    newdict = {}
    keys = dicti.keys()
    nrElemPruned = 0
    elemPruned = []
    print "Dicti before Prune: ", dicti
    for i in range(len(dicti.items())):
        if dicti[keys[i]] >= threshold:
            newdict.update({keys[i] : dicti[keys[i]]})
        else :
            elemPruned.append(keys[i])
            nrElemPruned = nrElemPruned + 1
    if nrElemPruned < 1:
        print "No Elements Pruned"
    else :
        print "Elements Pruned due to Threshold: ", nrElemPruned, "\nThese: ", elemPruned
    for item in elemPruned:
        prevPruned.append(item)
    return newdict

#Creates the next list of items so from S_k -> C_k+1, but can't subtract earlier pruned subsets from C_k+1
def cN(dicti):
    startList = []
    resList = []
    k = len(dicti.items()[0][0])
    #print "Prev Pruned ", prevPruned[k-2]
    for key in sorted(dicti):
        startList.append(key)
    length = len(startList[0])
    for i in range(len(startList)):
        j = i+1
        while j < len(startList):
            if startList[i][length-1] != startList[j][length-1] and startList[i][:k-1] == startList[j][:k-1]:
                resList.append(startList[i]+startList[j][length-1])
            j = j+1
    print"C",k+1,"Candidate Set:", resList
    resList = cnPruner(resList)
    return resList

def cnPruner(resList):
    nPruned = []
    nres = []
    for el in resList:
        tCount = 0
        isPruned = False
        for ppel in prevPruned:
            charCount = 0
            for char in ppel:
                res = el.find(char)
                if res != -1:
                    charCount = charCount + 1
            if charCount == len(ppel):
                 nPruned.append(el)
                 isPruned = True
        if isPruned == False:
            nres.append(el)
    print "C", len(nres[0]), "After Pruning prevPruned", nres
    print "Elements Pruned cause containing subset of prevPruned ", nPruned
    #print "Res is: ", nres
    return nres

#Char in each checklist if the are in each transaction, and count how many times, they totally occur.
def updateDict(cList,tList,threshold):
    resDict = {}
    for tl in tList:
        for cL in cList:
            notinTransaction = False
            for char in cL:
                res = tl.find(char)
                if res == -1:
                    notinTransaction = True
                    break
            if notinTransaction == False:
                if resDict.has_key(cL):
                    resDict[cL] = resDict[cL] + 1
                else:
                    resDict.update({cL : 1})
    resDict = pruner(resDict,threshold)
    return resDict


def dictToLatexTabel(dicti,title):
    print "\n\\begin{center}"
    print "\\captionof{table}{",title,"}"
    print "\\begin{tabular}{|c|c|}"
    print "\\hline\nTransID & Items \\\\ \\hline"

    di = dicti.items()
    for item in sorted(di):
        print item[0], "&", item[1], "\\\\"
    print "\\hline \n\\end{tabular}"
    print "\\end{center}"

def listToLatexTabel(listi,title):
    listi= sorted(listi)
    print "\n\\begin{center}"
    print "\\captionof{table}{",title,"}"
    print "\\begin{tabular}{|c|}"
    print "\\hline\n Candidates \\\\ \\hline"

    for item in listi:
        print item,"\\\\"
    print "\\hline \n\\end{tabular}"
    print "\\end{center}"


apriori(list1,2)
