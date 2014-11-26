#!/usr/bin/env python
def draw():
  scale = 653./17499
  from ROOT import TFile, TH1F
  m = TFile("dplot_17499.root", "r")
  m_h01 = m.Get("h1")
  m_h02 = m.Get("h2")
  m_h03 = m.Get("h3")
  m_h04 = m.Get("h4")
  m_h05 = m.Get("h5")
  m_h06 = m.Get("h6")
  m_h07 = m.Get("h7")
  m_h01.Scale(scale)
  m_h02.Scale(scale)
  m_h03.Scale(scale)
  m_h04.Scale(scale)
  m_h05.Scale(scale)
  m_h06.Scale(scale)

  d = TFile("dplot_653.root", "r")
  d_h01  = d.Get("h1")
  d_h02  = d.Get("h2")
  d_h03  = d.Get("h3")
  d_h04  = d.Get("h4")
  d_h05  = d.Get("h5")
  d_h06  = d.Get("h6")
  d_h07  = d.Get("h7")
  
  d_h01.SetLineColor(1)
  m_h01.SetLineColor(2)
  
  d_h02.SetLineColor(1)
  m_h02.SetLineColor(2)
  
  d_h03.SetLineColor(1)
  m_h03.SetLineColor(2)

  d_h04.SetLineColor(1)
  m_h04.SetLineColor(2)

  d_h05.SetLineColor(1)
  m_h05.SetLineColor(2)

  d_h06.SetLineColor(1)
  m_h06.SetLineColor(2)

  def calChi2(mc, data):
    nBins = data.GetNbinsX()
    chi2List = [(data.GetBinContent(i)-mc.GetBinContent(i))**2/data.GetBinContent(i) for i in range(nBins) if data.GetBinContent(i)>0]
    chi2 = reduce(lambda x1, x2: x1 + x2, chi2List)
    return chi2/nBins

  from ROOT import TLegend
  leg_peta = TLegend(0.3, 0.6, 0.7, 0.8)
  leg_peta.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h01, d_h01)))
  leg_peta.AddEntry( d_h01 , "Data"          , "lp")
  leg_peta.AddEntry( m_h01 , "Mc Integration", "lp")
  
  leg_pbeta = TLegend(0.3, 0.6, 0.7, 0.8)
  leg_pbeta.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h02, d_h02)))
  leg_pbeta.AddEntry( d_h02 , "Data"          , "lp")
  leg_pbeta.AddEntry( m_h02 , "Mc Integration", "lp")
  
  leg_ppb = TLegend(0.3, 0.6, 0.7, 0.8)
  leg_ppb.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h03, d_h03)))
  leg_ppb.AddEntry( d_h03 , "Data"          , "lp")
  leg_ppb.AddEntry( m_h03 , "Mc Integration", "lp")
  
  cos_peta_at_ppb = TLegend(0.3, 0.6, 0.7, 0.8)
  cos_peta_at_ppb.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h04, d_h04)))
  cos_peta_at_ppb.AddEntry( d_h04 , "Data"          , "lp")
  cos_peta_at_ppb.AddEntry( m_h04 , "Mc Integration", "lp")
  
  cos_ppb_at_peta = TLegend(0.3, 0.6, 0.7, 0.8)
  cos_ppb_at_peta.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h05, d_h05)))
  cos_ppb_at_peta.AddEntry( d_h05 , "Data"          , "lp")
  cos_ppb_at_peta.AddEntry( m_h05 , "Mc Integration", "lp")
  
  cos_ppb_at_pbeta = TLegend(0.3, 0.6, 0.7, 0.8)
  cos_ppb_at_pbeta.SetHeader('#chi^{2} / nbin = ' + str(calChi2(m_h06, d_h06)))
  cos_ppb_at_pbeta.AddEntry( d_h06 , "Data"          , "lp")
  cos_ppb_at_pbeta.AddEntry( m_h06 , "Mc Integration", "lp")
  
  from ROOT import TPostScript, TCanvas
  ps = TPostScript("test.ps")
  c = TCanvas()
  
  d_h01.Draw("elp")
  m_h01.Draw("same")
  leg_peta.Draw()
  
  c.Update()
  ps.NewPage()
  d_h02.Draw("elp")
  m_h02.Draw("same")
  leg_pbeta.Draw()
  
  c.Update()
  ps.NewPage()
  d_h03.Draw("elp")
  m_h03.Draw("same")
  leg_ppb.Draw()
  
  c.Update()
  ps.NewPage()
  d_h04.Draw("elp")
  m_h04.Draw("same")
  cos_peta_at_ppb.Draw()
  
  c.Update()
  ps.NewPage()
  d_h05.Draw("elp")
  m_h05.Draw("same")
  cos_ppb_at_peta.Draw()
  
  c.Update()
  ps.NewPage()
  d_h06.Draw("elp")
  m_h06.Draw("same")
  cos_ppb_at_pbeta.Draw()
  
  c.Update()
  ps.NewPage()
  m_h07.Draw('colz')

  c.Update()
  ps.NewPage()
  d_h07.Draw('colz')

  c.Update()
  ps.Close()

if __name__ == '__main__':
  import sys, os
  os.chdir(sys.argv[1])
  draw()

