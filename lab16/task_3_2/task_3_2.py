class ShopItem:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.quantity} pcs"


class Shop:
    def __init__(self):
        self._items = []

    def add_item(self, item: ShopItem):
        self._items.append(item)

    def get_alpha_iterator(self):
        return ShopIterator(sorted(self._items, key=lambda i: i.name))

    def get_quantity_iterator(self):
        return ShopIterator(sorted(self._items, key=lambda i: -i.quantity))


class ShopIterator:
    def __init__(self, items):
        self._items = items
        self._position = 0

    def has_next(self):
        return self._position < len(self._items)

    def next(self):
        if self.has_next():
            item = self._items[self._position]
            self._position += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    shop = Shop()
    shop.add_item(ShopItem("Bread", 30))
    shop.add_item(ShopItem("Apples", 15))
    shop.add_item(ShopItem("Milk", 50))

    print("[Shop: Alphabetical Order]")
    alpha_it = shop.get_alpha_iterator()
    while alpha_it.has_next():
        print(alpha_it.next())

    print("\n[Shop: By Quantity Descending]")
    qty_it = shop.get_quantity_iterator()
    while qty_it.has_next():
        print(qty_it.next())
