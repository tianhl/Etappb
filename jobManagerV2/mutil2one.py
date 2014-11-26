#! /usr/bin/python

# author: tianhl
# mail: tianhl@ihep.ac.cn
# date: 2009.3.17

#===========================================
def reduceFileName(directoryName):    
  import os
  fileList = map(lambda f: os.path.normcase(f), os.listdir(directoryName)) #list directory
  # remove no file or no raw file or no BhaBha file
  fileList = filter(lambda f: os.path.isfile(os.path.join(directoryName, f)) and \
      os.path.splitext(f)[1].lower()[1:] == 'raw'and (f.find('Bhabha_file') >= 0), fileList) 
  # get (fullDirectory, file name)
  fileDetail = map(lambda f: (os.path.join(directoryName, f), os.path.splitext(f)[0].split('.')[0]), fileList) 
  return fileDetail

#===========================================
def getRunFileCouple(date):
  import os
  rawFileDir = '/besfs/offline/data/cal/' + date
  fileList = reduceFileName(rawFileDir)  # get full information about file
  return fileList

#===========================================
def test(date):
  import os
  env_str_list = os.environ['PACKAGE_POLICY_FOR_PROJECT_GAUDIROOT']
  directory = env_str_list[0:env_str_list.find('cmt/')] + 'run/bb_rec/'
  output_directory = directory + date

  if os.path.exists('/besfs/offline/data/cal/' + date) is False:
    print '/besfs/offline/data/cal/' + date + ' does not exist'
    import sys
    sys.exit()

  if os.path.exists(output_directory) is False :
    print output_directory + ' is created now'
    os.mkdir(output_directory)

  rec_directory = '/besfs/offline/data/cal/rec/' + date

  if os.path.exists(rec_directory) is False :
    print rec_directory + ' is created now'
    os.mkdir(rec_directory)

  logList = []
  def generator(runTuple):
    fullName = runTuple[0]
    fileName = runTuple[1]
    aPScptProc = runScptProc()
    
    aPScptProc.setSrcScptName(directory + '/recBB.txt')
    aPScptProc.setDstScptName(output_directory + '/' + fileName + '.txt')
    #print output_directory + '/' + fileName + '.txt'
   
    input   = 'RawDataInputSvc.InputFiles = {"' + fullName + '"};'
    output  = 'RootCnvSvc.digiRootOutputFile = "' + rec_directory + '/' + fileName + '.rec";'

    aTuple = (input, output)
    aPScptProc.setRepTuple(aTuple) 
    aPScptProc.do()
    
    logList.append(output_directory + '/' + fileName + '.txt.bosslog\n')

    import commands
    os.chdir(output_directory)
    print commands.getoutput('dp -q ' + fileName + '.txt')

  map(lambda r: generator(r), getRunFileCouple(date))
  of = open( output_directory + '/' + date + '.joblog', 'w')
  of.writelines(logList)
  of.close()

#===========================================
from PScptProc import PScptProc
class runScptProc(PScptProc):
  def scptProc(self, iLine = ''):
    aTuple = self.getRepTuple()
    if iLine.startswith('RawDataInputSvc.InputFiles'):
      return aTuple[0]
    elif iLine.startswith('RootCnvSvc.digiRootOutputFile'):
      return aTuple[1]
    else:
      return iLine

#===========================================

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2 :
    print 'arguments error'
    sys.exit()

  test(sys.argv[1])
