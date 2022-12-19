from typing import List, Tuple
import unittest
from collections import Counter


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
    uniq_categories = Counter(categories).keys()
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_cats = dict()
    transformed_rows = []

    for cat in categories:
        bin_cat = (int(b) for b in bin_format.format(1 << len(seen_cats)))
        seen_cats.setdefault(cat, list(bin_cat))
        transformed_rows.append((cat, seen_cats[cat]))
    return transformed_rows


class TestFT(unittest.TestCase):
    def test_empty_list(self):
        arg = []
        self.assertRaises(TypeError, fit_transform, arg)

    def test_empty_set(self):
        arg = set()
        self.assertRaises(TypeError, fit_transform, arg)

    def test_empty_dict(self):
        arg = dict()
        self.assertRaises(TypeError, fit_transform, arg)

    def test_none(self):
        self.assertRaises(TypeError, fit_transform, None)

    def test_string_1(self):
        arg = 'abcbcc'
        actual = fit_transform(arg)
        expected = [('a', [0, 0, 1]),
                    ('b', [0, 1, 0]),
                    ('c', [1, 0, 0]),
                    ('b', [0, 1, 0]),
                    ('c', [1, 0, 0]),
                    ('c', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_string_2(self):
        arg = 'cacbcb'
        actual = fit_transform(arg)
        expected = [('c', [0, 0, 1]),
                    ('a', [0, 1, 0]),
                    ('c', [0, 0, 1]),
                    ('b', [1, 0, 0]),
                    ('c', [0, 0, 1]),
                    ('b', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_list_string(self):
        arg = ['cacbcb']
        actual = fit_transform(arg)
        expected = [('cacbcb', [1])]
        self.assertEqual(actual, expected)

    def test_set_string_1(self):
        arg = {'c', 'c', 'b', 'a'}
        it = arg.__iter__()
        actual = fit_transform(arg)
        expected = [(next(it), [0, 0, 1]),
                    (next(it), [0, 1, 0]),
                    (next(it), [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_set_string_2(self):
        arg = {'cacbcb', 'abcbcc'}
        it = arg.__iter__()
        actual = fit_transform(arg)
        expected = [(next(it), [0, 1]),
                    (next(it), [1, 0])]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
