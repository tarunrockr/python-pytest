import pytest 
# Run command | pytest test_fixture.py
@pytest.fixture 
def numbers():
    x=10
    y=20
    z=25
    return [x,y,z]

@pytest.mark.xfail
def test_one(numbers):
    x = 5
    assert x == numbers[0]

@pytest.mark.skip
def test_two(numbers):
    y = 20
    assert y == numbers[1]

def test_three(numbers):
    z = 25
    assert z == numbers[2]