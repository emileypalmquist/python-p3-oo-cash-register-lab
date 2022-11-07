#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, item, price, quantity=1):
        for i in range(0, quantity):
            self.items.append(item)
        new_price = price * quantity
        self.transactions.append({
            "price": new_price,
            "item": item,
            "quantity": quantity
        })
        self.total += new_price

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * self.discount / 100
            print(
                f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        removed = self.transactions.pop()
        for i in range(0, removed["quantity"]):
            self.items.pop()
        self.total -= removed["price"]
