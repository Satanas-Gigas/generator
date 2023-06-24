# -*- coding: windows-1251 -*-
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_inner = -1
        self.list_outer = 0
        return self

    def __next__(self):
        self.list_inner += 1
        if self.list_inner >= len(self.list_of_list[self.list_outer]):
            self.list_outer += 1
            self.list_inner = 0
        if self.list_outer >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.list_outer][self.list_inner]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


