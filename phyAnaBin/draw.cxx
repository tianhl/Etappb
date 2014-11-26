void draw(){
  TFile * f = new TFile("test.root");
  //Draw eta invariant mass 
  analy->Draw("sqrt(diPho_mass_2)", "sqrt(diPho_mass_2)<0.6&&sqrt(diPho_mass_2)>0.5");
  
  //Draw J/psi invariant mass 
  analy->Draw("sqrt(diPro_mass_2)", "sqrt(diPro_mass_2)<3.2&&sqrt(diPro_mass_2)>3.0");
  
  //Draw 4C chi2
  analy->Draw("chi2", "chi2>0&&chi2<1000");
  
  //Draw eta invariant mass exclusive J/psi
  analy->Draw("sqrt(diPho_mass_2)", "sqrt(diPho_mass_2)<0.6&&sqrt(diPho_mass_2)>0.5&&sqrt(diPro_mass_2)<3.0");
  
  //Draw eta invariant mass exclusive J/psi and 4C_chi2 less than 20
  analy->Draw("sqrt(diPho_mass_2)", "sqrt(diPho_mass_2)<0.6&&sqrt(diPho_mass_2)>0.5&&sqrt(diPro_mass_2)<3.0&&chi2>0&&chi2<20");
  analy->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)", "sqrt(diPho_mass_2)<0.6&&sqrt(diPho_mass_2)>0.5&&sqrt(diPro_mass_2)<3.0&&chi2>0&&chi2<20");
  
  //Draw Dalize p_eta_mass_2:pb_eta_mass_2
  analy->Draw("p_eta_mass_2:pb_eta_mass_2", "p_eta_mass_2>0&&pb_eta_mass_2>0");
  
  //Draw Dalize p_eta_mass_2:diPro_mass_2
  analy->Draw("p_eta_mass_2:diPro_mass_2", "p_eta_mass_2>0&&diPro_mass_2>0");
  
  //Draw Dalize pb_eta_mass_2:diPro_mass_2
  analy->Draw("pb_eta_mass_2:diPro_mass_2", "pb_eta_mass_2>0&&diPro_mass_2>0");
  
  //Draw Dalize p_eta_mass_2:pb_eta_mass_2 exclusive J/psi
  analy->Draw("p_eta_mass_2:pb_eta_mass_2", "p_eta_mass_2>0&&pb_eta_mass_2>0&&sqrt(diPro_mass_2)<3.0");
  
  //Draw Dalize p_eta_mass_2:diPro_mass_2 exclusive J/psi
  analy->Draw("p_eta_mass_2:diPro_mass_2", "p_eta_mass_2>0&&diPro_mass_2>0&&sqrt(diPro_mass_2)<3.0");
  
  //Draw Dalize pb_eta_mass_2:diPro_mass_2 exclusive J/psi 
  analy->Draw("pb_eta_mass_2:diPro_mass_2", "pb_eta_mass_2>0&&diPro_mass_2>0&&sqrt(diPro_mass_2)<3.0");
  
  //Draw Dalize p_eta_mass_2:pb_eta_mass_2 exclusive J/psi and 4C_chi2 less than 20
  analy->Draw("p_eta_mass_2:pb_eta_mass_2", "p_eta_mass_2>0&&pb_eta_mass_2>0&&sqrt(diPro_mass_2)<3.0&&chi2>0&&chi2<20");
  
  //Draw Dalize p_eta_mass_2:diPro_mass_2 exclusive J/psi and 4C_chi2 less than 20
  analy->Draw("p_eta_mass_2:diPro_mass_2", "p_eta_mass_2>0&&diPro_mass_2>0&&sqrt(diPro_mass_2)<3.0&&chi2>0&&chi2<20");
  
  //Draw Dalize pb_eta_mass_2:diPro_mass_2 exclusive J/psi and 4C_chi2 less than 20  
  analy->Draw("pb_eta_mass_2:diPro_mass_2", "pb_eta_mass_2>0&&diPro_mass_2>0&&sqrt(diPro_mass_2)<3.0&&chi2>0&&chi2<20");
  analy->Draw("eta_recoiling:diPho_mass_2", "eta_recoiling>0&&eta_recoiling<10&&sqrt(diPho_mass_2)<1")
  analy->Draw("eta_recoiling", "eta_recoiling>0&&eta_recoiling<10")
}
  
