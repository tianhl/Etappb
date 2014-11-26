#! /usr/bin/python

#from ROOT import TTree, TFile, TH1F, TH2F, TPostScript, TCanvas
from array import array

class AnalyzeEtappb:
  def __init__(self, fileList):
    import os
    
    #if os.path.exists(dst_name) is False :
    #  print dst_name, ' does not exist'
    #  import sys
    #  sys.exit()
    #else:
    #  print 'read root file: ', dst_name

    self.registryInput(fileList)  
    self.registryHist()  
    self.cutCondition()

  def registryInput(self, fileList):  
    from ROOT import TChain
    self.__tr = TChain('analy')
    map(lambda f: self.__tr.Add(f), fileList)
    
    self.__t_run                = array('l', [0])
    self.__t_evt                = array('l', [0])
    self.__t_chi2               = array('d', [0])
    self.__t_diPho_mass_2       = array('d', [0])
    self.__t_diPro_mass_2       = array('d', [0])
    self.__t_p_eta_mass_2       = array('d', [0])
    self.__t_pb_eta_mass_2      = array('d', [0])
    self.__t_p_momentum         = array('d', [0])
    self.__t_pb_momentum        = array('d', [0])
    self.__t_gamma_ppb_mass_2   = array('d', 2*[0])
    self.__t_eta_recoiling      = array('d', [0])
    self.__t_pb_recoiling       = array('d', [0])
    self.__t_p_recoiling        = array('d', [0])
    
    self.__t_pidDedxChi2        = array('d', 2*[0])      
    self.__t_pidTof1Chi2        = array('d', 2*[0])
    self.__t_pidTof2Chi2        = array('d', 2*[0])
    self.__t_tofProbPion        = array('d', 2*[0])
    self.__t_tofProbKaon        = array('d', 2*[0])
    self.__t_tofProbProt        = array('d', 2*[0])
    self.__t_dedxProbPion       = array('d', 2*[0])
    self.__t_dedxProbKaon       = array('d', 2*[0])
    self.__t_dedxProbProt       = array('d', 2*[0])
    self.__t_bothProbPion       = array('d', 2*[0])
    self.__t_bothProbKaon       = array('d', 2*[0])
    self.__t_bothProbProt       = array('d', 2*[0])

    self.__tr.SetBranchAddress('run'                , self.__t_run               )
    self.__tr.SetBranchAddress('evt'                , self.__t_evt               )
    self.__tr.SetBranchAddress('chi2'               , self.__t_chi2              )
    self.__tr.SetBranchAddress('diPho_mass_2'       , self.__t_diPho_mass_2      )
    self.__tr.SetBranchAddress('diPro_mass_2'       , self.__t_diPro_mass_2      )
    self.__tr.SetBranchAddress('p_eta_mass_2'       , self.__t_p_eta_mass_2      )
    self.__tr.SetBranchAddress('pb_eta_mass_2'      , self.__t_pb_eta_mass_2     )
    self.__tr.SetBranchAddress('pb_momentum'        , self.__t_pb_momentum       )
    self.__tr.SetBranchAddress('p_momentum'         , self.__t_p_momentum        )
    self.__tr.SetBranchAddress('gamma_ppb_mass_2'   , self.__t_gamma_ppb_mass_2  )
    self.__tr.SetBranchAddress('eta_recoiling'      , self.__t_eta_recoiling     )
    self.__tr.SetBranchAddress('pb_recoiling'       , self.__t_pb_recoiling      )
    self.__tr.SetBranchAddress('p_recoiling'        , self.__t_p_recoiling       )

    self.__tr.SetBranchAddress('pidDedxChi2'        , self.__t_pidDedxChi2       )
    self.__tr.SetBranchAddress('pidTof1Chi2'        , self.__t_pidTof1Chi2       )
    self.__tr.SetBranchAddress('pidTof2Chi2'        , self.__t_pidTof2Chi2       )
    self.__tr.SetBranchAddress('tofProbPion'        , self.__t_tofProbPion       )
    self.__tr.SetBranchAddress('tofProbKaon'        , self.__t_tofProbKaon       )
    self.__tr.SetBranchAddress('tofProbProt'        , self.__t_tofProbProt       )
    self.__tr.SetBranchAddress('dedxProbPion'       , self.__t_dedxProbPion      )
    self.__tr.SetBranchAddress('dedxProbKaon'       , self.__t_dedxProbKaon      )
    self.__tr.SetBranchAddress('dedxProbProt'       , self.__t_dedxProbProt      )
    self.__tr.SetBranchAddress('bothProbPion'       , self.__t_bothProbPion      )
    self.__tr.SetBranchAddress('bothProbKaon'       , self.__t_bothProbKaon      )
    self.__tr.SetBranchAddress('bothProbProt'       , self.__t_bothProbProt      )


  def registryHist(self):
    from ROOT import TH1F, TH2F
    #self.__grap2D_1 = TGraph('g2_1', 'M_{p#bar{p}} vs M_{#gamma#gamma} ', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_1 = TH2F('h2_1', 'M_{p#bar{p}} vs M_{#gamma#gamma} ', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_1.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_1.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_2 = TH2F('h2_2', 'Dalitz Plot', 500, 0.01, 10, 500, 0.01, 10)
    self.__hist2D_2.GetXaxis().SetTitle('M^{2}_{p#eta} (GeV)')
    self.__hist2D_2.GetYaxis().SetTitle('M^{2}_{#bar{p}#eta} (GeV)')

    self.__hist1D_1 = TH1F('h1_1', 'M_{#gamma#gamma} ', 500, 0.05, 0.95)
    self.__hist1D_1.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_1.GetYaxis().SetTitle('Entries/')
  
    self.__hist1D_2 = TH1F('h1_2', 'M_{p#bar{p}} ', 500, 1.5, 4.0)
    self.__hist1D_2.GetXaxis().SetTitle('M_{p#bar{p}} (GeV)')
    self.__hist1D_2.GetYaxis().SetTitle('Entries/')

    self.__hist1D_3 = TH1F('h1_3', 'M_{#gamma#gamma p}  ', 100, 1.4, 2.8)
    self.__hist1D_3.GetXaxis().SetTitle('M_{#gamma#gamma p} (GeV)')
    self.__hist1D_3.GetYaxis().SetTitle('Entries/')
  
    self.__hist1D_4 = TH1F('h1_4', 'M_{#gamma#gamma #bar{p}}  ', 100, 1.4, 2.8)
    self.__hist1D_4.GetXaxis().SetTitle('M_{#gamma#gamma #bar{p}} (GeV)')
    self.__hist1D_4.GetYaxis().SetTitle('Entries/')

  def cutCondition(self):  
    from ROOT import TF1
    # for eta jpsi: cutP_0 = 3.47; cutP_1 = 0.75
    cutP_0 = 3.47
    cutP_1 = 0.75
    self.__f1 = TF1('eta_mass_top',  '[0] - [1] * x', 0.5, 0.7)
    self.__f1.SetParameters(cutP_0, cutP_1)
    self.__f1.SetLineColor(2)

    jpsi_mass = 3.097
    jpsi_offset = 0.003
    jpsi_sig = 0.00653

    jpsi_mass_mean = jpsi_mass + jpsi_offset
    jpsi_mass_3sig = 3 * jpsi_sig
    
    cutP_3 = jpsi_mass_mean - jpsi_mass_3sig
    self.__f2 = TF1('jpsi_mass_top',  '[0]', 0., 0.5)
    self.__f2.SetParameter(0, cutP_3)
    self.__f2.SetLineColor(2)
    
    eta_mass = 0.547
    eta_offset = -0.001
    eta_sig = 0.0063

    self.__eta_mass_mean = eta_mass + eta_offset
    self.__eta_mass_3sig = 3 * eta_sig 

  def cut(self):
    #return True
    
    from ROOT import TMath
    tmp = TMath.Sqrt(self.__t_diPho_mass_2[0])
    if tmp > 0.095 and tmp < 0.16:  
      return False
    if abs(TMath.Sqrt(self.__t_diPho_mass_2[0]) - self.__eta_mass_mean) < self.__eta_mass_3sig:
      return False
    if TMath.Sqrt(self.__t_diPho_mass_2[0]) < 0.5 and \
	TMath.Sqrt(self.__t_diPro_mass_2[0]) > self.__f2.Eval(TMath.Sqrt(self.__t_diPro_mass_2[0])):
      return False
    if (TMath.Sqrt(self.__t_diPho_mass_2[0]) >= 0.5 and \
	TMath.Sqrt(self.__t_diPro_mass_2[0]) > self.__f1.Eval(TMath.Sqrt(self.__t_diPho_mass_2[0]))):
      return False

    return True
    
  def loop(self):
    #from ROOT import TTree, TFile, TH1F, TH2F, TPostScript, TCanvas, TMath
    from ROOT import TMath
    print 'Entrise: ', self.__tr.GetEntries()
    cutNo = 0
    for eachEntry in xrange(self.__tr.GetEntries()):
      if eachEntry%100000 == 0:
	print eachEntry 
      self.__tr.GetEntry(eachEntry)
      
      if self.cut():
	cutNo += 1
        self.__hist2D_1.Fill(TMath.Sqrt(self.__t_diPho_mass_2[0]), TMath.Sqrt(self.__t_diPro_mass_2[0]))
        self.__hist2D_2.Fill(self.__t_pb_eta_mass_2[0], self.__t_p_eta_mass_2[0])
        self.__hist1D_1.Fill(TMath.Sqrt(self.__t_diPho_mass_2[0]))
        self.__hist1D_2.Fill(TMath.Sqrt(self.__t_diPro_mass_2[0]))
        self.__hist1D_3.Fill(TMath.Sqrt(self.__t_p_eta_mass_2[0]))
        self.__hist1D_4.Fill(TMath.Sqrt(self.__t_pb_eta_mass_2[0]))
        #print self.__t_diPho_mass_2[0]

    print 'cut No: ', cutNo	
    print 'cut rate: ', float(cutNo)/self.__tr.GetEntries()	

  def finalize(self):
    from ROOT import TPostScript, TCanvas
    ps = TPostScript('test.ps')
    canvas = TCanvas()
    canvas.SetGrid()

    ps.NewPage()
    self.__hist2D_1.Draw()
    self.__f1.Draw('same')
    self.__f2.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_2.Draw('box')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_1.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_2.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_3.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_4.Draw()

    canvas.Update()
    ps.Close()

def test(dst_name):
  import os
  os.chdir(dst_name)
  from convertEtappb import scanFiles
  fileList = scanFiles(dst_name)
  analyze = AnalyzeEtappb(fileList) 
  analyze.loop()
  analyze.finalize()
  print 'result: ', os.getcwd() + '/test.ps'

if __name__ == '__main__':
  import sys, os
  if len(sys.argv) < 2 :
    print 'arguments error'
    sys.exit()
  import time  
  time.clock()
  dir_name = os.path.join(os.path.normpath(os.path.abspath(sys.argv[1])), 'analy')
  print dir_name
  test(dir_name)
  print 'exe time: ', time.clock()

