#! /usr/bin/python
# author: tianhl
# mail: tianhl@ihep.ac.cn
# date: 2008.12.19 
#===========================================
def reduceFileName(directoryName):    
  import os
  fileList = map(lambda f: os.path.normcase(f), os.listdir(directoryName)) #list directory
  fileList = filter(lambda f: os.path.isfile(os.path.join(directoryName, f)) and \
      os.path.splitext(f)[1].lower()[1:] == 'raw', fileList) # remove no file and no rec file
  # get (fullDirectory, file name)
  fileDetail = map(lambda f: (os.path.join(directoryName, f), os.path.splitext(f)[0].split('.')[0]), fileList) 
  return fileDetail

#===========================================
def getRunFileCouple():
  import os
  rawFileDir = '/bes/besd19/offline/raw/929/'
  fileList = reduceFileName(rawFileDir)  # get full information about file
  return fileList

#===========================================
def test():
  def generator(runTuple):
    fullName = runTuple[0]
    fileName = runTuple[1]
    aPScptProc = runScptProc()
    aPScptProc.setSrcScptName('/ihepbatch/bes/offline/jobcards/641/jobOptions_rec_data.txt')
    dstDir = './test/'
    dstName = dstDir + '/jobOptions_rec_data-' + fileName + '.txt'
    aPScptProc.setDstScptName(dstName)
     
    input   = 'RawDataInputSvc.InputFiles = {' + fullName + '};'

    output0_dir = '/besfs/offline/data/641/tmp/'
    output1_dir = '/besfs/offline/data/641/hadron/1006/'
    output2_dir = '/besfs/offline/data/641/dst/1006/'
    output3_dir = '/besfs/offline/data/641/rec/1006/'
    
    output0 = 'EventCnvSvc.digiRootOutputFile ="' + output0_dir + '/' + fileName + '.tmp"\n' 
    output1 = 'SelectHadron.digiRootOutputFile="' + output1_dir + '/' + fileName + '.hadron"\n'
    output2 = 'WriteDst.digiRootOutputFile="'     + output2_dir + '/' + fileName + '.dst"\n'
    output3 = 'WriteRec.digiRootOutputFile="'     + output3_dir + '/' + fileName + '.rec"\n'
    aTuple = (input, output0, output1, output2, output3)
    aPScptProc.setRepTuple(aTuple) 
    aPScptProc.do()

  map(lambda r: generator(r), getRunFileCouple())

#===========================================
from PScptProc import PScptProc
class runScptProc(PScptProc):
  def scptProc(self, iLine = ''):
    aTuple = self.getRepTuple()
    if iLine.startswith('RawDataInputSvc.InputFiles'):
      return aTuple[0]
    elif iLine.startswith('EventCnvSvc.digiRootOutputFile'):
      return aTuple[1]
    elif iLine.startswith('SelectHadron.digiRootOutputFile'):
      return aTuple[2]
    elif iLine.startswith('WriteDst.digiRootOutputFile'):
      return aTuple[3]
    elif iLine.startswith('WriteRec.digiRootOutputFile'):
      return aTuple[4]
    else:
      return iLine

#===========================================

if __name__ == '__main__':
  import sys
  #if len(sys.argv) < 2 :
  #  print 'arguments errer'
  #  sys.exit()

  test()
