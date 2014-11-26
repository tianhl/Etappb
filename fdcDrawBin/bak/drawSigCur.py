#!/usr/bin/env python
def draw():
  fi = open('sValue', 'r')
  lines = fi.readlines()
  #from decimal import Decimal
  massList   =[]
  widthList  =[]
  sValueList = []
  for eachline in lines:
    items = eachline.split()

    mass   = float(items[0])
    width  = float(items[1])
    sValue = float(items[2]) + 386.491608
    massList.append(mass)
    widthList.append(width)
    sValueList.append(sValue)
 
  minS = min(sValueList)
  minI = sValueList.index(minS)
  minM = massList[minI]
  from ROOT import TGraph
  g = TGraph()
  for i in xrange(len(massList)):
    g.SetPoint(i, massList[i], sValueList[i])

  from ROOT import TF1
  fun1 = TF1('fun1', 'pol3')

  from ROOT import TPostScript, TCanvas
  ps = TPostScript('test.ps')
  c = TCanvas()

  #g.Fit('fun1')
  #title = 'min: '+ str(fun1.GetMinimum())+ ' at '+ str(fun1.GetMinimumX())
  widthS = float(minS) + 0.5
  g.Fit('fun1')
  leftpoint  = fun1.GetX(widthS, 0.0, float(minM))
  rightpoint =fun1.GetX(widthS, float(minM), 10000.)
  leftwidth = float(minM) - leftpoint
  rightwidth = rightpoint - float(minM)

  title = 'min: '+ str(minS)+ ' at '+ str(minM) 
  g.SetTitle(title)

  g.Draw('AL*')
  ps.Close()

  from time import sleep
  while 1:
    sleep(5)


if __name__ == '__main__':
  import sys, os
  os.chdir(sys.argv[1])
  draw()

