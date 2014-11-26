eff()
{
    //    gROOT->Reset();
    //    gROOT->SetStyle("Plain");
    //    gStyle->SetOptFit(111);
    //    gStyle->SetOptStat(0);
    //    gStyle->SetStripDecimals(kFALSE);

    gStyle->SetCanvasColor(0);
    gStyle->SetFrameFillStyle(1001);
    gStyle->SetFrameFillColor(0);
    gStyle->SetFrameBorderMode(0);
    gStyle->SetStatColor(0);
    gStyle->SetTitleColor(1);
    gStyle->SetTitleXOffset(1.1);
    gStyle->SetTitleYOffset(1.1);
    gStyle->SetTitleTextColor(1);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadColor(0);
    gStyle->SetPadTickX(1);
    gStyle->SetPadTickY(1);
    gStyle->SetNdivisions(505,"xy");

    gStyle->SetTitleFont(72,"xy");
    gStyle->SetLabelSize(0.05,"xy");
    gStyle->SetCanvasDefH(600);
    gStyle->SetCanvasDefW(600);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadLeftMargin(0.16);
    gStyle->SetPadTopMargin(0.1);
    gStyle->SetPadBottomMargin(0.18);

    //Double_t fitf(Double_t *x,Double_t *par)
    ///// get the information of mctrue
    TFile *f1  = TFile::Open("/ihepbatch/besd13/liuhw/root/jpsi/mc_root/gkk.root");
    TTree *T1  = (TTree*)f1->Get("mctruth");
    //  
    //// get the information after final selection  
    TFile *f2  = TFile::Open("/ihepbatch/besd13/liuhw/root/jpsi/mc_root/gkk.root");
    TTree *T2  = (TTree*)f2->Get("vxyz");
    //
    //// book histogram
    //
    TH1D *h1 = new TH1D("h1"," ",80,0,4);
    TH1D *h2 = new TH1D("h2"," ",80,0,4);
    TH1D *h3 = new TH1D("h3"," ",80,0,4);
    //
    //
    TCanvas *myCanvas = new TCanvas("myCanvas","",800,800);
    myCanvas->Divide(2,2);
    myCanvas->cd(1);
    //  // here m_cos_pp is the costheta value of proton in mctrue
    T1->Draw("mkk_mc>>h1");
    myCanvas->cd(2);
    //here cos2 is the costheta value of final selection, you should set it value
    T2->Draw("mkk>>h2","chi1<40&&umiss>-0.05&&umiss<0.05&&ptgamma2<0.0004&&chi1>0");
    myCanvas->cd(3);
    h1->Sumw2();
    h2->Sumw2();
    h3->SetMarkerColor(2);
    h3->SetMarkerStyle(23);
    h3->GetXaxis()->SetTitle("M_{KK}(GeV)");
    h3->GetYaxis()->SetTitle("efficiency/50MeV");
    h3->Divide(h2,h1,1,1,"B");
    h3->Draw();
    //  myCanvas->cd(4);
    //  
    // TF1 *func = new TF1("fit",fitf,-0.8,0.8,2);
    //  func->SetParameters(0.69,800);
    //  h3->Fit("fit");
    //  h2->Fit("fit");
    //  myCanvas->SaveAs("fit11.gif");
}
