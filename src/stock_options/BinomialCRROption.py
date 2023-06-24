# Price an option by the binomial CRR model

import math

from .BinomialTreeOption import BinomialTreeOption


class BinomialCRROption(BinomialTreeOption):
    def _setup_parameters_(self):
        # Required calculations for the model
        # Expected value in the up state
        self.u = math.exp(self.sigma * math.sqrt(self.dt))
        self.d = 1./self.u  # Expected value in the down state
        self.qu = (math.exp((self.r-self.div)*self.dt) -
                   self.d) / (self.u-self.d)
        self.qd = 1-self.qu
