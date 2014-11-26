#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5

############################################
############################################
from PScptProc import PScptProc
class runScptProc(PScptProc):
#===========================================
  def scptProc(self, iLine = ''):
    aTuple = self.getRepTuple()
    if iLine.startswith('EventCnvSvc.digiRootInputFile'):
      return aTuple[0]
    elif iLine.startswith('EventCnvSvc.digiRootOutputFile'):
      return aTuple[1]
    else:
      return iLine
    
############################################
############################################
def __test():
  import os
  dataList = ['904', '912', '929', '930', '1001', '1002', '1003', '1004',]
  for  eachdata in dataList:
    recFileDir = '/besfs/offline/data/640new/rec/' + eachdata + '/'
    fileList = os.listdir(recFileDir)

    fileDict = {}
    i = 0
    for fileName in fileList: 
      fileDetail = fileName.split('.')[0].split('_')
      temp = fileDetail[1]
      runNo = temp[-4:] 
      temp = fileDetail[3]
      fileN = temp[4:]
      fileTuple = (runNo, fileN)
      fileDict[i] = fileTuple
      i += 1
    
    reduceDict = {}
    for i in xrange(len(fileDict)):
      temp  = fileDict[i] 
      runNo = temp[0]
      fileN = temp[1]
      reduceDict[runNo] = []
    for i in xrange(len(fileDict)):
      temp  = fileDict[i] 
      runNo = temp[0]
      fileN = temp[1]
      reduceDict[runNo].append(fileN)
    for eachItem in reduceDict.keys():
      reduceDict[eachItem].sort()
    
    barrelOrEndc = ['_b', '_e']
    bhabahOrDimu = {'bhabha':'bb', 'dimu':'dimu'}
         
    for eachBE in barrelOrEndc:
      for eachBD in bhabahOrDimu:
        for eachItem in reduceDict.keys():
          aPScptProc = runScptProc()
          aPScptProc.setSrcScptName('/ihepbatch/bes/offline/6.4.0/TestRelease/TestRelease-00-00-39/run/'\
				 + bhabahOrDimu[eachBD] + '/' + eachBD + '_select' + eachBE +'.txt')

          dstDirc = '/ihepbatch/bes/offline/6.4.0/TestRelease/TestRelease-00-00-39/run/' \
				 + bhabahOrDimu[eachBD] + '/run/'
          selectFileDirc = '/besfs/offline/data/640new/' + bhabahOrDimu[eachBD] + '/'
          stringFileList = ''
          print  eachItem
          selectFileName = selectFileDirc + 'run' + eachItem + eachBD + eachBE + '.root'
          recfileNolist = reduceDict[eachItem]
          stringFileList = ''
          for eachFileN in recfileNolist:
            fileName = recFileDir + 'run_000' + eachItem + '_Any_file' + eachFileN + '_SFO-1.rec'
            stringFileName = '"' + fileName + '",'
            stringFileList += stringFileName
           
          dstName = dstDirc + eachBD + eachBE + eachItem + '.txt'
          aPScptProc.setDstScptName(dstName)
          
          inputFileName = 'EventCnvSvc.digiRootInputFile =  {' + stringFileList[:-1] + '};'
          outputFileName = 'EventCnvSvc.digiRootOutputFile = "' + selectFileName + '";'

          print inputFileName
          print outputFileName
          aTuple = (inputFileName, outputFileName)
          aPScptProc.setRepTuple(aTuple)
          aPScptProc.do()
    

if __name__ == '__main__':
  __test()
