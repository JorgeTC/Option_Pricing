# Price an option by the binomial CRR lattice """
import numpy as np

from .BinomialCRROption import BinomialCRROption


class BinomialCRRLattice(BinomialCRROption):
    def _setup_parameters_(self):
        super(BinomialCRRLattice, self)._setup_parameters_()
        self.M = 2*self.N + 1

    def _initialize_stock_price_tree_(self):
        self.STs = np.zeros(self.M)
        self.STs[0] = self.S0 * self.u**self.N
        for i in range(self.M)[1:]:
            self.STs[i] = self.STs[i-1]*self.d

    def _initialize_payoffs_tree_(self):
        odd_nodes = self.STs[::2]
        return np.maximum(0, (odd_nodes - self.K) if self.is_call else (self.K - odd_nodes))

    def __check_early_exercise__(self, payoffs, node):
        self.STs = self.STs[1:-1]  # Shorten the ends of the list
        odd_STs = self.STs[::2]
        early_ex_payoffs = (
            odd_STs - self.K) if self.is_call else (self.K - odd_STs)
        payoffs = np.maximum(payoffs, early_ex_payoffs)
        return payoffs
