#! /usr/bin/python

#from ROOT import TTree, TFile, TH1F, TH2F, TPostScript, TCanvas
from array import array

class AnalyzeEtappb:
  def __init__(self, fileList = []):
    import os
    
    self.registryInput(fileList)  
    self.registryHist()  
    self.cutCondition()

  def registryInput(self, fileList):  
    from ROOT import TChain
    self.__tr = TChain('analy')
    map(lambda f: self.__tr.Add(f), fileList)
    
    self.__t_run                   = array('l', [0])
    self.__t_4chi2                 = array('d', [0])
    self.__t_5chi2                 = array('d', [0])
    self.__t_4C_diPho_mass_2       = array('d', [0])
    self.__t_4C_diPro_mass_2       = array('d', [0])
    self.__t_4C_p_eta_mass_2       = array('d', [0])
    self.__t_4C_pb_eta_mass_2      = array('d', [0])
    self.__t_4C_p_momentum         = array('d', [0])
    self.__t_4C_pb_momentum        = array('d', [0])
    self.__t_4C_gamma_ppb_mass_2   = array('d', 2*[0])
    self.__t_5C_diPho_mass_2       = array('d', [0])
    self.__t_5C_diPro_mass_2       = array('d', [0])
    self.__t_5C_p_eta_mass_2       = array('d', [0])
    self.__t_5C_pb_eta_mass_2      = array('d', [0])
    self.__t_5C_p_momentum         = array('d', [0])
    self.__t_5C_pb_momentum        = array('d', [0])
    self.__t_5C_gamma_ppb_mass_2   = array('d', 2*[0])
    self.__t_bothProbPion          = array('d', 2*[0])
    self.__t_bothProbKaon          = array('d', 2*[0])
    self.__t_bothProbProt          = array('d', 2*[0])
    self.__t_pidDedx               = array('d', 2*[0])
    self.__t_pidBeta               = array('d', 2*[0])

    self.__tr.SetBranchAddress('4chi2'                 , self.__t_4chi2                )
    self.__tr.SetBranchAddress('5chi2'                 , self.__t_5chi2                )
    self.__tr.SetBranchAddress('run'                   , self.__t_run                  )
    self.__tr.SetBranchAddress('C4_diPho_mass_2'       , self.__t_4C_diPho_mass_2      )
    self.__tr.SetBranchAddress('C4_diPro_mass_2'       , self.__t_4C_diPro_mass_2      )
    self.__tr.SetBranchAddress('C4_p_eta_mass_2'       , self.__t_4C_p_eta_mass_2      )
    self.__tr.SetBranchAddress('C4_pb_eta_mass_2'      , self.__t_4C_pb_eta_mass_2     )
    self.__tr.SetBranchAddress('C4_pb_momentum'        , self.__t_4C_pb_momentum       )
    self.__tr.SetBranchAddress('C4_p_momentum'         , self.__t_4C_p_momentum        )
    self.__tr.SetBranchAddress('C4_gamma_ppb_mass_2'   , self.__t_4C_gamma_ppb_mass_2  )
    self.__tr.SetBranchAddress('C5_diPho_mass_2'       , self.__t_5C_diPho_mass_2      )
    self.__tr.SetBranchAddress('C5_diPro_mass_2'       , self.__t_5C_diPro_mass_2      )
    self.__tr.SetBranchAddress('C5_p_eta_mass_2'       , self.__t_5C_p_eta_mass_2      )
    self.__tr.SetBranchAddress('C5_pb_eta_mass_2'      , self.__t_5C_pb_eta_mass_2     )
    self.__tr.SetBranchAddress('C5_pb_momentum'        , self.__t_5C_pb_momentum       )
    self.__tr.SetBranchAddress('C5_p_momentum'         , self.__t_5C_p_momentum        )
    self.__tr.SetBranchAddress('C5_gamma_ppb_mass_2'   , self.__t_5C_gamma_ppb_mass_2  )
    self.__tr.SetBranchAddress('bothProbPion'          , self.__t_bothProbPion         )
    self.__tr.SetBranchAddress('bothProbKaon'          , self.__t_bothProbKaon         )
    self.__tr.SetBranchAddress('bothProbProt'          , self.__t_bothProbProt         )
    self.__tr.SetBranchAddress('pidDedx'               , self.__t_pidDedx              )
    self.__tr.SetBranchAddress('pidBeta'               , self.__t_pidBeta              )


  def registryHist(self):
    from ROOT import TH1F, TH2F
    self.__hist2D_0 = TH2F('h2_0', 'M_{p#bar{p}} vs M_{#gamma#gamma}', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_0.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_0.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_1 = TH2F('h2_1', 'M_{p#bar{p}} vs M_{#gamma#gamma} after PID', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_1.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_1.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_4 = TH2F('h2_4', 'M_{p#bar{p}} vs M_{#gamma#gamma} after 4C#chi^2 and 5C#chi^2', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_4.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_4.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_2 = TH2F('h2_2', 'M_{p#bar{p}} vs M_{#gamma#gamma} after mass cut ', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_2.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_2.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_3 = TH2F('h2_3', 'Dalitz Plot 4C', 50, 2, 8, 50, 2, 8)
    self.__hist2D_3.GetXaxis().SetTitle('M^{2}_{p#eta} (GeV)')
    self.__hist2D_3.GetYaxis().SetTitle('M^{2}_{#bar{p}#eta} (GeV)')

    self.__hist2D_5 = TH2F('h2_5', 'Dalitz Plot 5C', 50, 2, 8, 50, 2, 8)
    self.__hist2D_5.GetXaxis().SetTitle('M^{2}_{p#eta} (GeV)')
    self.__hist2D_5.GetYaxis().SetTitle('M^{2}_{#bar{p}#eta} (GeV)')

    self.__hist2D_6 = TH2F('h2_6', '4C#chi^{2} vs 5C#chi^{2}', 40, 0, 40, 40, 0, 40)
    self.__hist2D_6.GetXaxis().SetTitle('4C#chi^{2}')
    self.__hist2D_6.GetYaxis().SetTitle('5C#chi^{2}')

    self.__hist2D_7 = TH2F('h2_7', 'Dedx vs P_{p}', 40, 0, 1.6, 100, 0, 6000)
    self.__hist2D_7.GetXaxis().SetTitle('P_{p}')
    self.__hist2D_7.GetYaxis().SetTitle('Dedx')

    self.__hist2D_8 = TH2F('h2_8', 'Dedx vs P_{pb}', 40, 0, 1.6, 100, 0, 6000)
    self.__hist2D_8.GetXaxis().SetTitle('P_{pb}')
    self.__hist2D_8.GetYaxis().SetTitle('Dedx')

    self.__hist2D_9 = TH2F('h2_9', '#beta vs P_{p}', 40, 0, 1.6, 100, 0.2, 1.2)
    self.__hist2D_9.GetXaxis().SetTitle('P_{p}')
    self.__hist2D_9.GetYaxis().SetTitle('#beta')

    self.__hist2D_10 = TH2F('h2_10', '#beta vs P_{pb}', 40, 0, 1.6, 100, 0.2, 1.2)
    self.__hist2D_10.GetXaxis().SetTitle('P_{pb}')
    self.__hist2D_10.GetYaxis().SetTitle('#beta')

    self.__hist1D_0 = TH1F('h1_0', 'M_{#gamma#gamma p}  4C', 100, 1.3, 3.)
    self.__hist1D_0.GetXaxis().SetTitle('M_{#gamma#gamma p} (GeV)')
    self.__hist1D_0.GetYaxis().SetTitle('Entries/')
  
    self.__hist1D_1 = TH1F('h1_1', 'M_{#gamma#gamma #bar{p}}  4C', 100, 1.3, 3.)
    self.__hist1D_1.GetXaxis().SetTitle('M_{#gamma#gamma #bar{p}} (GeV)')
    self.__hist1D_1.GetYaxis().SetTitle('Entries/')
    self.__hist1D_1.SetLineColor(2)

    self.__hist1D_10 = TH1F('h1_10', 'M_{#gamma#gamma p}  5C', 100, 1.3, 3.)
    self.__hist1D_10.GetXaxis().SetTitle('M_{#gamma#gamma p} (GeV)')
    self.__hist1D_10.GetYaxis().SetTitle('Entries/')
  
    self.__hist1D_11 = TH1F('h1_11', 'M_{#gamma#gamma #bar{p}}  5C', 100, 1.3, 3.)
    self.__hist1D_11.GetXaxis().SetTitle('M_{#gamma#gamma #bar{p}} (GeV)')
    self.__hist1D_11.GetYaxis().SetTitle('Entries/')
    self.__hist1D_11.SetLineColor(2)

    self.__hist1D_2 = TH1F('h1_2', 'M_{p#bar{p}} 4C', 500, 1.5, 4.0)
    self.__hist1D_2.GetXaxis().SetTitle('M_{p#bar{p}} (GeV)')
    self.__hist1D_2.GetYaxis().SetTitle('Entries/')

    self.__hist1D_12 = TH1F('h1_12', 'M_{p#bar{p}} 5C', 500, 1.5, 4.0)
    self.__hist1D_12.GetXaxis().SetTitle('M_{p#bar{p}} (GeV)')
    self.__hist1D_12.GetYaxis().SetTitle('Entries/')

    self.__hist1D_3 = TH1F('h1_3', 'M_{#gamma#gamma}  4C', 100, 0.01, 1.01)
    self.__hist1D_3.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_3.GetYaxis().SetTitle('Entries/')

    self.__hist1D_4 = TH1F('h1_4', 'P_{p} 4C ', 100, 0.01, 1.5)
    self.__hist1D_4.GetXaxis().SetTitle('P_{p} (GeV)')
    self.__hist1D_4.GetYaxis().SetTitle('Entries/')

    self.__hist1D_5 = TH1F('h1_5', 'P_{pb}  4C', 100, 0.01, 1.5)
    self.__hist1D_5.GetXaxis().SetTitle('P_{pb} (GeV)')
    self.__hist1D_5.GetYaxis().SetTitle('Entries/')
    self.__hist1D_5.SetLineColor(2)

    self.__hist1D_13 = TH1F('h1_13', 'P_{p} 5C ', 100, 0.01, 1.5)
    self.__hist1D_13.GetXaxis().SetTitle('P_{p} (GeV)')
    self.__hist1D_13.GetYaxis().SetTitle('Entries/')

    self.__hist1D_14 = TH1F('h1_14', 'P_{pb}  5C', 100, 0.01, 1.5)
    self.__hist1D_14.GetXaxis().SetTitle('P_{pb} (GeV)')
    self.__hist1D_14.GetYaxis().SetTitle('Entries/')
    self.__hist1D_14.SetLineColor(2)

    self.__hist1D_6 = TH1F('h1_6', 'run map  ', 1000, 8050, 9050)
    self.__hist1D_6.GetXaxis().SetTitle('run map')
    self.__hist1D_6.GetYaxis().SetTitle('Entries/')
    self.__hist1D_6.SetLineColor(2)

    self.__hist1D_7 = TH1F('h1_7', '4C #chi^{2}  ', 201, 0, 201)
    self.__hist1D_7.GetYaxis().SetTitle('Entries/')

    self.__hist1D_8 = TH1F('h1_8', '5C #chi^{2}  ', 201, 0, 201)
    self.__hist1D_8.GetYaxis().SetTitle('Entries/')

    self.__hist1D_9 = TH1F('h1_9', 'M_{p#bar{p}} after cut 4C', 500, 1.5, 4.0)
    self.__hist1D_9.GetXaxis().SetTitle('M_{p#bar{p}} (GeV)')
    self.__hist1D_9.GetYaxis().SetTitle('Entries/')


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

  def cut_3(self):
    if self.__t_4C_diPho_mass_2[0] <= 0 or self.__t_4C_diPro_mass_2[0] <= 0:
      return False
    from ROOT import TMath, TLine
    mDiPho = TMath.Sqrt(self.__t_4C_diPho_mass_2[0])
    mDiPro = TMath.Sqrt(self.__t_4C_diPro_mass_2[0])

    eta_low = self.__eta_mass_mean - self.__eta_mass_3sig
    eta_upp = self.__eta_mass_mean + self.__eta_mass_3sig
    self.__t_line0 = TLine(eta_low, 1.5, eta_low, 4)
    self.__t_line1 = TLine(eta_upp, 1.5, eta_upp, 4)
    self.__t_line0.SetLineColor(2)
    self.__t_line1.SetLineColor(2)

    if mDiPho < eta_low or mDiPho > eta_upp:
      return False
    if mDiPho < 0.5 and mDiPro > self.__f2.Eval(mDiPro):
      return False
    if mDiPro > self.__f1.Eval(mDiPho):
      return False

    return True

  def cut_0(self):
    if self.__t_bothProbProt[0] > self.__t_bothProbPion[0] and\
        self.__t_bothProbProt[0] > self.__t_bothProbKaon[0] and\
        self.__t_bothProbProt[1] > self.__t_bothProbPion[1] and\
        self.__t_bothProbProt[1] > self.__t_bothProbKaon[1] and\
        self.__t_bothProbProt[0] > 0.01 and\
        self.__t_bothProbProt[0] > 0.01 and\
        self.__t_bothProbProt[1] > 0.01 and\
        self.__t_bothProbProt[1] > 0.01 :
      return True
    else:
      return False
    
  def cut_1(self):
    from ROOT import TLine
    cutValue0 = 20
    self.__t_line2 = TLine(cutValue0, 0, cutValue0, 1000)
    self.__t_line2.SetLineColor(2)
    if self.__t_4chi2[0] < cutValue0 :
      return True
    else:
      return False

  def cut_2(self):  
    from ROOT import TLine
    cutValue1 = 30
    self.__t_line3 = TLine(cutValue1, 0, cutValue1, 1000)
    self.__t_line3.SetLineColor(2)
    if self.__t_5chi2[0] < cutValue1 :
      return True
    else:
      return False

  def loop(self):
    #from ROOT import TTree, TFile, TH1F, TH2F, TPostScript, TCanvas, TMath
    from ROOT import TMath
    print 'Entrise: ', self.__tr.GetEntries()
    cutNo = 0
    #for eachEntry in xrange(100000):
    for eachEntry in xrange(self.__tr.GetEntries()):
      if eachEntry%500000 == 0:
	print eachEntry 
      self.__tr.GetEntry(eachEntry)
      
      self.__hist2D_0.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
      self.__hist2D_6.Fill(self.__t_4chi2[0], self.__t_5chi2[0])

      #print 'Dedx: ', self.__t_pidDedx[0]
      #print 'Beta: ', self.__t_pidBeta[0]
      #print '5Cmo: ', self.__t_5C_p_momentum[0]
      #print '4Cmo: ', self.__t_4C_p_momentum[0]
      #print ''
      #self.__hist2D_7.Fill(  self.__t_5C_p_momentum[0] , self.__t_pidDedx[0])
      #self.__hist2D_8.Fill(  self.__t_5C_pb_momentum[0], self.__t_pidDedx[1])
      #self.__hist2D_9.Fill(  self.__t_5C_p_momentum[0] , self.__t_pidBeta[0])
      #self.__hist2D_10.Fill( self.__t_5C_pb_momentum[0], self.__t_pidBeta[1])


      if self.cut_0():
        self.__hist2D_1.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
        self.__hist1D_7.Fill(self.__t_4chi2[0])
        self.__hist1D_8.Fill(self.__t_5chi2[0])
        if self.cut_1():
          self.__hist2D_4.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))

          if self.cut_2() and self.cut_3():
            self.__hist2D_2.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
            self.__hist2D_3.Fill(self.__t_4C_pb_eta_mass_2[0], self.__t_4C_p_eta_mass_2[0])
            self.__hist2D_5.Fill(self.__t_5C_pb_eta_mass_2[0], self.__t_5C_p_eta_mass_2[0])
            self.__hist1D_10.Fill(TMath.Sqrt(self.__t_5C_p_eta_mass_2[0]))
            self.__hist1D_11.Fill(TMath.Sqrt(self.__t_5C_pb_eta_mass_2[0]))
            self.__hist1D_4.Fill(self.__t_4C_p_momentum[0])
            self.__hist1D_5.Fill(self.__t_4C_pb_momentum[0])
            self.__hist1D_13.Fill(self.__t_4C_p_momentum[0])
            self.__hist1D_14.Fill(self.__t_4C_pb_momentum[0])
            self.__hist1D_9.Fill(TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
            self.__hist1D_12.Fill(TMath.Sqrt(self.__t_5C_diPro_mass_2[0]))
            self.__hist1D_6.Fill(self.__t_run[0])
            self.__hist1D_0.Fill(TMath.Sqrt(self.__t_4C_p_eta_mass_2[0]))
            self.__hist1D_1.Fill(TMath.Sqrt(self.__t_4C_pb_eta_mass_2[0]))
            self.__hist1D_2.Fill(TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
            self.__hist1D_3.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]))

            self.__hist2D_7.Fill(  self.__t_5C_p_momentum[0] , self.__t_pidDedx[0])
            self.__hist2D_8.Fill(  self.__t_5C_pb_momentum[0], self.__t_pidDedx[1])
            self.__hist2D_9.Fill(  self.__t_5C_p_momentum[0] , self.__t_pidBeta[0])
            self.__hist2D_10.Fill( self.__t_5C_pb_momentum[0], self.__t_pidBeta[1])
    print 'cut No: ', cutNo	
    print 'cut rate: ', float(cutNo)/self.__tr.GetEntries()	

  def finalize(self):
    from ROOT import TPostScript, TCanvas
    ps = TPostScript('test.ps')
    canvas = TCanvas()
    canvas.SetGrid()

    ps.NewPage()
    self.__hist2D_0.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_6.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_7.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_8.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_9.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_10.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_1.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_7.Draw()
    self.__t_line2.Draw('same') 

    canvas.Update()
    ps.NewPage()
    self.__hist1D_8.Draw()
    self.__t_line3.Draw('same') 

    canvas.Update()
    ps.NewPage()
    self.__hist2D_4.Draw('colz')
    self.__f1.Draw('same')
    self.__f2.Draw('same')
    self.__t_line0.Draw('same') 
    self.__t_line1.Draw('same') 

    canvas.Update()
    ps.NewPage()
    self.__hist1D_2.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_3.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_2.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_3.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_5.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_0.Draw()
    self.__hist1D_1.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_10.Draw()
    self.__hist1D_11.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_4.Draw()
    self.__hist1D_5.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_12.Draw()
    self.__hist1D_13.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_6.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_9.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_13.Draw()
    self.__hist1D_14.Draw('same')

    canvas.Update()
    ps.Close()

