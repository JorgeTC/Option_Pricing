import matplotlib.pyplot as plt

import __init__
from src.stock_options.BinomialCRROption import BinomialCRROption


def main():
    constant_values = {"S0": 50, "K": 50, "r": 0.05, "T": 0.5,
                       "sigma": 0.3, "is_call": True, "is_eu": True}
    option_price_results = {}
    for i in range(2, 100):
        option_price_results[i] = BinomialCRROption(
            N=i, **constant_values).price()

    # Obtain the keys and values from the diccionary
    N_values = list(option_price_results.keys())
    option_prices = list(option_price_results.values())

    # Graph the option price as a function of N
    plt.plot(N_values, option_prices, marker='o')
    plt.xlabel('N')
    plt.ylabel('Precio de la opción')
    plt.title('Precio de opción Put americana para diferentes N')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
