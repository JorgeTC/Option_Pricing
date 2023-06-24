#Price an option by the binomial CRR model

from BinomialTreeOption import BinomialTreeOption
import math

class BinomialCRROption(BinomialTreeOption):
    def _setup_parameters_(self):
        #Required calculations for the model
        self.u = math.exp(self.sigma * math.sqrt(self.dt)) # Expected value in the up state
        self.d = 1./self.u # Expected value in the down state
        self.qu = (math.exp((self.r-self.div)*self.dt) -self.d) / (self.u-self.d)
        self.qd = 1-self.qu