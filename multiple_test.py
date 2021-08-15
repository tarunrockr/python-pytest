import pytest

# ------------------ Run Command for following two functions | py.test -k test_func1 -v    ----------------------
# # Test function 1
# def test_func1():
#     a=15
#     b=10
#     assert a==b 

# # Test function 2
# def test_func2():
#     a=5
#     b=10
#     assert a+5 == b


# ------------------ Run Command for following two functions | py.test -m name1    ----------------------
# Test function 1
@pytest.mark.name1
def test_func1():
    a=15
    b=10
    assert a==b 

# Test function 2
@pytest.mark.name2
def test_func2():
    a=5
    b=10
    assert a+5 == b
