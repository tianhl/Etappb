#!/usr/bin/env python
def draw():
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
  print 'min s: ', minS


if __name__ == '__main__':
  import sys, os
  os.chdir(sys.argv[1])
  draw()

