import os
import astropy.io.fits as fits
import ddosa

class SpectraBins(ddosa.DataAnalysis):
    input_binsname="spectral_bins_256"

    rmfbins=True

    version="v1"
    def main(self):
        self.binrmf=os.environ['CURRENT_IC']+"/ic/ibis/rsp/isgr_ebds_mod_0001.fits"
        e=fits.open(self.binrmf)[1].data
        self.bins=zip(e['E_MIN'],e['E_MAX'])
        self.binrmfext=self.binrmf+'[1]'

    def get_binrmfext(self):
        return self.binrmfext
