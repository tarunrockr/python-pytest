import pytest

# ------------------ Run Command for following function | pytest first_test.py    ----------------------
# Main function
def func(x):
	return x+5


# Test function | run command : pytest first_test.py
def test_function():
	assert func(3) == 8

