#! /usr/bin/env python

from hostList import hostList

outputList = []
threadList = []
def cpfromremove(num):
  max = int(num)
  from os import mkdir, path
  dirList = map(lambda host: host.split('.')[0], hostList[:max])
  dirList = filter(lambda dir: not path.exists(dir), dirList)
  map(lambda dir: mkdir(dir), dirList)
  #cmdList = ['scp ' + hostList[i] + ':/home/tianhl/workarea/' \
  #    + hostList[i].split('.')[0] + '/fort/mplot.hbook ' \
  #    + hostList[i].split('.')[0] + '/' \
  #    for i in range(max)]
  #map2remove(cmdList)
  #print 'cp mplot'
  #cmdList = ['scp ' + hostList[i] + ':/home/tianhl/workarea/' \
  #    + hostList[i].split('.')[0] + '/fort/dplot.hbook ' \
  #    + hostList[i].split('.')[0] + '/' \
  #    for i in range(max)]
  #map2remove(cmdList)
  #print 'cp dplot'
  #cmdList = ['scp ' + hostList[i] + ':/home/tianhl/workarea/' \
  #    + hostList[i].split('.')[0] + '/fort/mplot.info ' \
  #    + hostList[i].split('.')[0] + '/' \
  #    for i in range(max)]
  #map2remove(cmdList)
  #print 'cp mplot.info'
  #cmdList = ['cd ' + hostList[i].split('.')[0] + '; h2root mplot.hbook mplot.root' for i in range(max)]
  #map2remove(cmdList)
  #print 'h2root mplot'
  #cmdList = ['cd ' + hostList[i].split('.')[0] + '; h2root dplot.hbook dplot.root' for i in range(max)]
  #map2remove(cmdList)
  #print 'h2root dplot'

def map2remove(cmdList):  
  map(lambda i: outputList.append('error, no output'),  range(len(cmdList)))
  map(lambda i:subJob(i, cmdList[i]), range(len(cmdList)))
  map(lambda thread: thread.start(), threadList)
  map(lambda thread: thread.join(), threadList)
  del threadList[:]

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
    num = sys.argv[1]
    cpfromremove(num)
