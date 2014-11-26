#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5

############################################
############################################

#===========================================

#  if list.__len__() <= 0:
#    return []
#  elif list.__len__() == 1: 
#    return list
#
#  temp0 = list[0]
#  temp1 = list[1:]
#  if temp1.count(temp0) > 0: 
#    tempList = reduceRunList(temp1)
#    return tempList
#  elif temp1.count(temp0) == 0: 
#    tempList = reduceRunList(temp1)
#    tempList.append(temp0)
#    return tempList 

#===========================================
def reduceFileName(directoryName):    
  import os
  fileList = map(lambda f: os.path.normcase(f), os.listdir(directoryName)) #list directory
  fileList = filter(lambda f: os.path.isfile(os.path.join(directoryName, f)) and \
      os.path.splitext(f)[1].lower()[1:] == 'rec', fileList) # remove no file and no rec file
  # get (fullDirectory, run number)
  fileDetail = map(lambda f: (os.path.join(directoryName, f), os.path.splitext(f)[0].split('_')[1]), fileList) 

  #def reduceRunList(list):
  #  #list = filter(lambda f: f.isdigit(), list)
  #  #list = set(list)
  #  #list = map(lambda r: r, list)
  #  #return list    

  runList = map(lambda f: f[1], fileDetail) # get run No. list
  runList = [r for r in sorted(set(runList)) if r.isdigit()] #only appears one time 

  def getFileNo(runNo): 
    # get file information only if the file's run No. matchs the given run No.
    #fileInEachRun = filter(lambda f: f[1] == runNo, fileDetail)
    #fileInEachRun = map(lambda d: '"' + d[0] + '"', fileInEachRun) # get file name list in each run
    fileInEachRun = [ '"' + f[0] + '"' for f in fileDetail if f[1] == runNo]# get file name list in each run
    fileInEachRun = reduce(lambda d0, d1:  d0 + ', ' + d1 , fileInEachRun) #get string of file list
    return (runNo, fileInEachRun)

  runFileCouple = map(lambda r: getFileNo(r), runList) # get fullDirectory and run No. of each run
  return runFileCouple # [(runNo, fileInEachRun), (runNo, fileInEachRun), ...]

#===========================================
def getRunFileCouple():
  import os
  recFileDir = '/besfs/offline/data/640new/rec/'
  dataList = ['904', '912', '929']
  recDirList = map(lambda d: recFileDir + d + '/', dataList)  # get full directory name list
  recDirList = filter(lambda d: os.path.isdir(d), recDirList)  # remove error directory 
  runFileList = map(lambda d: reduceFileName(d), recDirList)  # get full information about file
  runFileList = reduce(lambda r0, r1: r0 + r1, runFileList )  # one list contains all (runNo, fileList)
  return runFileList

#===========================================
def test():
  def generator(runTuple):
    runNo = runTuple[0]
    fileName = runTuple[1]
    aPScptProc = runScptProc()
    aPScptProc.setSrcScptName('test_1001.txt')
    dstName = './test/pi-select-' + str(runNo) + '.txt'
    aPScptProc.setDstScptName(dstName)

    aTuple= ('EventCnvSvc.digiRootInputFile =  {' + fileName + '};',\
	'EventCnvSvc.digiRootOutputFile = "' + \
	'/ihepbatch/besd12/xcao/Pion_data/' + str(runNo) + '_pion.root";')
    aPScptProc.setRepTuple(aTuple) 
    aPScptProc.do()

  map(lambda r: generator(r), getRunFileCouple())

#===========================================
from PScptProc import PScptProc
class runScptProc(PScptProc):
  def scptProc(self, iLine = ''):
    aTuple = self.getRepTuple()
    if iLine.startswith('EventCnvSvc.digiRootInputFile'):
      return aTuple[0]
    elif iLine.startswith('EventCnvSvc.digiRootOutputFile'):
      return aTuple[1]
    else:
      return iLine

#===========================================

if __name__ == '__main__':
  test()
