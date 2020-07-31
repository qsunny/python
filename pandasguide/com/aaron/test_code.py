import sys


def test(x):
    if x > 0:
        print("a")
    else:
        print("b")


def distinct_list():
    l = [1, 2, 2, 3, 3, 3]
    print({}.fromkeys(l).keys())
    lt = list(set(l))
    print(lt)


def vars_test():
    ff = vars() is locals()
    print(ff)
    ff = vars(sys) is sys.__dict__
    print(vars())
    print(locals())
    print(ff)

def unicode_test():
    s = '美的'
    print(s)


class Data(object):
    def __init__(self, *args):
        self._data = list(args)
        self._index = 0

    def __iter__(self):
        return self

    # 兼容python3
    def __next__(self):
        return self.next()

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d


def iterator_test():
    d = Data(1, 2, 3)
    for x in d:
        print(x)


class Data1(object):
    """生成器"""
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        for x in self._data:
            yield x


def generator_test():
    d = Data1(1, 2, 3)
    for x in d:
        print(x)


if __name__ == "__main__":
    # distinct_list()
    # vars_test()
    # unicode_test()
    # iterator_test()
    generator_test()
