from typing import Any, Tuple


class Cache:
    def __init__(self, *args) -> None:
        self.items = set(args)

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __add__(self, items):
        if isinstance(items, (list, tuple, set, Cache)):
            for item in items:
                self.items.add(item)

        else:
            self.items.add(items)
        return self

    def __iadd__(self, item):
        return self.__add__(item)

    def __isub__(self, item):
        return self.__sub__(item)

    def __sub__(self, items):
        if isinstance(items, (list, tuple, set, Cache)):
            self.items = set([item for item in self.items if item not in items])
        else:
            self.items = set([item for item in self.items if item != items])
        return self

    def __delitem__(self, item) -> None:
        self.items.remove(item)

    def append(self, item):
        return self.__add__(item)

    def remove(self, item):
        return self.__sub__(item)

    def get_or_set(self, item) -> Tuple[bool, Any]:
        is_set = False
        if item not in self.items:
            self.items.add(item)
            is_set = True
        return is_set, item

    def __repr__(self) -> str:
        return str(self.items)

    def __matmul__(self, items: list[Any]):
        return set([item for item in items if item not in self.items])


global_cache = Cache()
