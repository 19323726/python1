
class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity_available: int):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_available = quantity_available

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity_available(self):
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, value):
        if value >= 0:
            self._quantity_available = value
        else:
            print("Error: Quantity cannot be negative")

    def decrease_quantity(self, amount: int) -> bool:
        """Simple interface hiding the implementation details"""
        if amount <= 0:
            print("Error: Amount must be positive")
            return False
        if self._quantity_available >= amount:
            self._quantity_available -= amount
            return True
        else:
            print(f"Error: Not enough stock. Only {self._quantity_available} available")
            return False

    def increase_quantity(self, amount: int) -> None:
        """Simple interface hiding the implementation details"""
        if amount > 0:
            self._quantity_available += amount
        else:
            print("Error: Amount must be positive")

    def display_details(self) -> str:
        """Abstract method to be implemented by subclasses"""
        return f"ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f}, Available: {self._quantity_available}"

    def to_dict(self):
        """Abstract representation of the product"""
        return {
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_available": self._quantity_available
        }


class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity_available: int, weight: float):
        super().__init__(product_id, name, price, quantity_available)
        self._weight = weight  

    @property
    def weight(self):
        return self._weight

    def display_details(self) -> str:
        """Overridden method with different implementation"""
        return f"{super().display_details()}, Weight: {self._weight}kg"

    def to_dict(self):
        """Overridden method with additional data"""
        data = super().to_dict()
        data.update({
            "type": "physical",
            "weight": self._weight
        })
        return data


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity_available: int, download_link: str):
        super().__init__(product_id, name, price, quantity_available)
        self._download_link = download_link   

    @property
    def download_link(self):
        return self._download_link

    
    def display_details(self) -> str:
        """Overridden method with different implementation"""
        return f"{super().display_details()}, Download: {self._download_link}"

    def to_dict(self):
        """Overridden method with additional data"""
        data = super().to_dict()
        data.update({
            "type": "digital",
            "download_link": self._download_link
        })
        return data


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self._product = product  
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
        else:
            print("Error: Quantity cannot be negative")

    def calculate_subtotal(self) -> float:
        return self._product.price * self._quantity

    def __str__(self):
        subtotal = self.calculate_subtotal()
        return f"Item: {self._product.name}, Qty: {self._quantity}, Price: ${self._product.price:.2f}, Subtotal: ${subtotal:.2f}"

    def to_dict(self):
        return {
            "product_id": self._product.product_id,
            "quantity": self._quantity
        }


class ShoppingCart:
    def __init__(self):
        self._items = {}  
        self._product_catalog = self._initialize_catalog()

    def _initialize_catalog(self) -> dict:
        """Initialize with some sample products"""
        catalog = {}
        catalog['1001'] = PhysicalProduct('1001', 'T-Shirt', 19.99, 50, 0.2)
        catalog['1002'] = PhysicalProduct('1002', 'Jeans', 49.99, 30, 0.5)
        catalog['2001'] = DigitalProduct('2001', 'E-Book', 9.99, 1000, 'example.com/download/ebook')
        return catalog

    def add_item(self, product_id: str, quantity: int) -> bool:
        """Add item to cart with validation"""
        if product_id not in self._product_catalog:
            print("Product not found")
            return False
        
        product = self._product_catalog[product_id]
        
        if not product.decrease_quantity(quantity):
            return False
        
        if product_id in self._items:
            self._items[product_id].quantity += quantity
        else:
            self._items[product_id] = CartItem(product, quantity)
        
        return True

    def remove_item(self, product_id: str) -> bool:
        """Remove item from cart"""
        if product_id not in self._items:
            print("Item not in cart")
            return False
        
        item = self._items[product_id]
        product = item.product
        product.increase_quantity(item.quantity)
        del self._items[product_id]
        return True

    def update_quantity(self, product_id: str, new_quantity: int) -> bool:
        """Update item quantity with validation"""
        if product_id not in self._items:
            print("Item not in cart")
            return False
        
        if new_quantity < 0:
            print("Quantity cannot be negative")
            return False
        
        item = self._items[product_id]
        product = item.product
        quantity_diff = new_quantity - item.quantity
        
        if quantity_diff > 0:
            if not product.decrease_quantity(quantity_diff):
                return False
        else:
            product.increase_quantity(-quantity_diff)
        
        item.quantity = new_quantity
        return True

    def get_total(self) -> float:
        """Calculate grand total"""
        return sum(item.calculate_subtotal() for item in self._items.values())

    def display_cart(self) -> None:
        """Display cart contents"""
        if not self._items:
            print("Your cart is empty")
            return
        
        print("\n=== YOUR SHOPPING CART ===")
        for item in self._items.values():
            print(item)
        print(f"\nGRAND TOTAL: ${self.get_total():.2f}")
        print("==========================")

    def display_products(self) -> None:
        """Display available products (demonstrates polymorphism)"""
        print("\n=== AVAILABLE PRODUCTS ===")
        for product in self._product_catalog.values():
            print(product.display_details())  
        print("==========================")

def main():
    cart = ShoppingCart()
    
    while True:
        print("\n==== ONLINE SHOPPING CART ====")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Update Quantity")
        print("5. Remove Item")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            cart.display_products()
        elif choice == '2':
            product_id = input("Enter product ID: ")
            try:
                quantity = int(input("Enter quantity: "))
                if cart.add_item(product_id, quantity):
                    print("Item added to cart!")
                else:
                    print("Failed to add item")
            except ValueError:
                print("Invalid quantity - please enter a number")
        elif choice == '3':
            cart.display_cart()
        elif choice == '4':
            product_id = input("Enter product ID: ")
            try:
                new_quantity = int(input("Enter new quantity: "))
                if cart.update_quantity(product_id, new_quantity):
                    print("Quantity updated!")
                else:
                    print("Failed to update quantity")
            except ValueError:
                print("Invalid quantity - please enter a number")
        elif choice == '5':
            product_id = input("Enter product ID to remove: ")
            if cart.remove_item(product_id):
                print("Item removed from cart!")
            else:
                print("Failed to remove item")
        elif choice == '6':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice - please enter 1-6")

if __name__ == "__main__":
    main()
