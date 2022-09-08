from main import checking_brackets
import pytest


@pytest.mark.parametrize('string, result', [
    ('()()()()()()()()()()()()', True),
    ('((((((()))))))', True),
    ('(()())((()))', True),
    ('(((((()()())))))', True),
    ])
def test_func_correct(string, result):
    assert checking_brackets(string) == result


@pytest.mark.parametrize('string, result', [
    ('()()()()()()()()()((()()', False),
    ('((((((())))))(', False),
    ('(abcd', False),
    (25, False),
    ])
def test_func_not_correct(string, result):
    assert checking_brackets(string) == result
