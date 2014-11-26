#! /usr/bin/env python

from array import array
def calChi2(mc, data):
  nBins = data.GetNbinsX()
  chi2List = [(data.GetBinContent(i)-mc.GetBinContent(i))**2/data.GetBinContent(i)\
      for i in range(nBins) if data.GetBinContent(i)>0]
  chi2 = reduce(lambda x1, x2: x1 + x2, chi2List)
  #chi2 = 0.
  return chi2/nBins

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
    self.__t_4C_p_momentum_x       = array('d', [0])
    self.__t_4C_p_momentum_y       = array('d', [0])
    self.__t_4C_p_momentum_z       = array('d', [0])
    self.__t_4C_p_momentum_e       = array('d', [0])
    self.__t_4C_pb_momentum_x      = array('d', [0])
    self.__t_4C_pb_momentum_y      = array('d', [0])
    self.__t_4C_pb_momentum_z      = array('d', [0])
    self.__t_4C_pb_momentum_e      = array('d', [0])
    self.__t_4C_gamma_ppb_mass_2   = array('d', 2*[0])
    self.__t_5C_diPho_mass_2       = array('d', [0])
    self.__t_5C_diPro_mass_2       = array('d', [0])
    self.__t_5C_p_eta_mass_2       = array('d', [0])
    self.__t_5C_pb_eta_mass_2      = array('d', [0])
    self.__t_5C_p_momentum         = array('d', [0])
    self.__t_5C_pb_momentum        = array('d', [0])
    self.__t_5C_p_momentum_x       = array('d', [0])
    self.__t_5C_p_momentum_y       = array('d', [0])
    self.__t_5C_p_momentum_z       = array('d', [0])
    self.__t_5C_p_momentum_e       = array('d', [0])
    self.__t_5C_pb_momentum_x      = array('d', [0])
    self.__t_5C_pb_momentum_y      = array('d', [0])
    self.__t_5C_pb_momentum_z      = array('d', [0])
    self.__t_5C_pb_momentum_e      = array('d', [0])
    self.__t_5C_eta_x              = array('d', [0])
    self.__t_5C_eta_y              = array('d', [0])
    self.__t_5C_eta_z              = array('d', [0])
    self.__t_5C_eta_e              = array('d', [0])
    self.__t_5C_gamma_ppb_mass_2   = array('d', 2*[0])
    self.__t_bothProbPion          = array('d', 2*[0])
    self.__t_bothProbKaon          = array('d', 2*[0])
    self.__t_bothProbProt          = array('d', 2*[0])
    self.__t_pidDedx               = array('d', 2*[0])
    self.__t_pidBeta               = array('d', 2*[0])

    self.__tr.SetBranchAddress('4chi2'                 , self.__t_4chi2                )
    self.__tr.SetBranchAddress('5chi2'                 , self.__t_5chi2                )
    self.__tr.SetBranchAddress('run'                   , self.__t_run                  )
    self.__tr.SetBranchAddress('C4_p_momentum_x',  self.__t_4C_p_momentum_x )     
    self.__tr.SetBranchAddress('C4_p_momentum_y',  self.__t_4C_p_momentum_y )
    self.__tr.SetBranchAddress('C4_p_momentum_z',  self.__t_4C_p_momentum_z )
    self.__tr.SetBranchAddress('C4_p_momentum_e',  self.__t_4C_p_momentum_e )
    self.__tr.SetBranchAddress('C4_pb_momentum_x', self.__t_4C_pb_momentum_x)
    self.__tr.SetBranchAddress('C4_pb_momentum_y', self.__t_4C_pb_momentum_y)
    self.__tr.SetBranchAddress('C4_pb_momentum_z', self.__t_4C_pb_momentum_z)
    self.__tr.SetBranchAddress('C4_pb_momentum_e', self.__t_4C_pb_momentum_e)
    self.__tr.SetBranchAddress('C5_p_momentum_x', self.__t_5C_p_momentum_x )     
    self.__tr.SetBranchAddress('C5_p_momentum_y', self.__t_5C_p_momentum_y )
    self.__tr.SetBranchAddress('C5_p_momentum_z', self.__t_5C_p_momentum_z )
    self.__tr.SetBranchAddress('C5_p_momentum_e', self.__t_5C_p_momentum_e )
    self.__tr.SetBranchAddress('C5_pb_momentum_x', self.__t_5C_pb_momentum_x)
    self.__tr.SetBranchAddress('C5_pb_momentum_y', self.__t_5C_pb_momentum_y)
    self.__tr.SetBranchAddress('C5_pb_momentum_z', self.__t_5C_pb_momentum_z)
    self.__tr.SetBranchAddress('C5_pb_momentum_e', self.__t_5C_pb_momentum_e)
    self.__tr.SetBranchAddress('C5_eta_x', self.__t_5C_eta_x ) 
    self.__tr.SetBranchAddress('C5_eta_y', self.__t_5C_eta_y ) 
    self.__tr.SetBranchAddress('C5_eta_z', self.__t_5C_eta_z ) 
    self.__tr.SetBranchAddress('C5_eta_e', self.__t_5C_eta_e ) 
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

    self.__hist2D_1 = TH2F('h2_1', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut #pi or J/#psi', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_1.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_1.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_2 = TH2F('h2_2', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut 4C #chi^{2}', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_2.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_2.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_3 = TH2F('h2_3', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut momentum and endcup', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_3.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_3.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_4 = TH2F('h2_4', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut eta', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_4.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_4.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_5 = TH2F('h2_5', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut 5 #chi^{2} (using 4c fit v)', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_5.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_5.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_6 = TH2F('h2_6', 'M_{p#bar{p}} vs M_{#gamma#gamma} cut 5 #chi^{2} (using 5c fit v)', 500, 0.01, 1.01, 500, 1.5, 4.0)
    self.__hist2D_6.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist2D_6.GetYaxis().SetTitle('M_{p#bar{p}} (GeV)')

    self.__hist2D_7 = TH2F('h2_7', 'Dalitz Plot 5C', 50, 2, 8, 50, 2, 8)
    self.__hist2D_7.GetXaxis().SetTitle('M^{2}_{p#eta} (GeV)')
    self.__hist2D_7.GetYaxis().SetTitle('M^{2}_{#bar{p}#eta} (GeV)')

    self.__hist2D_8 = TH2F('h2_8', 'M_{#gamma #gamma} vs 4C #chi^{2}', 50, 0.2, 0.7, 200, 0, 200)
    self.__hist2D_8.GetXaxis().SetTitle('M_{#gamma #gamma}')
    self.__hist2D_8.GetYaxis().SetTitle('4C #chi^{2}')

    self.__hist1D_4cChi_0 = TH1F('h1_4cChi_0', '4C #chi^{2}  ', 201, 0, 201)
    self.__hist1D_4cChi_0.GetYaxis().SetTitle('Entries/')

    self.__hist1D_0 = TH1F('h1_0', 'M_{#gamma#gamma} 4C', 100, 0.2, 0.7)
    self.__hist1D_0.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_0.GetYaxis().SetTitle('Entries/')

    self.__hist1D_1 = TH1F('h1_1', 'M_{#gamma#gamma} after cut #pi or J/#psi', 100, 0.2, 0.7)
    self.__hist1D_1.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_1.GetYaxis().SetTitle('Entries/')

    self.__hist1D_2 = TH1F('h1_2', 'M_{#gamma#gamma} after cut 4C #chi^{2}', 100, 0.45, 0.65)
    self.__hist1D_2.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_2.GetYaxis().SetTitle('Entries/')

    self.__hist1D_3 = TH1F('h1_3', 'M_{#gamma#gamma} after cut momentum and #theta', 100, 0.45, 0.65)
    self.__hist1D_3.GetXaxis().SetTitle('M_{#gamma#gamma} (GeV)')
    self.__hist1D_3.GetYaxis().SetTitle('Entries/')

    self.__hist1D_4 = TH1F('h1_4', 'P_{p} 4C ', 100, 0.01, 1.5)
    self.__hist1D_4.GetXaxis().SetTitle('P_{p} (GeV)')
    self.__hist1D_4.GetYaxis().SetTitle('Entries/')

    self.__hist1D_5 = TH1F('h1_5', 'P_{pb}  4C', 100, 0.01, 1.5)
    self.__hist1D_5.GetXaxis().SetTitle('P_{pb} (GeV)')
    self.__hist1D_5.GetYaxis().SetTitle('Entries/')
    self.__hist1D_5.SetLineColor(2)

    self.__hist1D_6 = TH1F('h1_6', '#theta  ', 40, -1.1, 1.1)
    self.__hist1D_6.GetYaxis().SetTitle('Entries/')

    self.__hist1D_7 = TH1F('h1_7', '#theta', 40, -1.1, 1.1)
    self.__hist1D_7.GetXaxis().SetTitle('#theta')
    self.__hist1D_7.GetYaxis().SetTitle('Entries/')
    self.__hist1D_7.SetLineColor(2)

    self.__hist1D_8 = TH1F('h1_8', 'M_{#gamma#gamma p} 5C', 100, 2, 8)
    self.__hist1D_8.GetXaxis().SetTitle('M_{#gamma#gamma p} (GeV)')
    self.__hist1D_8.GetYaxis().SetTitle('Entries/')
  
    self.__hist1D_9 = TH1F('h1_9', 'M_{#gamma#gamma #bar{p}}  5C', 100, 2, 8)
    self.__hist1D_9.GetXaxis().SetTitle('M_{#gamma#gamma #bar{p}} (GeV)')
    self.__hist1D_9.GetYaxis().SetTitle('Entries/')
    self.__hist1D_9.SetLineColor(2)

    self.__hist1D_10 = TH1F('h1_10', 'M_{p#bar{p}} 5C', 100, 3, 10)
    self.__hist1D_10.GetXaxis().SetTitle('M_{#gamma#gamma p} (GeV)')
    self.__hist1D_10.GetYaxis().SetTitle('Entries/')
  
  def cutCondition(self):  
    from ROOT import TF1
    # for eta jpsi: cutP_0 = 3.47; cutP_1 = 0.75
    cutP_0 = 3.4
    cutP_1 = 0.75
    self.__f1 = TF1('eta_mass_top',  '[0] - [1] * x', 0.4, 0.7)
    self.__f1.SetParameters(cutP_0, cutP_1)
    self.__f1.SetLineColor(2)

    jpsi_mass = 3.097
    jpsi_offset = 0.003
    jpsi_sig = 0.009

    jpsi_mass_mean = jpsi_mass + jpsi_offset
    jpsi_mass_3sig = 3 * jpsi_sig
    
    cutP_3 = jpsi_mass_mean - jpsi_mass_3sig
    self.__f2 = TF1('jpsi_mass_top',  '[0]', 0., 0.6)
    self.__f2.SetParameter(0, cutP_3)
    self.__f2.SetLineColor(2)
    
    eta_mass = 0.547
    eta_offset = -0.0007
    eta_sig = 0.007016

    self.__eta_mass_mean = eta_mass + eta_offset
    self.__eta_mass_3sig = 3 * eta_sig 

  def cut_0(self):
    if self.__t_4C_diPho_mass_2[0] <= 0 or self.__t_4C_diPro_mass_2[0] <= 0:
      return False
    from ROOT import TMath, TLine
    mDiPho = TMath.Sqrt(self.__t_4C_diPho_mass_2[0])
    mDiPro = TMath.Sqrt(self.__t_4C_diPro_mass_2[0])

    pi_mass_cut = 0.2
    self.__t_line0 = TLine(pi_mass_cut, 1.5, pi_mass_cut, 4)
    self.__t_line0.SetLineColor(2)
    if mDiPho < pi_mass_cut:
      return False
    if mDiPho < 0.5 and mDiPro > self.__f2.Eval(mDiPro):
      return False
    if mDiPro > self.__f1.Eval(mDiPho):
      return False

    return True

  def cut_1(self):
    from ROOT import TLine
    cutValue0 = 20
    self.__t_line1 = TLine(cutValue0, 0, cutValue0, 100)
    self.__t_line1.SetLineColor(2)
    if self.__t_4chi2[0] < cutValue0 :
      return True
    else:
      return False

  def cut_2(self):
    from ROOT import TMath
    p_theta = self.__t_4C_p_momentum_z[0]/self.__t_4C_p_momentum[0]
    pb_theta = self.__t_4C_pb_momentum_z[0]/self.__t_4C_pb_momentum[0]

    from ROOT import TLine
    cutValue0 = 0.3
    cutValue1 = -0.8
    cutValue2 = 0.8
    self.__t_line4 = TLine(cutValue0, 0, cutValue0, 50)
    self.__t_line5 = TLine(cutValue1, 0, cutValue1, 50)
    self.__t_line6 = TLine(cutValue2, 0, cutValue2, 50)
    self.__t_line4.SetLineColor(4)    
    self.__t_line5.SetLineColor(4)   
    self.__t_line6.SetLineColor(4)  

    if self.__t_5C_p_momentum[0] > cutValue0 and self.__t_5C_pb_momentum[0] > cutValue0\
	and p_theta < cutValue2 and p_theta > cutValue1\
	and pb_theta < cutValue2 and pb_theta > cutValue1:
       return True
    else:
       return False

  def cut_3(self):
    from ROOT import TMath, TLine
    mDiPho = TMath.Sqrt(self.__t_4C_diPho_mass_2[0])

    from ROOT import TLine
    eta_low = self.__eta_mass_mean - self.__eta_mass_3sig
    eta_upp = self.__eta_mass_mean + self.__eta_mass_3sig
    self.__t_line2 = TLine(eta_low, 0, eta_low, 100)
    self.__t_line3 = TLine(eta_upp, 0, eta_upp, 100)
    self.__t_line2.SetLineColor(2)
    self.__t_line3.SetLineColor(2)

    if mDiPho > eta_low and mDiPho < eta_upp:
      return 1
    elif (((mDiPho < (eta_low - self.__eta_mass_3sig)) and  (mDiPho > (eta_low - 2*self.__eta_mass_3sig)))\
	or ((mDiPho > (eta_upp + self.__eta_mass_3sig)) and  (mDiPho < (eta_upp + 2*self.__eta_mass_3sig)))):
    #elif mDiPho < (eta_low - self.__eta_mass_3sig):
      return 2

  def cut_4(self):  
    from ROOT import TLine
    cutValue1 = 30
    self.__t_line7 = TLine(cutValue1, 0, cutValue1, 1000)
    self.__t_line7.SetLineColor(2)
    if self.__t_5chi2[0] < cutValue1 :
      return True
    else:
      return False

  def loop(self):
    from ROOT import TMath
    print 'Entrise: ', self.__tr.GetEntries()
    cutNo = 0
    self.sigline = []
    self.bkgline = []
    for eachEntry in xrange(self.__tr.GetEntries()):
      if eachEntry%500000 == 0:
	print eachEntry 
      self.__tr.GetEntry(eachEntry)
      
      self.__hist2D_0.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
      self.__hist1D_0.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]))
      if self.cut_0():   # cut pi0 and j/psi
        self.__hist2D_1.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
        self.__hist1D_1.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]))
        self.__hist1D_4cChi_0.Fill(self.__t_4chi2[0]) 
        self.__hist2D_8.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), self.__t_4chi2[0])
        if self.cut_1():  # cut 4c chi2 > 20
          self.__hist2D_2.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
          self.__hist1D_2.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]))
          self.__hist1D_4.Fill(self.__t_4C_p_momentum[0])
          self.__hist1D_5.Fill(self.__t_4C_pb_momentum[0])

	  from ROOT import TMath
	  p_theta = self.__t_4C_p_momentum_z[0]/self.__t_4C_p_momentum[0]
	  pb_theta = self.__t_4C_pb_momentum_z[0]/self.__t_4C_pb_momentum[0]
          self.__hist1D_6.Fill(p_theta)
          self.__hist1D_7.Fill(pb_theta)

	  if self.cut_2(): # cut  mometum and angle
            self.__hist2D_3.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
            self.__hist1D_3.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]))
	    if self.cut_3() == 1:  # cut eta
              self.__hist2D_4.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
	      if self.cut_4(): # cut 5c chi2 > 30
                self.__hist2D_5.Fill(TMath.Sqrt(self.__t_4C_diPho_mass_2[0]), TMath.Sqrt(self.__t_4C_diPro_mass_2[0]))
                self.__hist2D_6.Fill(TMath.Sqrt(self.__t_5C_diPho_mass_2[0]), TMath.Sqrt(self.__t_5C_diPro_mass_2[0]))
                self.__hist2D_7.Fill(self.__t_5C_pb_eta_mass_2[0], self.__t_5C_p_eta_mass_2[0])
                self.__hist1D_8.Fill(self.__t_5C_p_eta_mass_2[0])
                self.__hist1D_9.Fill(self.__t_5C_pb_eta_mass_2[0])
                self.__hist1D_10.Fill(self.__t_5C_diPro_mass_2[0])
                # write 4 momtum to file
	        pline =   str(self.__t_5C_p_momentum_x[0]  )+ ' ' + str(self.__t_5C_p_momentum_y[0] ) + \
	            ' ' + str(self.__t_5C_p_momentum_z[0]  )+ ' ' + str(self.__t_5C_p_momentum_e[0]) + '\n'
	        pbline =  str(self.__t_5C_pb_momentum_x[0] )+ ' ' + str(self.__t_5C_pb_momentum_y[0]) + \
	            ' ' + str(self.__t_5C_pb_momentum_z[0] )+ ' ' + str(self.__t_5C_pb_momentum_e[0]) + '\n'
	        etaline = str(self.__t_5C_eta_x[0]         )+ ' ' + str(self.__t_5C_eta_y[0]        ) + \
	            ' ' + str(self.__t_5C_eta_z[0]         )+ ' ' + str(self.__t_5C_eta_e[0]) + '\n'
	        self.sigline.append(pline + pbline + etaline)
	        #print 'sig: ', self.cut_3()
                #print '  diPho: ', TMath.Sqrt(self.__t_4C_diPho_mass_2[0])
	    elif self.cut_3() == 2:
              # write 4 momtum to file
	      bgpline =   str(self.__t_5C_p_momentum_x[0]  )+ ' ' + str(self.__t_5C_p_momentum_y[0] ) + \
	            ' ' + str(self.__t_5C_p_momentum_z[0]  )+ ' ' + str(self.__t_5C_p_momentum_e[0]) + '\n'
	      bgpbline =  str(self.__t_5C_pb_momentum_x[0] )+ ' ' + str(self.__t_5C_pb_momentum_y[0]) + \
	            ' ' + str(self.__t_5C_pb_momentum_z[0] )+ ' ' + str(self.__t_5C_pb_momentum_e[0]) + '\n'
	      bgetaline = str(self.__t_5C_eta_x[0]         )+ ' ' + str(self.__t_5C_eta_y[0]        ) + \
	            ' ' + str(self.__t_5C_eta_z[0]         )+ ' ' + str(self.__t_5C_eta_e[0]) + '\n'
	      self.bkgline.append(bgpline + bgpbline + bgetaline)
	      #print 'bkg: ', self.cut_3()
              #print '  diPho: ', TMath.Sqrt(self.__t_4C_diPho_mass_2[0])

    self.__hist1D_2.Fit('gaus')
    self.__hist1D_3.Fit('gaus')
    
    from ROOT import TLegend
    self.__leg_momentum = TLegend(0.15, 0.7, 0.5, 0.9)
    self.__leg_momentum.SetHeader('#chi^{2} / nbin = ' + str(calChi2(self.__hist1D_4, self.__hist1D_5)))
    self.__leg_momentum.AddEntry( self.__hist1D_4 , "P_{p}      ", "lp")
    self.__leg_momentum.AddEntry( self.__hist1D_5 , "P_{#bar{p}}", "lp")

    self.__leg_theta = TLegend(0.15, 0.8, 0.35, 0.9)
    self.__leg_theta.SetHeader('#chi^{2} / nbin = ' + str(calChi2(self.__hist1D_6, self.__hist1D_7)))
    self.__leg_theta.AddEntry( self.__hist1D_6 , "#theta_{p}      ", "lp")
    self.__leg_theta.AddEntry( self.__hist1D_7 , "#theta_{#bar{p}}", "lp")

    self.__leg_gammaGammaP = TLegend(0.3, 0.6, 0.7, 0.8)
    self.__leg_gammaGammaP.SetHeader('#chi^{2} / nbin = ' + str(calChi2(self.__hist1D_8, self.__hist1D_9)))
    self.__leg_gammaGammaP.AddEntry( self.__hist1D_8 , "#gamma #gamma p      ", "lp")
    self.__leg_gammaGammaP.AddEntry( self.__hist1D_9 , "#gamma #gamma #bar{p}", "lp")



  def finalize(self):
    fo = open('sig.dat', 'w')
    fo.writelines(self.sigline)
    fo.close()
    fo = open('bkg.dat', 'w')
    fo.writelines(self.bkgline)
    fo.close()
    from ROOT import TPostScript, TCanvas
    from ROOT import gStyle
    gStyle.SetOptFit(1111)
    ps = TPostScript('test.ps')
    canvas = TCanvas()
    canvas.SetGrid()

    ps.NewPage()
    self.__hist2D_0.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_0.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_1.Draw()
    self.__f1.Draw('same')
    self.__f2.Draw('same')
    self.__t_line0.Draw('same') 

    canvas.Update()
    ps.NewPage()
    self.__hist1D_1.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_8.Draw()
    self.__t_line2.Draw('same')
    self.__t_line3.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_4cChi_0.Draw()
    self.__t_line1.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_2.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_2.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_4.Draw()
    self.__hist1D_5.Draw('same')
    self.__t_line4.Draw('same')
    self.__leg_momentum.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_6.Draw()
    self.__hist1D_7.Draw('same')
    self.__t_line5.Draw('same')   
    self.__t_line6.Draw('same')  
    self.__leg_theta.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_3.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist1D_3.Draw()
    self.__t_line2.Draw('same')
    self.__t_line3.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_4.Draw()
    self.__f1.Draw('same')
    self.__f2.Draw('same')
    self.__t_line2.Draw('same')
    self.__t_line3.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist2D_5.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_6.Draw()

    canvas.Update()
    ps.NewPage()
    self.__hist2D_7.Draw('colz')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_8.Draw()
    self.__hist1D_9.Draw('same')
    self.__leg_gammaGammaP.Draw('same')

    canvas.Update()
    ps.NewPage()
    self.__hist1D_10.Draw()

    canvas.Update()
    ps.Close()

