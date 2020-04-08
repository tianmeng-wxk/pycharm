import pytest

class TestDemo:
    def test_sum(self, sum):
        sum= 200+400
        assert sum == 500
    def test_assert(self):
        assert False

