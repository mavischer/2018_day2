import numpy as np

from maxima import find_maxima

def test_simple_sequence_two_maxima():
    inp = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(inp)
    exp = [2, 4]
    assert exp == out

def test_simple_sequence_one_maximum():
    inp = [-i**2 for i in range(-3, 4)]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out

def test_sine_wave():
    inp = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    out = find_maxima(inp)
    exp = [16,78]
    assert exp == out

def test_max_on_both_borders():
    inp = [4, 2, 1, 3, 1, 2]
    out = find_maxima(inp)
    exp = [0,3,5]
    assert exp == out

def test_max_on_right_border():
    inp = [4, 2, 1, 3, 1, 5]
    out = find_maxima(inp)
    exp = [0,3,5]
    assert exp == out

def test_absolute_left_border():
    inp = [4, 2, 1, 3, 1]
    out = find_maxima(inp)
    exp = [0,3]
    assert exp == out

def test_plateau():
    inp = [1, 2, 2, 1]
    out = find_maxima(inp)
    exp = []
    assert exp == out

def test_plateau_before_max():
    inp = [1, 2, 2, 3, 1]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out


def test_plateau_after_max():
    inp = [1, 3, 2, 2, 1]
    out = find_maxima(inp)
    exp = [1]
    assert exp == out


def test_plateau_between_max():
    inp = [3, 2, 2, 3]
    out = find_maxima(inp)
    exp = [0,3]
    assert exp == out
