import sys
sys.path.append('..')
import pytest
import project2
import pandas as pd

file1 = "yummly.json"

def test_read():
    input_data = project2.read(file1)
    if input_data is not None:
        assert True
    else:
        assert False


def test_clean_data():
    input_data = project2.read(file1)
    res = project2.clean_data(input_data)
    if res is not None:
        assert True
    else:
        assert False


def test_result():
    ingredients = ['lemon zest,olives']
    N = 3 
    input_data = project2.read(file1)
    res = project2.clean_data(input_data)
    result = project2.result(ingredients,N,res)
    if result is not None:
        assert True
    else:
        assert False
