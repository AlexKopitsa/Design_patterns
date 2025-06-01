from abc import ABC, abstractmethod
from collections import deque

# === Component ===
class Element(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


# === Leaf ===
class Item(Element):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Item({self.name}, {self.price})"


# === Composite ===
class Box(Element):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, element: Element):
        self.children.append(element)

    def get_price(self):
        return sum(child.get_price() for child in self.children)

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def __str__(self):
        return f"Box({self.name})"


# === Iterators ===
class DepthIterator:
    def __init__(self, root: Element):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current = self.stack.pop()
            if isinstance(current, Box):
                self.stack.extend(reversed(current.get_children()))
            return current
        raise StopIteration


class BreadthIterator:
    def __init__(self, root: Element):
        self.queue = deque([root])

    def __iter__(self):
        return self

    def __next__(self):
        while self.queue:
            current = self.queue.popleft()
            if isinstance(current, Box):
                self.queue.extend(current.get_children())
            return current
        raise StopIteration


# === Analysis ===
def find_cheapest(iterator):
    return min((el for el in iterator if isinstance(el, Item)), key=lambda x: x.get_price())

def find_most_expensive(iterator):
    return max((el for el in iterator if isinstance(el, Item)), key=lambda x: x.get_price())


# === Client code ===
if __name__ == "__main__":
    root = Box("Main")
    box1 = Box("Box1")
    box2 = Box("Box2")
    item1 = Item("Book", 120)
    item2 = Item("Phone", 1000)
    item3 = Item("Pen", 15)
    item4 = Item("Watch", 500)

    box1.add(item1)
    box1.add(item2)
    box2.add(item3)
    root.add(box1)
    root.add(box2)
    root.add(item4)

    print("[Depth-first traversal]")
    for el in DepthIterator(root):
        print(f"{el.get_name()} - {el.get_price()}")

    print("\n[Breadth-first traversal]")
    for el in BreadthIterator(root):
        print(f"{el.get_name()} - {el.get_price()}")

    print("\n[Cheapest item]")
    print(find_cheapest(DepthIterator(root)))

    print("\n[Most expensive item]")
    print(find_most_expensive(DepthIterator(root)))
