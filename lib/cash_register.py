#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        # Internal log to track previous item batches for voiding
        self._transaction_history = []

    
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    
    def add_item(self, item, price, quantity=1):
        # Update total based on quantity
        self.total += price * quantity
        
        # Populate the items list with duplicates matching the quantity
        for _ in range(quantity):
            self.items.append(item)
            
        # Record this specific batch execution for potential voiding
        self._transaction_history.append((item, price, quantity))

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)
            
            # Format cleanly to match test expected strings (e.g., $800 instead of $800.0)
            display_total = int(self.total) if isinstance(self.total, (int, float)) and self.total.is_integer() else round(self.total, 2)
            print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        if not self._transaction_history:
            return
            
        # Retrieve the parameters of the last item batch added
        item, price, quantity = self._transaction_history.pop()
        
        # Revert price change entirely
        self.total -= price * quantity
        
        # Remove the correct count of item strings from the list
        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)
