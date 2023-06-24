import math


class StockOption:
    def __init__(self, S0, K, r, T, N, pu: float = 0, pd: float = 0,
                 div: float = 0, sigma: float = 0, is_call: bool = True, is_eu: bool = True):
        self.S0 = S0
        self.K = K
        self.r = r
        self.T = T
        self.N = max(1, N)  # Ensure N have at least 1 time step
        self.STs = None  # Declare the stock prices tree

 # Optional parameters used by derived classes
        self.pu = pu  # Probability of up state
        self.pd = pd  # Probability of down state
        self.div = div  # Dividend yield
        self.sigma = sigma  # Volatility
        self.is_call = is_call  # Call or put
        self.is_european = is_eu  # Eu or Am
 # Computed values
        self.dt = T/float(N)  # Single time step, in years
        self.df = math.exp(-(r-self.div) * self.dt)  # Discount factor
