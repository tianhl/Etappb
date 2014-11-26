{
    gSystem->Load("libRooFit");
    using namespace RooFit;

    //RooRealVar mpi0("mpi0", "mpi0", 0.1, 0.145);
    RooRealVar jpsi_m("jpsi_m", "jpsi_m", 3.0, 3.145);
    RooRealVar mispi0Mass("mispi0Mass", "mispi0Mass", 0.0, 0.2);
    RooRealVar pi0Mass("pi0Mass", "pi0Mass", 0.05, 0.18);
    RooRealVar mispi0_theta("mispi0_theta", "mispi0_theta", -1.1, 1.1);
    RooRealVar MisDifAngle("MisDifAngle", "MisDifAngle", 0.0, 145);

    RooRealVar mean("mean", "mean of Novosibirsk", 3.097, 3.0, 3.145);
    RooRealVar sigma("sigma", "width of Novosibirsk", 0.05, 0., 1.5);
    //RooRealVar tail("tail", "tail of Novosibirsk", -0.5, -1, 0);
    //RooNovosibirsk sig("sig","signal", mpi0, mean, sigma, tail);

    RooBreitWigner  bw("bw", "bw", jpsi_m, mean, sigma);

    RooRealVar c0("c0", "coefficient #0", 1,-10000,10000);
    RooRealVar c1("c1", "coefficient #1", 1,-10000,10000);
    RooRealVar c2("c2", "coefficient #2", 1,-100,100);
    RooRealVar c3("c3", "coefficient #3", 1,-100,100);
    RooChebychev bkg("bkg", "background pdf", jpsi_m, RooArgList(c0, c1));
    RooRealVar nsig("nsig", "signal fraction", 10000,0,40000);
    RooRealVar nbkg("nbkg", "bg fraction", 10000,0,20000);

    RooExtendPdf esig("esig", "esig", bw,  nsig);
    RooExtendPdf ebkg("ebkg", "ebkg", bkg, nsig);
    RooAddPdf model("model", "model", RooArgList(bw, bkg), RooArgList(nsig, nbkg));

    //TFile* f1= new TFile("fulleta3pijpsi_4.root");
    //TTree * tree1 = f1->Get("all");
    TChain *tree1 = new TChain("all");
    tree1->Add("fulleta3pijpsi_4.root");

    RooDataSet* matchedpi0 = new RooDataSet("jpsi", "jpsi", tree1,  RooArgSet(jpsi_m, mispi0Mass, pi0Mass, mispi0_theta, MisDifAngle));
    RooDataSet* matchedpi01 = matchedpi0->reduce("mispi0Mass>0.1&&mispi0Mass<0.16&&abs(mispi0_theta)<0.93&&MisDifAngle<40&&pi0Mass>0.08&&pi0Mass<0.16");

    RooPlot* frame = jpsi_m.frame();
    matchedpi01->plotOn(frame);

    model.fitTo(*matchedpi01, Extended(kTRUE));
    model.paramOn(frame);
    model.plotOn(frame, LineStyle(kDashed));
    model.Print();

    frame->Draw();

    cout<<" #### "<<nsig.getVal()<<endl;
    cout<<" $$$$ "<<nbkg.getVal()<<endl;

}
