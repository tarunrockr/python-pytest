# Defining a test class | Run command: pytest grouping.py
class Test:

    def test_one(self):
        x =  "maverick"
        assert 'e' in x

    def test_two(self):
        x =  "basketball"
        assert hasattr(x,'abc')