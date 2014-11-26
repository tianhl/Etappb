#!/usr/bin/env python
def draw(type):
  fi = open('sValue', 'r')
  lines = fi.readlines()
  from decimal import Decimal
  massList   =[]
  widthList  =[]
  sValueList = []
  for eachline in lines:
    items = eachline.split()

    mass   = Decimal(items[0])
    width  = Decimal(items[1])
    sValue = Decimal(items[2])
    massList.append(mass)
    widthList.append(width)
    sValueList.append(sValue)
 
  minS = min(sValueList)
  minI = sValueList.index(minS)
  minW = widthList[minI]
  from ROOT import TGraph
  g = TGraph()
  for i in xrange(len(widthList)):
    g.SetPoint(i, widthList[i], sValueList[i])

  from ROOT import TF1
  fun1 = TF1('fun1', 'pol3')

  from ROOT import TPostScript, TCanvas
  ps = TPostScript('test.ps')
  c = TCanvas()
  
  widthS = float(minS) + 0.5
  g.Fit('fun1')
  print 'chi2/nbins: ', fun1.GetChisquare()/len(sValueList)
  leftpoint  = fun1.GetX(widthS, 0.0, float(minW))
  rightpoint =fun1.GetX(widthS, float(minW), widthList[-1])
  leftwidth = float(minW) - leftpoint
  rightwidth = rightpoint - float(minW)

  title = 'min: '+ str(minS)+ ' at '+ str(minW) + ' (-' + str( leftwidth) + '/+' + str(rightwidth) + ')'
  g.SetTitle(title)

  g.Draw('AL*')
  ps.Close()

  from time import sleep
  while 1:
    sleep(5)


if __name__ == '__main__':
  import sys, os
  type = sys.argv[1]
  os.chdir(sys.argv[2])
  draw(type.upper())

