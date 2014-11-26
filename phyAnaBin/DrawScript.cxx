Draw(){
  TFile *f1 = new TFile("McAnaly_etaJpsi_650_090810/analy/test.root");
  TFile *f2 = new TFile("McAnaly_pi0ppbar_650_090810/analy/test.root");
  TFile *f3 = new TFile("McAnaly_chicjGamma_650_090810/analy/test.root");
  TFile *f4 = new TFile("McAnaly_pipiJpsi_650_090810/analy/test.root");
  TFile *f5 = new TFile("McAnaly_ppb_650_090810/analy/test.root");
  TFile *f6 = new TFile("McAnaly_etappb_650_090810/analy/test.root");
  
  TTree *t1 = f1->Get("analy");
  TTree *t2 = f2->Get("analy");
  TTree *t3 = f3->Get("analy");
  TTree *t4 = f4->Get("analy");
  TTree *t5 = f5->Get("analy");
  TTree *t6 = f6->Get("analy");

  Int_t flag = 0; // mass 2 mass
  //Int_t flag = 1; // recoiling 2 mass
  
  if (flag == 0){ 
    TH2F *h1 = new TH2F("h1", "h1", 100, 0.1, 0.9, 100, 1.5, 4);
    TH2F *h2 = new TH2F("h2", "h2", 100, 0.1, 0.9, 100, 1.5, 4);
    TH2F *h3 = new TH2F("h3", "h3", 100, 0.1, 0.9, 100, 1.5, 4);
    TH2F *h4 = new TH2F("h4", "h4", 100, 0.1, 0.9, 100, 1.5, 4);
    TH2F *h5 = new TH2F("h5", "h5", 100, 0.1, 0.9, 100, 1.5, 4);
    TH2F *h6 = new TH2F("h6", "h6", 100, 0.1, 0.9, 100, 1.5, 4);
    
    t1->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h1");
    t2->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h2");
    t3->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h3");
    t4->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h4");
    t5->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h5");
    t6->Draw("sqrt(diPro_mass_2):sqrt(diPho_mass_2)>>h6");
  }else{
    TH2F *h1 = new TH2F("h1", "h1", 100, 0.1, 0.9, 100, 0.1, 10);
    TH2F *h2 = new TH2F("h2", "h2", 100, 0.1, 0.9, 100, 0.1, 10);
    TH2F *h3 = new TH2F("h3", "h3", 100, 0.1, 0.9, 100, 0.1, 10);
    TH2F *h4 = new TH2F("h4", "h4", 100, 0.1, 0.9, 100, 0.1, 10);
    TH2F *h5 = new TH2F("h5", "h5", 100, 0.1, 0.9, 100, 0.1, 10);
    TH2F *h6 = new TH2F("h6", "h6", 100, 0.1, 0.9, 100, 0.1, 10);
    
    t1->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h1");
    t2->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h2");
    t3->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h3");
    t4->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h4");
    t5->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h5");
    t6->Draw("pb_recoiling:sqrt(diPho_mass_2)>>h6");
  }
  
  h1->SetMarkerColor(kBlue);
  h2->SetMarkerColor(kYellow);
  h3->SetMarkerColor(kGreen);
  h4->SetMarkerColor(kMagenta);
  h5->SetMarkerColor(kBlack);
  h6->SetMarkerColor(kRed);
  
  h1->Draw();
  h2->Draw("same");
  h3->Draw("same");
  h4->Draw("same");
  h5->Draw("same");
  h6->Draw("same");
}
