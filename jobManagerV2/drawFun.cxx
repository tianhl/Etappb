Double_t fun(Double_t *x, Double_t *par){
  if (x[0] > par[0]){
    Double_t arg = -1 * ( x[0] - 6700.) / par[1];
    return par[0] + par[1] * ( 1 - TMath::Exp(arg));
  }
  else 
    return x[0];
}

void drawFun(){
  Double_t x_0 = 6700., y_1 = 8000.;
  Double_t par;
  par = y_1 - x_0;
  TF1 * tf = new TF1("fun", fun, 100., 10000., 2);
  tf->SetParameters(x_0, par);
  tf->Draw();
}
