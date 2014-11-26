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

  sCut = -375

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
  
  binWidth = 20
  binList  = fliterDict.keys()
  binList.sort()
  print binList
  bins     = len(binList)/binWidth
  offset   = len(binList)-binWidth*bins
  print 'len:    ', len(binList)
  print 'bins:   ', bins
  print 'offset: ', offset
  
  xList = []
  yList = []
  for eachbin in xrange(bins):
    if eachbin < bins - 1:
      x = 0.0
      y = 0.0
      for item in xrange(binWidth):
	binIndex = eachbin*binWidth + item
	x =  x + binList[binIndex]
	if fliterDict[binList[binIndex]] <= y:
	  y = fliterDict[binList[binIndex]]
      print 'x = ', x/binWidth
      print 'y = ', y
      xList.append(x/binWidth)
      yList.append(y)
    else:
      x = 0.0
      y = 0.0
      for item in xrange(offset):
	binIndex = eachbin*binWidth + item
	print binList[binIndex]
	x =  x + binList[binIndex]
	if fliterDict[binList[binIndex]] <= y:
	  y = fliterDict[binList[binIndex]]
      print 'x = ', x/offset
      print 'y = ', y
      xList.append(x/offset)
      yList.append(y)

  j = 0
  for i in xrange(bins):
    g_3.SetPoint(j, xList[i], yList[i])
    j = j + 1

  g_1.Draw('AP')
  g_2.Draw('P')
  g_3.Draw('PL')

  from time import sleep
  while 1:
    sleep(5)
#  from decimal import Decimal
#  massList   =[]
#  widthList  =[]
#  sValueList = []
#  for eachline in lines:
#    items = eachline.split()
#
#    mass   = Decimal(items[0])
#    width  = Decimal(items[1])
#    sValue = Decimal(items[2])
#    massList.append(mass)
#    widthList.append(width)
#    sValueList.append(sValue)
# 
#  minS = min(sValueList)
#  minI = sValueList.index(minS)
#  minM = massList[minI]
#
#  from ROOT import TF1
#  fun1 = TF1('fun1', 'pol3')
#
#  from ROOT import TPostScript, TCanvas
#  ps = TPostScript('test.ps')
#  c = TCanvas()
#
#  #g.Fit('fun1')
#  #title = 'min: '+ str(fun1.GetMinimum())+ ' at '+ str(fun1.GetMinimumX())
#  widthS = float(minS) + 0.5
#  g.Fit('fun1')
#  leftpoint  = fun1.GetX(widthS, 0.0, float(minM))
#  rightpoint =fun1.GetX(widthS, float(minM), 10000.)
#  leftwidth = float(minM) - leftpoint
#  rightwidth = rightpoint - float(minM)
#
#  title = 'min: '+ str(minS)+ ' at '+ str(minM) + ' (-' + str( leftwidth) + '/+' + str(rightwidth) + ')'
#  g.SetTitle(title)
#


if __name__ == '__main__':
  import sys, os
  os.chdir(sys.argv[1])
  draw()

