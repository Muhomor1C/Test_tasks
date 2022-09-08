from main import get_most_character_example2
import pytest


@pytest.mark.parametrize('string, result', [
    ('vvvvvvVggvgggiaaAAAAaaaaaaiii', ('a', 12)),
    ('wklIOGwwHHwWuevakswWIIqopPPkk', ('w', 7)),
    ('pppppppppppppppppppAAAPPPnnnn', ('p', 22)),
    ('opopopopopopopopopopopopopopo', ('o', 15)),
    ])
def test_func_correct(string, result):
    assert get_most_character_example2(string) == result


@pytest.mark.parametrize('string, result', [
    (2222222222222222222222222222222, ()),
    ('wklI!OGww!HHwWuevakswWII!PPkk', ()),
    ('pppp#ppppp#pppppppp#ppAAAPPPn', ()),
    ('opopopopop123popopopopopopopo', ()),
    ])
def test_func_not_correct(string, result):
    assert get_most_character_example2(string) == result
