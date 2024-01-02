class Store:
    def __init__(self):
        self.products = {"Product1": 100, "Product2": 50, "Product3": 30}
        self.bill = {}

    def display_menu(self):
        print("Product Menu:")
        for product, price in self.products.items():
            print(f"{product}: Rs.{price}")

    def generate_bill(self):
        print("Your Bill:")
        total_amount = 0
        for product, quantity in self.bill.items():
            price = self.products[product]
            total_price = price * quantity
            print(f"{product} x {quantity}: Rs.{total_price}")
            total_amount += total_price
        print("Total Amount: Rs.{}".format(total_amount))

    def take_order(self, product, quantity):
        if product in self.products and quantity > 0:
            self.bill[product] = quantity
            print(f"{quantity} {product}(s) added to your bill.")
        else:
            print("Invalid product or quantity.")

store = Store()
store.display_menu()
store.take_order("Product1", 2)
store.take_order("Product3", 1)
store.generate_bill()