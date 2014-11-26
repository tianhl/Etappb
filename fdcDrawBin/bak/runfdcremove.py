#! /usr/bin/env python
from runremove import ConnectRemove
outputList = []
threadList = []
def subJob(item, cmd):
  threadList.append(ConnectRemove(item, cmd))

def test():

  from hostList import hostList
  cmdList = ['ssh ' + host + '  "cd workarea; ./bin/runfdc.py ' for host in hostList]
  
  massLow = 1.53
  massUp  = 1.54
  massStep = (massUp - massLow)/len(hostList)
  massList = []
  print massStep
  for i in range(len(hostList)):
    massList.append(massLow + i * massStep)
  cmdList = [cmdList[i] + ' ' + str(massList[i]) + ' 0 1 0.1 0 1 " ' for i in range(len(massList))]  


  cmdList = ['ssh ' + host + ' "' + ' "' for host in hostList]
  map(lambda i:subJob(i, cmdList[i]), range(len(cmdList)))
  map(lambda thread: thread.start(), threadList)
  map(lambda thread: thread.join(), threadList)
  print outputList

if __name__ == '__main__':
  test()
