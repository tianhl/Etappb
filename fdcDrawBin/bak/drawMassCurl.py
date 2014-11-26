#!/usr/bin/env python
def draw(type,filename):
  fi = open(filename, 'r')
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
 
  if type == 'M':
    massWidthList = massList
  elif type == 'W':
    massWidthList = widthList
    
  minS = min(sValueList)
  minI = sValueList.index(minS)
  minV = massWidthList[minI]
  from ROOT import TGraph
  g = TGraph()
  for i in xrange(len(massWidthList)):
    g.SetPoint(i, massWidthList[i], sValueList[i])

  from ROOT import TF1
  fun1 = TF1('fun1', 'pol3')

  from ROOT import TPostScript, TCanvas
  ps = TPostScript('test.ps')
  c = TCanvas()

  widthS = float(minS) + 0.5
  g.Fit('fun1')
  print 'chi2/nbins: ', fun1.GetChisquare()/len(sValueList)
  leftpoint  = fun1.GetX(widthS, 0.0, float(minV))
  rightpoint =fun1.GetX(widthS, float(minV), massWidthList[-1])
  leftwidth = float(minV) - leftpoint
  rightwidth = rightpoint - float(minV)

  title = 'min: '+ str(minS)+ ' at '+ str(minV) + ' (-' + str( leftwidth) + '/+' + str(rightwidth) + ')'
  g.SetTitle(title)

  g.Draw('AL*')
  ps.Close()

  from time import sleep
  while 1:
    sleep(5)


if __name__ == '__main__':
  import sys, os
  type = sys.argv[1]
  draw(type.upper(), sys.argv[2])

