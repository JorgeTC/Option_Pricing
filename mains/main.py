import __init__
from src.BinomialCRRLattice import BinomialCRRLattice
from src.BinomialCRROption import BinomialCRROption
from src.BinomialEuropeanOption import BinomialEuropeanOption
from src.BinomialLROption import BinomialLROption
from src.BinomialLRWithGreeks import BinomialLRWithGreeks
from src.BinomialTreeOption import BinomialTreeOption
from src.FDExplicitEu import FDExplicitEu
from src.FDImplicitEu import FDImplicitEu
from src.TrinomialLattice import TrinomialLattice
from src.TrinomialTreeOption import TrinomialTreeOption


def main():
    eu_option = BinomialEuropeanOption(
        50, 50, 0.05, 0.5, 2, {"pu": 0.2, "pd": 0.2, "is_call": False})
    print(eu_option.price())

    am_option = BinomialTreeOption(
        50, 50, 0.05, 0.5, 2, {"pu": 0.2, "pd": 0.2, "is_call": False, "is_eu": False})
    print(am_option.price())

    eu_option = BinomialCRROption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False})
    print(eu_option.price())

    am_option = BinomialCRROption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    print(am_option.price())

    eu_option = BinomialLROption(50, 50, 0.05, 0.5, 3, {
                                 "sigma": 0.3, "is_call": False})
    print("European put: %s" % eu_option.price())

    am_option = BinomialLROption(50, 50, 0.05, 0.5, 3, {
                                 "sigma": 0.3, "is_call": False, "is_eu": False})
    print("American put: %s" % am_option.price())

    eu_call = BinomialLRWithGreeks(50, 50, 0.05, 0.5, 300, {
                                   "sigma": 0.3, "is_call": True})

    price, delta, gamma = eu_call.price()
    print(
        f"European call values\nPrice: {price }\nDelta: {delta}\nGamma: {gamma}")

    eu_put = BinomialLRWithGreeks(50, 50, 0.05, 0.5, 300, {
                                  "sigma": 0.3, "is_call": False})
    results = eu_put.price()
    print("European call values")
    print("Price: %s\nDelta: %s\nGamma: %s" % results)

    eu_put = TrinomialTreeOption(50, 50, 0.05, 0.5, 2, {
                                 "sigma": 0.3, "is_call": False})
    print("European put: %s" % eu_put.price())

    am_option = TrinomialTreeOption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    print("American put: %s" % am_option.price())

    eu_option = BinomialCRRLattice(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False})
    print("European put: %s" % eu_option.price())

    am_option = BinomialCRRLattice(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    print("American put: %s" % am_option.price())

    eu_option = TrinomialLattice(50, 50, 0.05, 0.5, 2, {
                                 "sigma": 0.3, "is_call": False})
    print("European put: %s" % eu_option.price())

    am_option = TrinomialLattice(50, 50, 0.05, 0.5, 2, {
                                 "sigma": 0.3, "is_call": False, "is_eu": False})
    print("American put: %s" % am_option.price())

    option = FDExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = FDImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())


if __name__ == '__main__':
    main()
