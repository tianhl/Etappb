#!/usr/bin/env python
def draw():
  fi = open('numScan', 'r')
  lines = fi.readlines()

  numList = []
  numIntList = []
  sVaList = []
  
  number = 0
  for eachLine in lines:
    minS = 'min s is'
    minP = eachLine.find(minS)
    numS = 'mode 1 with diag 1,2'
    numP = eachLine.find(numS)
    if minP > 0:
      sValue = eachLine[minP+len(minS):]
      sValue = float(sValue)
      sVaList.append(sValue)
      number = number + 1
    if numP > 0:
      numF = float(eachLine[:numP].split()[1])*653
      numList.append(numF)
      numIntList.append(int(numF))

  print number
  numDict = {}
  for eachItem in xrange(len(numList)):
    numDict[numIntList[eachItem]] = 0
  for eachItem in xrange(len(sVaList)):
    if  sVaList[eachItem] < numDict[numIntList[eachItem]]:
      numDict[numIntList[eachItem]] = sVaList[eachItem]

  numDictList = numDict.keys()
  numDictList.sort()

  #from decimal import Decimal
  #numDecimalList = []
  #svaDecimalList = []
  #for eachItem in numList:
  #  if eachItem < 450:
  #    continue
  #  if eachItem > 500:
  #    break
  #  numDecimal = Decimal(str(eachItem))
  #  svaDecimal = Decimal(str(numDict[eachItem]))
  #  numDecimalList.append(numDecimal)
  #  svaDecimalList.append(svaDecimal)

  from ROOT import TGraph
  g_1 = TGraph()
  g_1.SetMarkerStyle(8)
  #g.SetMarkerSize(9)
  g_2 = TGraph()
  g_2.SetMarkerStyle(1)
  g_2.SetMarkerColor(2)
  g_3 = TGraph()
  g_3.SetLineColor(2)
  g_3.SetLineWidth(3)

  sCut = -380

  fliterDict = {}
  j = 0
  for i in xrange(len(numDict)):
    if  numDict[numDictList[i]] > sCut:
      continue
    g_1.SetPoint(j, numDictList[i], numDict[numDictList[i]])
    fliterDict[numDictList[i]] = numDict[numDictList[i]]
    j = j + 1

  j = 0
  for i in xrange(len(numList)):
    if sVaList[i] > sCut:
      continue
    g_2.SetPoint(j, numList[i], sVaList[i])
    j = j + 1
  
  binList  = fliterDict.keys()
  binList.sort()
  

  def findMin(list):
    min = 0
    pos = -99
    for i in list:
      if fliterDict[i] < min:
	min = fliterDict[i]
	pos = i
    return pos
  
  def findLeftMin(pos):
    leftBinList  = binList[:binList.index(pos)]
    pos = findMin(leftBinList)
    sortDict[pos]=  fliterDict[pos]
    return pos

  def findRightMin(pos):     
    rightBinList = binList[binList.index(pos)+1:]
    pos = findMin(rightBinList)
    sortDict[pos]=  fliterDict[pos]
    return pos

  sortDict = {}
  minPos = findMin(binList)
  sortDict[minPos]=  fliterDict[minPos]
  
  leftPos = minPos
  while True:
    pos = findLeftMin(leftPos)
    if binList.index(pos) == 0:
      break
    leftPos = pos

  rightPos = minPos
  while True:
    pos = findRightMin(rightPos)
    if binList.index(pos) ==  len(binList)-1:
      break
    rightPos = pos

  xList = []
  yList = []

  sortDictList = sortDict.keys()
  sortDictList.sort()
  for i in sortDictList:
    xList.append(i)
    yList.append(sortDict[i])

  j = 0
  for i in xrange(len(xList)):
    g_3.SetPoint(j, xList[i], yList[i])
    j = j + 1

  from ROOT import TF1
  f1 = TF1('f1', 'pol5',  float(xList[0]), float(xList[-1]))
  g_1.Draw('AP')
  g_2.Draw('P')
  #g_3.Fit('pol6', '', '',  float(binList[0]), float(binList[-1]))
  g_3.Fit(f1)
  g_3.Draw('PL')

  print yList
  from time import sleep
  while 1:
    sleep(5)


if __name__ == '__main__':
  import sys, os
  os.chdir(sys.argv[1])
  draw()

