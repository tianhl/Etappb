#! /usr/bin/python 

from ROOT import *
from array import array

gROOT.ProcessLine(
"struct Inf_t {\
  long run[1];\
  long pdgid[100];\
  Double_t t5CpiE[2];\
  Double_t t5CpiPx[2];\
  Double_t t5CpiPy[2];\
  Double_t t5CpiPz[2];\
  Double_t t5CgamE[2];\
  Double_t t5CgamPx[2];\
  Double_t t5CgamPy[2];\
  Double_t t5CgamPz[2];\
  Double_t t5Cchi2[1];\
  Double_t t4CpiE[2];\
  Double_t t4CpiPx[2];\
  Double_t t4CpiPy[2];\
  Double_t t4CpiPz[2];\
  Double_t t4CgamE[2];\
  Double_t t4CgamPx[2];\
  Double_t t4CgamPy[2];\
  Double_t t4CgamPz[2];\
  Double_t t4Cchi2[1];\
  Double_t bothProbPion[2];\
  Double_t bothProbKaon[2];\
  Double_t bothProbProt[2];\
  Double_t pidDedx[2];\
  Double_t pidBeta[2];\
};");

class AnalyzeEtappb:
  def __init__(self, foName = 'etappb.root'):
    self.__nEntries = 0
    self.__fileName = 'test.min'

    # for write
    self.__fo = TFile(foName, 'recreate')
    self.__tr = TTree('analy', 'analysic for etappb')
    self.__t_run                = array('l', [0])
    self.__t_pdgid              = array('l', 100*[0])
    self.__t_4chi2              = array('d', [0])
    self.__t_4C_diPho_mass_2    = array('d', [0])
    self.__t_4C_diPro_mass_2    = array('d', [0])
    self.__t_4C_p_eta_mass_2    = array('d', [0])
    self.__t_4C_pb_eta_mass_2   = array('d', [0])
    self.__t_4C_p_momentum      = array('d', [0])
    self.__t_4C_p_momentum_x    = array('d', [0])
    self.__t_4C_p_momentum_y    = array('d', [0])
    self.__t_4C_p_momentum_z    = array('d', [0])
    self.__t_4C_p_momentum_e    = array('d', [0])
    self.__t_4C_pb_momentum     = array('d', [0])
    self.__t_4C_pb_momentum_x   = array('d', [0])
    self.__t_4C_pb_momentum_y   = array('d', [0])
    self.__t_4C_pb_momentum_z   = array('d', [0])
    self.__t_4C_pb_momentum_e   = array('d', [0])
    self.__t_4C_gamma_ppb_mass_2= array('d', 2*[0])
    self.__t_5chi2              = array('d', [0])
    self.__t_5C_diPho_mass_2    = array('d', [0])
    self.__t_5C_diPro_mass_2    = array('d', [0])
    self.__t_5C_p_eta_mass_2    = array('d', [0])
    self.__t_5C_pb_eta_mass_2   = array('d', [0])
    self.__t_5C_p_momentum      = array('d', [0])
    self.__t_5C_p_momentum_x    = array('d', [0])
    self.__t_5C_p_momentum_y    = array('d', [0])
    self.__t_5C_p_momentum_z    = array('d', [0])
    self.__t_5C_p_momentum_e    = array('d', [0])
    self.__t_5C_pb_momentum     = array('d', [0])
    self.__t_5C_pb_momentum_x   = array('d', [0])
    self.__t_5C_pb_momentum_y   = array('d', [0])
    self.__t_5C_pb_momentum_z   = array('d', [0])
    self.__t_5C_pb_momentum_e   = array('d', [0])
    self.__t_5C_eta_x   = array('d', [0])
    self.__t_5C_eta_y   = array('d', [0])
    self.__t_5C_eta_z   = array('d', [0])
    self.__t_5C_eta_e   = array('d', [0])
    self.__t_5C_gamma_ppb_mass_2= array('d', 2*[0])
    self.__t_bothProbPion       = array('d', 2*[0])
    self.__t_bothProbKaon       = array('d', 2*[0])
    self.__t_bothProbProt       = array('d', 2*[0])
    self.__t_pidDedx            = array('d', 2*[0])
    self.__t_pidBeta            = array('d', 2*[0])

    # for constant varient
    psip_m = 3.68609
    self.__psipX = 0.011*psip_m
    self.__psipY = 0.0 
    self.__psipZ = 0.0 
    self.__psipE = psip_m
  
  
  def __commitInput(self):
    self.__fi = TFile(self.__fileName)
    self.__chain = self.__fi.Get('inf')
    self.__inf_t = Inf_t()
    
    self.__chain.SetBranchAddress('5CpiE'  , self.__inf_t.t5CpiE  )
    self.__chain.SetBranchAddress('5CpiPx' , self.__inf_t.t5CpiPx )
    self.__chain.SetBranchAddress('5CpiPy' , self.__inf_t.t5CpiPy )
    self.__chain.SetBranchAddress('5CpiPz' , self.__inf_t.t5CpiPz )
    self.__chain.SetBranchAddress('5CgamE' , self.__inf_t.t5CgamE )
    self.__chain.SetBranchAddress('5CgamPx', self.__inf_t.t5CgamPx)
    self.__chain.SetBranchAddress('5CgamPy', self.__inf_t.t5CgamPy)
    self.__chain.SetBranchAddress('5CgamPz', self.__inf_t.t5CgamPz)
    self.__chain.SetBranchAddress('5Cchi2' , self.__inf_t.t5Cchi2 )
    self.__chain.SetBranchAddress('4CpiE'  , self.__inf_t.t4CpiE  )
    self.__chain.SetBranchAddress('4CpiPx' , self.__inf_t.t4CpiPx )
    self.__chain.SetBranchAddress('4CpiPy' , self.__inf_t.t4CpiPy )
    self.__chain.SetBranchAddress('4CpiPz' , self.__inf_t.t4CpiPz )
    self.__chain.SetBranchAddress('4CgamE' , self.__inf_t.t4CgamE )
    self.__chain.SetBranchAddress('4CgamPx', self.__inf_t.t4CgamPx)
    self.__chain.SetBranchAddress('4CgamPy', self.__inf_t.t4CgamPy)
    self.__chain.SetBranchAddress('4CgamPz', self.__inf_t.t4CgamPz)
    self.__chain.SetBranchAddress('4Cchi2' , self.__inf_t.t4Cchi2 )
    self.__chain.SetBranchAddress('run'    , self.__inf_t.run     )
    self.__chain.SetBranchAddress('pdgid'  , self.__inf_t.pdgid   )
    #self.__chain.SetBranchAddress('evt'    , self.__inf_t.evt     )

    self.__chain.SetBranchAddress('pidDedx'  , self.__inf_t.pidDedx  )
    self.__chain.SetBranchAddress('pidBeta'  , self.__inf_t.pidBeta  )
    #self.__chain.SetBranchAddress('pidTof2Chi2'  , self.__inf_t.pidTof2Chi2  )
    #self.__chain.SetBranchAddress('tofProbPion'  , self.__inf_t.tofProbPion  )
    #self.__chain.SetBranchAddress('tofProbKaon'  , self.__inf_t.tofProbKaon  )
    #self.__chain.SetBranchAddress('tofProbProt'  , self.__inf_t.tofProbProt  )
    #self.__chain.SetBranchAddress('dedxProbPion' , self.__inf_t.dedxProbPion )
    #self.__chain.SetBranchAddress('dedxProbKaon' , self.__inf_t.dedxProbKaon )
    #self.__chain.SetBranchAddress('dedxProbProt' , self.__inf_t.dedxProbProt )
    self.__chain.SetBranchAddress('bothProbPion' , self.__inf_t.bothProbPion )
    self.__chain.SetBranchAddress('bothProbKaon' , self.__inf_t.bothProbKaon )
    self.__chain.SetBranchAddress('bothProbProt' , self.__inf_t.bothProbProt )
  
    self.__nEntries = self.__chain.GetEntries()
  
  def __commitOutput(self):
    # for write
    self.__tr.Branch('run'                   , self.__t_run                   , 'run/l'                )
    self.__tr.Branch('pdgid'                 , self.__t_pdgid                 , 'pdgid/l'              )
    self.__tr.Branch('4chi2'                 , self.__t_4chi2                 , 'chi2/D'               )
    self.__tr.Branch('5chi2'                 , self.__t_5chi2                 , 'chi2/D'               )
    self.__tr.Branch('C4_diPho_mass_2'       , self.__t_4C_diPho_mass_2       , 'C4_diPho_mass_2/D'       )
    self.__tr.Branch('C4_diPro_mass_2'       , self.__t_4C_diPro_mass_2       , 'C4_diPro_mass_2/D'       )
    self.__tr.Branch('C4_p_eta_mass_2'       , self.__t_4C_p_eta_mass_2       , 'C4_p_eta_mass_2/D'       )
    self.__tr.Branch('C4_pb_eta_mass_2'      , self.__t_4C_pb_eta_mass_2      , 'C4_pb_eta_mass_2/D'      )
    self.__tr.Branch('C4_pb_momentum'        , self.__t_4C_pb_momentum        , 'C4_pb_momentum/D'        )
    self.__tr.Branch('C4_pb_momentum_x'      , self.__t_4C_pb_momentum_x      , 'C4_pb_momentum_x/D'      )
    self.__tr.Branch('C4_pb_momentum_y'      , self.__t_4C_pb_momentum_y      , 'C4_pb_momentum_y/D'      )
    self.__tr.Branch('C4_pb_momentum_z'      , self.__t_4C_pb_momentum_z      , 'C4_pb_momentum_z/D'      )
    self.__tr.Branch('C4_pb_momentum_e'      , self.__t_4C_pb_momentum_e      , 'C4_pb_momentum_e/D'      )
    self.__tr.Branch('C4_p_momentum'         , self.__t_4C_p_momentum         , 'C4_p_momentum/D'         )
    self.__tr.Branch('C4_p_momentum_x'       , self.__t_4C_p_momentum_x       , 'C4_p_momentum_x/D'      )
    self.__tr.Branch('C4_p_momentum_y'       , self.__t_4C_p_momentum_y       , 'C4_p_momentum_y/D'      )
    self.__tr.Branch('C4_p_momentum_z'       , self.__t_4C_p_momentum_z       , 'C4_p_momentum_z/D'      )
    self.__tr.Branch('C4_p_momentum_e'       , self.__t_4C_p_momentum_e       , 'C4_p_momentum_e/D'      )
    self.__tr.Branch('C4_gamma_ppb_mass_2'   , self.__t_4C_gamma_ppb_mass_2   , 'C4_gamma_ppb_mass_2[2]/D')
    self.__tr.Branch('C5_diPho_mass_2'       , self.__t_5C_diPho_mass_2       , 'C5_diPho_mass_2/D'       )
    self.__tr.Branch('C5_diPro_mass_2'       , self.__t_5C_diPro_mass_2       , 'C5_diPro_mass_2/D'       )
    self.__tr.Branch('C5_p_eta_mass_2'       , self.__t_5C_p_eta_mass_2       , 'C5_p_eta_mass_2/D'       )
    self.__tr.Branch('C5_pb_eta_mass_2'      , self.__t_5C_pb_eta_mass_2      , 'C5_pb_eta_mass_2/D'      )
    self.__tr.Branch('C5_pb_momentum'        , self.__t_5C_pb_momentum        , 'C5_pb_momentum/D'        )
    self.__tr.Branch('C5_pb_momentum_x'      , self.__t_5C_pb_momentum_x      , 'C5_pb_momentum_x/D'      )
    self.__tr.Branch('C5_pb_momentum_y'      , self.__t_5C_pb_momentum_y      , 'C5_pb_momentum_y/D'      )
    self.__tr.Branch('C5_pb_momentum_z'      , self.__t_5C_pb_momentum_z      , 'C5_pb_momentum_z/D'      )
    self.__tr.Branch('C5_pb_momentum_e'      , self.__t_5C_pb_momentum_e      , 'C5_pb_momentum_e/D'      )
    self.__tr.Branch('C5_p_momentum'         , self.__t_5C_p_momentum         , 'C5_p_momentum/D'         )
    self.__tr.Branch('C5_p_momentum_x'      , self.__t_5C_p_momentum_x      , 'C5_p_momentum_x/D'      )
    self.__tr.Branch('C5_p_momentum_y'      , self.__t_5C_p_momentum_y      , 'C5_p_momentum_y/D'      )
    self.__tr.Branch('C5_p_momentum_z'      , self.__t_5C_p_momentum_z      , 'C5_p_momentum_z/D'      )
    self.__tr.Branch('C5_p_momentum_e'      , self.__t_5C_p_momentum_e      , 'C5_p_momentum_e/D'      )
    self.__tr.Branch('C5_eta_x'      , self.__t_5C_eta_x      , 'C5_p_eta_x/D'      )
    self.__tr.Branch('C5_eta_y'      , self.__t_5C_eta_y      , 'C5_p_eta_y/D'      )
    self.__tr.Branch('C5_eta_z'      , self.__t_5C_eta_z      , 'C5_p_eta_z/D'      )
    self.__tr.Branch('C5_eta_e'      , self.__t_5C_eta_e      , 'C5_p_eta_e/D'      )
    self.__tr.Branch('C5_gamma_ppb_mass_2'   , self.__t_5C_gamma_ppb_mass_2   , 'C5_gamma_ppb_mass_2[2]/D')
    self.__tr.Branch('bothProbPion'          , self.__t_bothProbPion          , 'bothProbPion[2]/D')
    self.__tr.Branch('bothProbKaon'          , self.__t_bothProbKaon          , 'bothProbKaon[2]/D')
    self.__tr.Branch('bothProbProt'          , self.__t_bothProbProt          , 'bothProbProt[2]/D')
    self.__tr.Branch('pidDedx'               , self.__t_pidDedx               , 'pidDedx[2]/D')
    self.__tr.Branch('pidBeta'               , self.__t_pidBeta               , 'pidBeta[2]/D')

  def initialize(self, fileName):
    self.__fileName = fileName
    print 'execut: ', fileName
    self.__commitInput()
    self.__commitOutput()
  
  def loop(self, maxEntry = -999):
    if maxEntry < 0:
      maxEntry = self.__nEntries

    print 'max entry: ', maxEntry
    for i in xrange(maxEntry):
      self.__chain.GetEntry(i)
      if i%100000==0:
	print self.__fileName, ' : ', i

      self.__t_4chi2[0]              = 9999.   
      self.__t_5chi2[0]              = 9999.   
      self.__t_4C_diPho_mass_2[0]       = 9999.
      self.__t_4C_diPro_mass_2[0]       = 9999.
      self.__t_4C_p_eta_mass_2[0]       = 9999.
      self.__t_4C_pb_eta_mass_2[0]      = 9999.
      self.__t_4C_p_momentum[0]         = 9999.
      self.__t_4C_pb_momentum[0]        = 9999.
      self.__t_4C_p_momentum_x[0]         = 9999.
      self.__t_4C_p_momentum_y[0]         = 9999.
      self.__t_4C_p_momentum_z[0]         = 9999.
      self.__t_4C_p_momentum_e[0]         = 9999.
      self.__t_4C_pb_momentum_x[0]         = 9999.
      self.__t_4C_pb_momentum_y[0]         = 9999.
      self.__t_4C_pb_momentum_z[0]         = 9999.
      self.__t_4C_pb_momentum_e[0]         = 9999.
      self.__t_4C_gamma_ppb_mass_2[0]   = 9999.
      self.__t_4C_gamma_ppb_mass_2[1]   = 9999.
      self.__t_5C_diPho_mass_2[0]       = 9999.
      self.__t_5C_diPro_mass_2[0]       = 9999.
      self.__t_5C_p_eta_mass_2[0]       = 9999.
      self.__t_5C_pb_eta_mass_2[0]      = 9999.
      self.__t_5C_p_momentum[0]         = 9999.
      self.__t_5C_p_momentum_x[0]         = 9999.
      self.__t_5C_p_momentum_y[0]         = 9999.
      self.__t_5C_p_momentum_z[0]         = 9999.
      self.__t_5C_p_momentum_e[0]         = 9999.
      self.__t_5C_pb_momentum[0]        = 9999.
      self.__t_5C_pb_momentum_x[0]         = 9999.
      self.__t_5C_pb_momentum_y[0]         = 9999.
      self.__t_5C_pb_momentum_z[0]         = 9999.
      self.__t_5C_pb_momentum_e[0]         = 9999.
      self.__t_5C_eta_x[0]         = 9999.
      self.__t_5C_eta_y[0]         = 9999.
      self.__t_5C_eta_z[0]         = 9999.
      self.__t_5C_eta_e[0]         = 9999.
      self.__t_5C_gamma_ppb_mass_2[0]   = 9999.
      self.__t_5C_gamma_ppb_mass_2[1]   = 9999.
      #self.__t_eta_recoiling[0]      = 9999.
      #self.__t_pb_recoiling[0]       = 9999.
      #self.__t_p_recoiling[0]        = 9999.

      self.__t_pidDedx[0]    = 9999.    
      self.__t_pidBeta[0]    = 9999.    
      self.__t_pidDedx[1]    = 9999.    
      self.__t_pidBeta[1]    = 9999.    
      #self.__t_pidTof2Chi2[0]    = 9999.    
      #self.__t_tofProbPion[0]    = 9999.    
      #self.__t_tofProbKaon[0]    = 9999.    
      #self.__t_tofProbProt[0]    = 9999.    
      #self.__t_dedxProbPion[0]   = 9999.
      #self.__t_dedxProbKaon[0]   = 9999.
      #self.__t_dedxProbProt[0]   = 9999.
      self.__t_bothProbPion[0]   = 9999.
      self.__t_bothProbKaon[0]   = 9999.
      self.__t_bothProbProt[0]   = 9999.

      #self.__t_pidDedxChi2[1]    = 9999.    
      #self.__t_pidTof1Chi2[1]    = 9999.    
      #self.__t_pidTof2Chi2[1]    = 9999.    
      #self.__t_tofProbPion[1]    = 9999.    
      #self.__t_tofProbKaon[1]    = 9999.    
      #self.__t_tofProbProt[1]    = 9999.    
      #self.__t_dedxProbPion[1]   = 9999.
      #self.__t_dedxProbKaon[1]   = 9999.
      #self.__t_dedxProbProt[1]   = 9999.
      self.__t_bothProbPion[1]   = 9999.
      self.__t_bothProbKaon[1]   = 9999.
      self.__t_bothProbProt[1]   = 9999.
  
      self.__excute()
      self.__tr.Fill()


      
  def __excute(self):  
    for i in xrange(100):
      self.__t_pdgid[i] = self.__inf_t.pdgid[i]
    ##########  
    self.__t_5C_eta_e[0]         = self.__inf_t.t5CgamE[0]  + self.__inf_t.t5CgamE[1]
    self.__t_5C_eta_x[0]         = self.__inf_t.t5CgamPx[0] + self.__inf_t.t5CgamPx[1]
    self.__t_5C_eta_y[0]         = self.__inf_t.t5CgamPy[0] + self.__inf_t.t5CgamPy[1]
    self.__t_5C_eta_z[0]         = self.__inf_t.t5CgamPz[0] + self.__inf_t.t5CgamPz[1]

    self.__t_4chi2[0] = self.__inf_t.t4Cchi2[0]
    self.__t_5chi2[0] = self.__inf_t.t5Cchi2[0]
    self.__t_run[0]  = self.__inf_t.run[0]
    self.__t_bothProbPion[0]   = self.__inf_t.bothProbPion[0]
    self.__t_bothProbKaon[0]   = self.__inf_t.bothProbKaon[0]
    self.__t_bothProbProt[0]   = self.__inf_t.bothProbProt[0]
    self.__t_bothProbPion[1]   = self.__inf_t.bothProbPion[1]
    self.__t_bothProbKaon[1]   = self.__inf_t.bothProbKaon[1]
    self.__t_bothProbProt[1]   = self.__inf_t.bothProbProt[1]
    self.__t_pidDedx[0]   = self.__inf_t.pidDedx[0]
    self.__t_pidBeta[0]   = self.__inf_t.pidBeta[0]
    self.__t_pidDedx[1]   = self.__inf_t.pidDedx[1]
    self.__t_pidBeta[1]   = self.__inf_t.pidBeta[1]

    ##########  
    C5_diPho_mass_2 = (self.__inf_t.t5CgamE[0]  + self.__inf_t.t5CgamE[1])  ** 2 -\
                      (self.__inf_t.t5CgamPx[0] + self.__inf_t.t5CgamPx[1]) ** 2 -\
                      (self.__inf_t.t5CgamPy[0] + self.__inf_t.t5CgamPy[1]) ** 2 -\
                      (self.__inf_t.t5CgamPz[0] + self.__inf_t.t5CgamPz[1]) ** 2
    self.__t_5C_diPho_mass_2[0] = C5_diPho_mass_2  
  
    ##########  
    C4_diPho_mass_2 = (self.__inf_t.t4CgamE[0]  + self.__inf_t.t4CgamE[1])  ** 2 -\
                      (self.__inf_t.t4CgamPx[0] + self.__inf_t.t4CgamPx[1]) ** 2 -\
                      (self.__inf_t.t4CgamPy[0] + self.__inf_t.t4CgamPy[1]) ** 2 -\
                      (self.__inf_t.t4CgamPz[0] + self.__inf_t.t4CgamPz[1]) ** 2
    self.__t_4C_diPho_mass_2[0] = C4_diPho_mass_2  
  
    ##########  
    C5_diPro_mass_2 = (self.__inf_t.t5CpiE[0]  + self.__inf_t.t5CpiE[1])  ** 2 -\
                      (self.__inf_t.t5CpiPx[0] + self.__inf_t.t5CpiPx[1]) ** 2 -\
                      (self.__inf_t.t5CpiPy[0] + self.__inf_t.t5CpiPy[1]) ** 2 -\
                      (self.__inf_t.t5CpiPz[0] + self.__inf_t.t5CpiPz[1]) ** 2
    self.__t_5C_diPro_mass_2[0] = C5_diPro_mass_2  
  
    ##########  
    C4_diPro_mass_2 = (self.__inf_t.t4CpiE[0]  + self.__inf_t.t4CpiE[1])  ** 2 -\
                      (self.__inf_t.t4CpiPx[0] + self.__inf_t.t4CpiPx[1]) ** 2 -\
                      (self.__inf_t.t4CpiPy[0] + self.__inf_t.t4CpiPy[1]) ** 2 -\
                      (self.__inf_t.t4CpiPz[0] + self.__inf_t.t4CpiPz[1]) ** 2
    self.__t_4C_diPro_mass_2[0] = C4_diPro_mass_2  
  
    ##########  
    C5_gamma_ppb_mass_2    = (self.__inf_t.t5CgamE[0]  + self.__inf_t.t5CpiE[0]  + self.__inf_t.t5CpiE[1] ) ** 2 -\
	                     (self.__inf_t.t5CgamPx[0] + self.__inf_t.t5CpiPx[0] + self.__inf_t.t5CpiPx[1]) ** 2 -\
	                     (self.__inf_t.t5CgamPy[0] + self.__inf_t.t5CpiPy[0] + self.__inf_t.t5CpiPy[1]) ** 2 -\
	                     (self.__inf_t.t5CgamPz[0] + self.__inf_t.t5CpiPz[0] + self.__inf_t.t5CpiPz[1]) ** 2
    self.__t_5C_gamma_ppb_mass_2[0] = C5_gamma_ppb_mass_2

    ##########  
    C4_gamma_ppb_mass_2    = (self.__inf_t.t4CgamE[0]  + self.__inf_t.t4CpiE[0]  + self.__inf_t.t4CpiE[1] ) ** 2 -\
	                     (self.__inf_t.t4CgamPx[0] + self.__inf_t.t4CpiPx[0] + self.__inf_t.t4CpiPx[1]) ** 2 -\
	                     (self.__inf_t.t4CgamPy[0] + self.__inf_t.t4CpiPy[0] + self.__inf_t.t4CpiPy[1]) ** 2 -\
	                     (self.__inf_t.t4CgamPz[0] + self.__inf_t.t4CpiPz[0] + self.__inf_t.t4CpiPz[1]) ** 2
    self.__t_4C_gamma_ppb_mass_2[0] = C4_gamma_ppb_mass_2

    ##########  
    C5_gamma_ppb_mass_2    = (self.__inf_t.t5CgamE[1]  + self.__inf_t.t5CpiE[0]  + self.__inf_t.t5CpiE[1] ) ** 2 -\
	                     (self.__inf_t.t5CgamPx[1] + self.__inf_t.t5CpiPx[0] + self.__inf_t.t5CpiPx[1]) ** 2 -\
	                     (self.__inf_t.t5CgamPy[1] + self.__inf_t.t5CpiPy[0] + self.__inf_t.t5CpiPy[1]) ** 2 -\
	                     (self.__inf_t.t5CgamPz[1] + self.__inf_t.t5CpiPz[0] + self.__inf_t.t5CpiPz[1]) ** 2
    self.__t_5C_gamma_ppb_mass_2[1] = C5_gamma_ppb_mass_2

    ##########  
    C4_gamma_ppb_mass_2    = (self.__inf_t.t4CgamE[1]  + self.__inf_t.t4CpiE[0]  + self.__inf_t.t4CpiE[1] ) ** 2 -\
	                     (self.__inf_t.t4CgamPx[1] + self.__inf_t.t4CpiPx[0] + self.__inf_t.t4CpiPx[1]) ** 2 -\
	                     (self.__inf_t.t4CgamPy[1] + self.__inf_t.t4CpiPy[0] + self.__inf_t.t4CpiPy[1]) ** 2 -\
	                     (self.__inf_t.t4CgamPz[1] + self.__inf_t.t4CpiPz[0] + self.__inf_t.t4CpiPz[1]) ** 2
    self.__t_4C_gamma_ppb_mass_2[1] = C4_gamma_ppb_mass_2

    ##########  
    C5_p_eta_mass_2  = (self.__inf_t.t5CgamE[0]  + self.__inf_t.t5CgamE[1]  + self.__inf_t.t5CpiE[0] ) ** 2 -\
                       (self.__inf_t.t5CgamPx[0] + self.__inf_t.t5CgamPx[1] + self.__inf_t.t5CpiPx[0]) ** 2 -\
                       (self.__inf_t.t5CgamPy[0] + self.__inf_t.t5CgamPy[1] + self.__inf_t.t5CpiPy[0]) ** 2 -\
                       (self.__inf_t.t5CgamPz[0] + self.__inf_t.t5CgamPz[1] + self.__inf_t.t5CpiPz[0]) ** 2
    self.__t_5C_p_eta_mass_2[0]  = C5_p_eta_mass_2
  
    ##########  
    C4_p_eta_mass_2  = (self.__inf_t.t4CgamE[0]  + self.__inf_t.t4CgamE[1]  + self.__inf_t.t4CpiE[0] ) ** 2 -\
                       (self.__inf_t.t4CgamPx[0] + self.__inf_t.t4CgamPx[1] + self.__inf_t.t4CpiPx[0]) ** 2 -\
                       (self.__inf_t.t4CgamPy[0] + self.__inf_t.t4CgamPy[1] + self.__inf_t.t4CpiPy[0]) ** 2 -\
                       (self.__inf_t.t4CgamPz[0] + self.__inf_t.t4CgamPz[1] + self.__inf_t.t4CpiPz[0]) ** 2
    self.__t_4C_p_eta_mass_2[0]  = C4_p_eta_mass_2
  
    ##########  
    C5_pb_eta_mass_2 = (self.__inf_t.t5CgamE[0]  + self.__inf_t.t5CgamE[1]  + self.__inf_t.t5CpiE[1] ) ** 2 -\
                       (self.__inf_t.t5CgamPx[0] + self.__inf_t.t5CgamPx[1] + self.__inf_t.t5CpiPx[1]) ** 2 -\
                       (self.__inf_t.t5CgamPy[0] + self.__inf_t.t5CgamPy[1] + self.__inf_t.t5CpiPy[1]) ** 2 -\
                       (self.__inf_t.t5CgamPz[0] + self.__inf_t.t5CgamPz[1] + self.__inf_t.t5CpiPz[1]) ** 2 
    self.__t_5C_pb_eta_mass_2[0] = C5_pb_eta_mass_2
  
    ##########  
    C4_pb_eta_mass_2 = (self.__inf_t.t4CgamE[0]  + self.__inf_t.t4CgamE[1]  + self.__inf_t.t4CpiE[1] ) ** 2 -\
                       (self.__inf_t.t4CgamPx[0] + self.__inf_t.t4CgamPx[1] + self.__inf_t.t4CpiPx[1]) ** 2 -\
                       (self.__inf_t.t4CgamPy[0] + self.__inf_t.t4CgamPy[1] + self.__inf_t.t4CpiPy[1]) ** 2 -\
                       (self.__inf_t.t4CgamPz[0] + self.__inf_t.t4CgamPz[1] + self.__inf_t.t4CpiPz[1]) ** 2 
    self.__t_4C_pb_eta_mass_2[0] = C4_pb_eta_mass_2
  
    ##########  
    C5_p_momentum = self.__inf_t.t5CpiPx[0] ** 2 +\
                    self.__inf_t.t5CpiPy[0] ** 2 +\
                    self.__inf_t.t5CpiPz[0] ** 2
    if(C5_p_momentum>0):
      C5_p_momentum = TMath.Sqrt(C5_p_momentum)
      self.__t_5C_p_momentum[0] = C5_p_momentum

    ##########  
    self.__t_5C_p_momentum_x[0]         = self.__inf_t.t5CpiPx[0]
    self.__t_5C_p_momentum_y[0]         = self.__inf_t.t5CpiPy[0]
    self.__t_5C_p_momentum_z[0]         = self.__inf_t.t5CpiPz[0]
    self.__t_5C_p_momentum_e[0]         = self.__inf_t.t5CpiE[0] 

    ##########  
    self.__t_4C_p_momentum_x[0]         = self.__inf_t.t4CpiPx[0]
    self.__t_4C_p_momentum_y[0]         = self.__inf_t.t4CpiPy[0]
    self.__t_4C_p_momentum_z[0]         = self.__inf_t.t4CpiPz[0]
    self.__t_4C_p_momentum_e[0]         = self.__inf_t.t4CpiE[0] 

    ##########  
    C4_p_momentum = self.__inf_t.t4CpiPx[0] ** 2 +\
                    self.__inf_t.t4CpiPy[0] ** 2 +\
                    self.__inf_t.t4CpiPz[0] ** 2
    if(C4_p_momentum>0):
      C4_p_momentum = TMath.Sqrt(C4_p_momentum)
      self.__t_4C_p_momentum[0] = C4_p_momentum

    ##########  
    C5_pb_momentum = self.__inf_t.t5CpiPx[1] ** 2 +\
                     self.__inf_t.t5CpiPy[1] ** 2 +\
                     self.__inf_t.t5CpiPz[1] ** 2
    if(C5_pb_momentum>0):
      C5_pb_momentum = TMath.Sqrt(C5_pb_momentum)
      self.__t_5C_pb_momentum[0] = C5_pb_momentum
     
    ##########  
    self.__t_5C_pb_momentum_x[0]         = self.__inf_t.t5CpiPx[1]
    self.__t_5C_pb_momentum_y[0]         = self.__inf_t.t5CpiPy[1]
    self.__t_5C_pb_momentum_z[0]         = self.__inf_t.t5CpiPz[1]
    self.__t_5C_pb_momentum_e[0]         = self.__inf_t.t5CpiE[1] 

    ##########  
    self.__t_4C_pb_momentum_x[0]         = self.__inf_t.t4CpiPx[1]
    self.__t_4C_pb_momentum_y[0]         = self.__inf_t.t4CpiPy[1]
    self.__t_4C_pb_momentum_z[0]         = self.__inf_t.t4CpiPz[1]
    self.__t_4C_pb_momentum_e[0]         = self.__inf_t.t4CpiE[1] 

    ##########  
    C4_pb_momentum = self.__inf_t.t4CpiPx[1] ** 2 +\
                     self.__inf_t.t4CpiPy[1] ** 2 +\
                     self.__inf_t.t4CpiPz[1] ** 2
    if(C4_pb_momentum>0):
      C4_pb_momentum = TMath.Sqrt(C4_pb_momentum)
      self.__t_4C_pb_momentum[0] = C4_pb_momentum
     
  def finalize(self):
    self.__fo.Write()
    self.__fo.Close()
    self.__chain.Delete()
