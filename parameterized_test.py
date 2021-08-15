import pytest
# ------------------ Run Command for following function | pytest parameterized_test.py    ----------------------
@pytest.mark.parametrize('x,y,z',[(10,20,200),(20,40,200)])
def test_function(x,y,z):
    assert x*y == z