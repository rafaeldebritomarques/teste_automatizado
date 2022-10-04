from re import sub
import pytest
from matematica import soma,sub,mult,div      

def test_soma():
    assert soma(3,1) == 4

def test_sub():
    assert sub(5,2) == 3

def test_mult():
    assert mult(5,3) == 15

def test_div():
    assert div(15,3) == 5
    assert div(15,0) == "Divisão por zero"

