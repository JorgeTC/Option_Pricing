#ompute option price, delta and gamma by the LR tree 
from BinomialLROption import BinomialLROption
import numpy as np
import math

class BinomialLRWithGreeks(BinomialLROption):
    def __new_stock_price_tree__(self):
        self.STs = [np.array([self.S0*self.u/self.d,
        self.S0,
        self.S0*self.d/self.u])]
        for i in range(self.N):
            prev_branches = self.STs[-1]
            st = np.concatenate((prev_branches * self.u,[prev_branches[-1] * self.d]))
            self.STs.append(st)

    def price(self):
        self._setup_parameters_()
        self.__new_stock_price_tree__()
        payoffs = self.__begin_tree_traversal__()
        option_value = payoffs[math.ceil(len(payoffs)/2)-1]
        payoff_up = payoffs[0]
        payoff_down = payoffs[-1] #same as last item in the array
        S_up = self.STs[0][0]
        S_down = self.STs[0][-1]
        dS_up = S_up - self.S0
        dS_down = self.S0 - S_down
        dS = S_up - S_down
        dV = payoff_up - payoff_down
        delta = dV/dS
        gamma = ((payoff_up-option_value)/dS_up -(option_value-payoff_down)/dS_down) / ((self.S0+S_up)/2. - (self.S0+S_down)/2.)
        return option_value, delta, gamma