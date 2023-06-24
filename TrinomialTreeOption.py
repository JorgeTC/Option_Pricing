#Price an option by the Boyle trinomial tree
from BinomialTreeOption import BinomialTreeOption
import math
import numpy as np
class TrinomialTreeOption(BinomialTreeOption):
    def _setup_parameters_(self):
        self.u = math.exp(self.sigma*math.sqrt(2.*self.dt))
        self.d = 1/self.u
        self.m = 1
        self.qu = ((math.exp((self.r-self.div) *self.dt/2.) - math.exp(-self.sigma * math.sqrt(self.dt/2.))) / (math.exp(self.sigma * math.sqrt(self.dt/2.)) - math.exp(-self.sigma * math.sqrt(self.dt/2.))))**2
        self.qd = ((math.exp(self.sigma * math.sqrt(self.dt/2.)) - math.exp((self.r-self.div) * self.dt/2.)) / (math.exp(self.sigma * math.sqrt(self.dt/2.)) - math.exp(-self.sigma * math.sqrt(self.dt/2.))))**2.
        self.qm = 1 - self.qu - self.qd

    def _initialize_stock_price_tree_(self):
         # Initialize a 2D tree at T=0
        self.STs = [np.array([self.S0])]
        # Simulate the possible stock prices path
        for i in range(self.N):
            prev_branches = self.STs[-1]
            st = np.concatenate((prev_branches*self.u,[prev_branches[-1]*self.m],[prev_branches[-1]*self.d]))
            self.STs.append(st) # Add nodes at each time step

    def _traverse_tree_(self, payoffs):
        for i in reversed(range(self.N)):
            # The payoffs from NOT exercising the option 
            payoffs = (payoffs[:-2] * self.qu + payoffs[1:-1] * self.qm + payoffs[2:] * self.qd) * self.df

            # The payoffs from exercising, for American options
            if not self.is_european:
                payoffs = self.__check_early_exercise__(payoffs,i)
        
        return payoffs