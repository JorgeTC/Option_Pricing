from pytest import approx

from src.finite_differences.FDExplicitEu import FDExplicitEu
from src.finite_differences.FDImplicitEu import FDImplicitEu
from src.stock_options.BinomialCRRLattice import BinomialCRRLattice
from src.stock_options.BinomialCRROption import BinomialCRROption
from src.stock_options.BinomialEuropeanOption import BinomialEuropeanOption
from src.stock_options.BinomialLROption import BinomialLROption
from src.stock_options.BinomialLRWithGreeks import BinomialLRWithGreeks
from src.stock_options.BinomialTreeOption import BinomialTreeOption
from src.stock_options.TrinomialLattice import TrinomialLattice
from src.stock_options.TrinomialTreeOption import TrinomialTreeOption


def test_BinomialEuropeanOption():
    eu_option = BinomialEuropeanOption(
        50, 50, 0.05, 0.5, 2, {"pu": 0.2, "pd": 0.2, "is_call": False})
    assert approx(eu_option.price()) == 4.82565175125599


def test_BinomialTreeOption():
    am_option = BinomialTreeOption(
        50, 50, 0.05, 0.5, 2, {"pu": 0.2, "pd": 0.2, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 5.113060082823486


def test_BinomialCRROption():
    eu_option = BinomialCRROption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False})
    assert approx(eu_option.price()) == 3.1051473412967003


def test_BinomialCRROption_am():
    am_option = BinomialCRROption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 3.4091814964048277


def test_BinomialLROption():
    eu_option = BinomialLROption(50, 50, 0.05, 0.5, 3, {
        "sigma": 0.3, "is_call": False})
    assert approx(eu_option.price()) == 3.5674299991832887


def test_BinomialLROption_am():
    am_option = BinomialLROption(50, 50, 0.05, 0.5, 3, {
        "sigma": 0.3, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 3.668179104133528


def test_BinomialLRWithGreeks_call():
    eu_call = BinomialLRWithGreeks(50, 50, 0.05, 0.5, 300, {
        "sigma": 0.3, "is_call": True})
    price, delta, gamma = eu_call.price()
    assert approx(price) == 4.803864657409284
    assert approx(delta) == 0.5888015221823649
    assert approx(gamma) == 0.036736782388357196


def test_BinomialLRWithGreeks_put():
    eu_put = BinomialLRWithGreeks(50, 50, 0.05, 0.5, 300, {
        "sigma": 0.3, "is_call": False})
    price, delta, gamma = eu_put.price()
    assert approx(price) == 3.569360258827997
    assert approx(delta) == -0.41119847781760727
    assert approx(gamma) == 0.03673678238835338


def test_TrinomialTreeOption_eu():
    eu_put = TrinomialTreeOption(50, 50, 0.05, 0.5, 2, {
        "sigma": 0.3, "is_call": False})
    assert approx(eu_put.price()) == 3.330905491759248


def test_TrinomialTreeOption_am():
    am_option = TrinomialTreeOption(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 3.48241453902267


def test_BinomialCRRLattice_eu():
    eu_option = BinomialCRRLattice(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False})
    assert approx(eu_option.price()) == 3.1051473412967057


def test_BinomialCRRLattice_am():
    am_option = BinomialCRRLattice(
        50, 50, 0.05, 0.5, 2, {"sigma": 0.3, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 3.409181496404833


def test_TrinomialLattice_eu():
    eu_option = TrinomialLattice(50, 50, 0.05, 0.5, 2, {
        "sigma": 0.3, "is_call": False})
    assert approx(eu_option.price()) == 3.330905491759248


def test_TrinomialLattice_am():
    am_option = TrinomialLattice(50, 50, 0.05, 0.5, 2, {
        "sigma": 0.3, "is_call": False, "is_eu": False})
    assert approx(am_option.price()) == 3.48241453902267


def test_FDExplicitEu():
    option = FDExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    assert approx(option.price()) == 4.072882278148043


def test_FDImplicitEu():
    option = FDImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    assert approx(option.price()) == 4.065801939431454
