#! /usr/bin/env python

from hostList import hostList

outputList = []
threadList = []
def fileCmd(cmdFile):
  fi = open(cmdFile, 'r')
  cmdList = fi.readlines()
  fi.close()

  length = min(len(cmdList), len(hostList))
  cmdList = ['ssh ' + hostList[i] + ' "' + cmdList[i][:-1] + ' "' for i in range(length)]
  map2remove(cmdList)

def singleCmd(cmdStr):
  cmdList = ['ssh ' + host + ' "' + cmdStr + ' "' for host in hostList]
  map2remove(cmdList)

def map2remove(cmdList):  
  map(lambda i: outputList.append('error, no output'),  range(len(cmdList)))
  map(lambda i:subJob(i, cmdList[i]), range(len(cmdList)))
  map(lambda thread: thread.start(), threadList)
  map(lambda thread: thread.join(), threadList)

import commands, threading, time
class ConnectRemove(threading.Thread):
  def __init__(self, item, cmd):
    threading.Thread.__init__(self)
    self.cmd = cmd
    self.item = item

  def run(self): 
    print '# run at remove host: ', self.cmd
    output =  '#############################\n'
    output += '#  ' + self.cmd + '\n'
    output += '#############################\n'
    output += commands.getoutput(self.cmd)
    output += '\n'
    outputList[self.item] = output

def subJob(item, cmd):
  threadList.append(ConnectRemove(item, cmd))
  pass

if __name__ == '__main__':
  
  import sys
  if len(sys.argv) == 2:
    cmd = sys.argv[1]
    singleCmd(cmd)
  if sys.argv[1] == '-f' and len(sys.argv) == 3:
    cmd = sys.argv[2]
    fileCmd(cmd)

  for output in outputList:
    print output
