import pytest
from main import *


def test_counter(param_test_counter):
    (input, expected_output) = param_test_counter
    try:
        result = counter(input)
    except Exception as e:
        result = str(e)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output


def test_distance(param_test_distance):
    (input, expected_output) = param_test_distance
    try:
        result = distance_counter(input)
    except Exception as e:
        result = str(e)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output


def test_size(param_test_size):
    (input, expected_output) = param_test_size
    try:
        result = size_counter(input)
    except Exception as e:
        result = str(e)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output


def test_careful(param_test_careful):
    (input, expected_output) = param_test_careful
    try:
        result = careful_counter(input[0], input[1])
    except Exception as e:
        result = str(e)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output


def test_koef(param_test_koef):
    (input, expected_output) = param_test_koef
    try:
        result = koef_counter(input)
    except Exception as e:
        result = str(e)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
