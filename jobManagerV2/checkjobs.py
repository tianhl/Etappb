#! /usr/bin/python

# Author: Tian Haolai
# Mail: tianhl@ihep.ac.cn
# Date: 2009.03.18

def test(date):
  import os
  env_str_list = os.environ['PACKAGE_POLICY_FOR_PROJECT_GAUDIROOT']
  directory = env_str_list[0:env_str_list.find('cmt/')] + 'run/bb_rec/'
  output_directory = directory + date
  if os.path.exists(output_directory) and os.path.isdir(output_directory):
    os.chdir(output_directory)
  else: 
    print output_directory + ' does not exist!'
    import sys
    sys.exit()

  fi = open(date + '.joblog', 'r')
  jobList = fi.readlines()
  fi.close()

  errList = []
  import commands
  jobList = filter(lambda j:  os.path.isfile(j[:-1]), jobList)
  for eachJob in jobList:
    flag0 = False
    flag1 = False

    output = commands.getoutput('grep "ApplicationMgr       INFO Application Manager Finalized successfully" ' + eachJob[:-1])
    if output.find('ApplicationMgr       INFO Application Manager Finalized successfully') == -1:
      flag0 = True
        
    output = commands.getoutput('grep "ApplicationMgr       INFO Application Manager Terminated successfully" ' + eachJob[:-1])
    if output.find('ApplicationMgr       INFO Application Manager Terminated successfull') == -1:
      flag1 = True
    
    if(flag0 or flag1):
      print eachJob
      errList.append(eachJob[:-9] + '\n')

  fo = open(date + '.joberr', 'w')
  fo.writelines(errList)
  fo.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2 :
    print 'arguments error'
    sys.exit()
  
  test(sys.argv[1]) 
