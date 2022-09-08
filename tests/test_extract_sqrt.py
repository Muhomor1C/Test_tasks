from main import extract_sqrt
import pytest


@pytest.mark.parametrize('number, result', [
    (25, 5),
    (81, 9),
    ('ppppp', None),
    (53, None),
    ])
def test_func_correct(number, result):
    assert extract_sqrt(number) == result
