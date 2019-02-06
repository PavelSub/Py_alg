import sys


class SMem:

    def __init__(self):
        self.s_m = 0
        self.m_adres = []

    def sum_items(self, objs):
        for el in objs:
            if el.startswith('__') or hasattr(objs[el], '__call__') or hasattr(objs[el], '__loader__'):
                continue
            else:
                self.sum_el(objs[el])

    def sum_el(self, it):
        if id(it) not in self.m_adres:
            print(f' {id(it)}, Тип - {type(it)}, объект {it}, память - {sys.getsizeof(it)}')
            self.s_m += sys.getsizeof(it)
            self.m_adres.append(id(it))
            if hasattr(it, '__iter__'):
                if hasattr(it, 'items'):
                    for key, value in it.items():
                        self.sum_el(key)
                        self.sum_el(value)
                elif not isinstance(it, str):
                    for el2 in it:
                        self.sum_el(el2)

    def print_sum(self):
        print(f'Общие затраты памяти - {self.s_m}')
