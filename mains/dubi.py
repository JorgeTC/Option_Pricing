import matplotlib.pyplot as plt

import __init__
from src.stock_options.BinomialCRROption import BinomialCRROption


def request_parameter_to_graph(message, valid_values):
    while True:
        value = input(message)
        if value in valid_values:
            return value
        else:
            print("Invalid value. Try again.")


def request_parameter(message, min_value, max_value, is_integer):
    while True:
        try:
            value = input(message)
            if is_integer:
                value = int(value)
            else:
                value = float(value)

            if min_value <= value <= max_value:
                return value
            else:
                print("The value must be between {} - {}".format(min_value, max_value))
        except ValueError:
            print("Enter a valid number.")


def check_parameter(option):
    if option == "S0":
        K = request_parameter("Enter the Strike Price: ",
                              0, float('inf'), is_integer=False)
        r = request_parameter("Enter the risk-free rate: ",
                              0, float(1), is_integer=False)
        T = request_parameter("Enter the Time to Maturity: ",
                              0, float('inf'), is_integer=False)
        N = request_parameter("Enter the Number of steps: ",
                              2, float(1000), is_integer=True)
        return {"K": K, "r": r, "T": T, "N": N}
    elif option == "K":
        S0 = request_parameter("Enter the Spot Price: ",
                               0, float('inf'), is_integer=False)
        r = request_parameter("Enter the risk-free rate: ",
                              0, float(1), is_integer=False)
        T = request_parameter("Enter the Time to Maturity: ",
                              0, float('inf'), is_integer=False)
        N = request_parameter("Enter the Number of steps: ",
                              2, float(1000), is_integer=True)
        return {"S0": S0, "r": r, "T": T, "N": N}
    elif option == "r":
        S0 = request_parameter("Enter the Spot Price: ",
                               0, float('inf'), is_integer=False)
        K = request_parameter("Enter the Strike Price: ",
                              0, float('inf'), is_integer=False)
        T = request_parameter("Enter the Time to Maturity: ",
                              0, float('inf'), is_integer=False)
        N = request_parameter("Enter the Number of steps: ",
                              2, float(1000), is_integer=True)
        return {"S0": S0, "K": K, "T": T, "N": N}
    elif option == "T":
        S0 = request_parameter("Enter the Spot Price: ",
                               0, float('inf'), is_integer=False)
        K = request_parameter("Enter the Strike Price: ",
                              0, float('inf'), is_integer=False)
        r = request_parameter("Enter the risk-free rate: ",
                              0, float(1), is_integer=False)
        N = request_parameter("Enter the Number of steps: ",
                              2, float(1000), is_integer=True)
        return {"S0": S0, "K": K, "r": r, "N": N}
    elif option == "N":
        S0 = request_parameter("Enter the Spot Price: ",
                               0, float('inf'), is_integer=False)
        K = request_parameter("Enter the Strike Price: ",
                              0, float('inf'), is_integer=False)
        r = request_parameter("Enter the risk-free rate: ",
                              0, float(1), is_integer=False)
        T = request_parameter("Enter the Time to Maturity: ",
                              0, float('inf'), is_integer=False)
        return {"S0": S0, "K": K, "r": r, "T": T}
    else:
        print("Invalid option")


def main():
    # Lista de valores válidos
    valid_list = ['S0', 'K', 'r', 'T', 'N']
    param_to_graph = request_parameter_to_graph(
        "Enter a parameter of the list:", valid_list)
    constant_parameters = check_parameter(param_to_graph)
    constant_values = {**constant_parameters,
                       "sigma": 0.3, "is_call": True, "is_eu": True}
    print(constant_values)

    option_price_results = {}
    for i in range(2, 100):
        all_values = {**constant_values, **{param_to_graph: i}}
        option_price_results[i] = BinomialCRROption(**all_values).price()

    # Obtain the keys and values from the diccionary
    N_values = list(option_price_results.keys())
    option_prices = list(option_price_results.values())

    # Graph the option price as a function of N
    plt.plot(N_values, option_prices, marker='o')
    plt.xlabel('param_to_graph')
    plt.ylabel('Precio de la opción')
    plt.title('Precio de opción Put americana para diferentes param_to_graph')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
