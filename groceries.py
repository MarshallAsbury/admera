class GroceryItem:
    """
        Represents an item from the Grocery store.
    """
    
    name = ''
    price =  0.00

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def set_name(self, name: str) -> None:
        self.name = name
    def set_price(self, price: float) -> None:
        self.price = price

    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class GroceryList:
    """
        Represents groceries.
    """

    groceries = []

    def __init__(self):
        pass

    def add_item(self, item: GroceryItem) -> None:
        self.groceries.append(item)
    
    def total_price(self) -> float:
        total = 0.00
        for item in self.groceries:
            total = total + item.get_price()
        return total    


# make a few lists
# all of the prices are wrong


if __name__ == '__main__':
    milk = GroceryItem('milk', 3.99)
    eggs = GroceryItem('eggs', 2.99)
    bread = GroceryItem('bread', 3.99)
    chicken = GroceryItem('chicken', 8.99)
    peppers = GroceryItem('peppers', 0.99)
    scallops = GroceryItem('scallops', 19.99)
    tofu = GroceryItem('tofu', 1.99)
    wine = GroceryItem('wine', 12.99)
    lemon = GroceryItem('lemon', 0.45)
    
    grocery_a = GroceryList()
    grocery_b = GroceryList()
    grocery_c = GroceryList()

    grocery_a.add_item(milk)
    grocery_a.add_item(eggs)

    print(grocery_a.total_price())

    grocery_b.add_item(bread)
    grocery_b.add_item(scallops)
    grocery_b.add_item(lemon)
    grocery_b.add_item(lemon)
    grocery_b.add_item(lemon)
    grocery_b.add_item(wine)

    print(grocery_b.total_price())

    grocery_c.add_item(chicken)
    grocery_c.add_item(peppers)
    grocery_c.add_item(tofu)

    print(grocery_c.total_price())
