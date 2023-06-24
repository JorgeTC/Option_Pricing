import matplotlib.pyplot as plt

import __init__
from src.stock_options.BinomialCRROption import BinomialCRROption


def request_parameter_to_graph(message, valid_values: list[str]):
    while True:
        value = input(message)
        if value in valid_values:
            return value
        else:
            print("Invalid value. Try again.")


def request_parameter(message, min_value, max_value, number_type):
    while True:
        value = input(message)
        try:
            value = number_type(value)
        except ValueError:
            print("Enter a valid number.")
            continue

        if min_value <= value <= max_value:
            return value
        else:
            print(f"The value must be between {min_value} - {max_value}")


def request_int(message, min_value, max_value) -> int:
    return request_parameter(message, min_value, max_value, int)


def request_float(message, min_value, max_value) -> float:
    return request_parameter(message, min_value, max_value, float)


def request_bool(message) -> bool:
    return input(message).strip().lower() == "true"


def check_parameter(option: str):
    ans = {}

    if option != "S0":
        ans['S0'] = request_float("Enter the Spot Price: ", 0.0, float('inf'))
    if option != "K":
        ans['K'] = request_float("Enter the Strike Price: ", 0.0, float('inf'))
    if option != "r":
        ans['r'] = request_float("Enter the risk-free rate: ", 0.0, 1.0)
    if option != "T":
        ans['T'] = request_float(
            "Enter the Time to Maturity: ", 0.0, float('inf'))
    if option != 'N':
        ans['N'] = request_int("Enter the Number of steps: ", 2, 1000)
    if option != 'sigma':
        ans['sigma'] = request_int(
            "Enter the Standard Deviation: ", 0.0, float('inf'))
    if option != "is_call":
        ans["is_call"] = request_bool("Is a call option? ")
    if option != "is_eu":
        ans['is_eu'] = request_bool("Is european option? ")

    return ans


def plot_series(series: dict, x_label: str, y_label: str, title: str):
    # Obtain the keys and values from the diccionary
    x_values = list(series.keys())
    y_values = list(series.values())

    # Graph the option price as a function
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()


def main():
    # Lista de valores válidos
    valid_list = ['S0', 'K', 'r', 'T', 'N']
    param_to_graph = request_parameter_to_graph(
        "Enter a parameter of the list: ", valid_list)
    constant_values = check_parameter(param_to_graph)
    print(constant_values)

    option_price_results = {}
    for i in range(2, 100):
        all_values = {**constant_values, **{param_to_graph: i}}
        option_price_results[i] = BinomialCRROption(**all_values).price()

    plot_series(option_price_results, 'Steps', 'Option price',
                f"Option price deppending on {param_to_graph}")


if __name__ == '__main__':
    main()
