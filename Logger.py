from itertools import groupby


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BoardRepr:

    def __init__(self, array_repr, depth, evaluation):
        self.array_repr = array_repr
        self.depth = depth
        self.eval = evaluation

    def __iter__(self):
        return self.array_repr

    def __str__(self):
        return str(self.array_repr)

    def __getitem__(self, item):
        if item == len(self.array_repr) - 1:
            return self.array_repr[item] + [" depth:{}|eval:{}]\t".format(self.depth, self.eval)]
        return self.array_repr[item] + ["\t\t\t\t\t"]

    def __repr__(self):
        return str(self.depth)


class Logger(metaclass=Singleton):
    log_file = 'minimax_tree.txt'

    def __init__(self):
        self.arr = []

    def append(self, item: BoardRepr):
        for idx, it in enumerate(self.arr):
            if it.depth == item.depth and idx < len(self.arr) - 1:
                if self.arr[idx + 1].depth < item.depth:
                    self.arr = self.arr[:idx] + [item] + self.arr[idx:]
                    return
        self.arr.append(item)

    def clear(self):
        open(self.log_file, 'w').close()
        self.arr.clear()

    def write(self):

        with open(self.log_file, 'a', encoding='utf-8') as f:
            for i, g in groupby(self.arr, key=lambda x: x.depth):
                board_repr = list((k for k in g))
                for idx, _ in enumerate(board_repr[0].array_repr):
                    for item in board_repr:
                        f.write(''.join(list(i for i in item[idx])))
                    f.write("\n")
                f.write("\n")
