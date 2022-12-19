from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(*args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')
    if len(args) == 1 and isinstance(args[0], str):
        categories = args[0]
    else:
        categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_cats = dict()
    transformed_rows = []

    for cat in categories:
        bin_cat = (int(b) for b in bin_format.format(1 << len(seen_cats)))
        seen_cats.setdefault(cat, list(bin_cat))
        transformed_rows.append((cat, seen_cats[cat]))
    return transformed_rows


def test_empty_list():
    arg = []
    with pytest.raises(TypeError):
        fit_transform(arg)


def test_empty_set():
    arg = set()
    with pytest.raises(TypeError):
        fit_transform(arg)


def test_empty_dict():
    arg = dict()
    with pytest.raises(TypeError):
        fit_transform(arg)


def test_none():
    with pytest.raises(TypeError):
        fit_transform(None)


def test_string_1():
    arg = 'abcbcc'
    actual = fit_transform(arg)
    expected = [('a', [0, 0, 1]),
                ('b', [0, 1, 0]),
                ('c', [1, 0, 0]),
                ('b', [0, 1, 0]),
                ('c', [1, 0, 0]),
                ('c', [1, 0, 0])]
    assert actual == expected


def test_string_2():
    arg = 'cacbcb'
    actual = fit_transform(arg)
    expected = [('c', [0, 0, 1]),
                ('a', [0, 1, 0]),
                ('c', [0, 0, 1]),
                ('b', [1, 0, 0]),
                ('c', [0, 0, 1]),
                ('b', [1, 0, 0])]
    assert actual == expected


def test_list_string():
    arg = ['cacbcb']
    actual = fit_transform(arg)
    expected = [('cacbcb', [1])]
    assert actual == expected


def test_set_string_1():
    arg = {'c', 'c', 'b', 'a'}
    it = arg.__iter__()
    actual = fit_transform(arg)
    expected = [(next(it), [0, 0, 1]),
                (next(it), [0, 1, 0]),
                (next(it), [1, 0, 0])]
    assert actual == expected


def test_set_string_2():
    arg = {'cacbcb', 'abcbcc'}
    it = arg.__iter__()
    actual = fit_transform(arg)
    expected = [(next(it), [0, 1]),
                (next(it), [1, 0])]
    assert actual == expected


if __name__ == '__main__':
    pass
