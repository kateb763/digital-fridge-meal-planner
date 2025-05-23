from datetime import datetime
from food_item import FoodItem

class Fridge:
    """
    A class to manage food items in a digital fridge, including quantity tracking and expiration monitoring.
    """

    def __init__(self):
        """
        Initializes the fridge with an empty dictionary of items.
        """
        self.items = {}

    def add_item(self, name, quantity=1, expiration_date=None):
        """
        Adds a new food item to the fridge or updates the quantity and expiration date if it already exists.

        Parameters:
        - name (str): Name of the food item.
        - quantity (int): Number of units to add. Defaults to 1.
        - expiration_date (str): Optional expiration date in 'YYYY-MM-DD' format.
        """
        if name in self.items:
            self.items[name].add_quantity(quantity, expiration_date)
        else:
            self.items[name] = FoodItem(name, quantity, expiration_date)

    def remove_item(self, name, quantity_to_remove=1):
        """
        Removes a specified quantity of a food item from the fridge.

        Parameters:
        - name (str): Name of the food item to remove.
        - quantity_to_remove (int): Number of units to remove. Defaults to 1.

        If the quantity to remove is greater than what’s available, prints a warning.
        """
        if name in self.items:
            if self.items[name].quantity > quantity_to_remove:
                self.items[name].quantity -= quantity_to_remove
            else:
                print(f"The quantity you are trying to remove ({quantity_to_remove}) is greater than the amount of {name} in the fridge. There are currently {self.items[name].quantity} {name}s in the fridge.")
        else:
            print(f"{name} is not in the fridge.")

    def list_all_items(self):
        """
        Prints all food items currently in the fridge with their quantities and expiration dates.
        """
        if len(self.items) == 0:
            print("The fridge is empty.")
        else:
            for item in self.items.values():
                print(f"{item}\n")  

    def check_expired_items(self, current_date=None):
        """
        Checks and returns a list of expired food items.

        Parameters:
        - current_date (str): The date to check against in 'YYYY-MM-DD' format. 
                              If not provided, defaults to today.

        Returns:
        - List of item names that are expired.
        """
        if not current_date:
            current_date = datetime.now().strftime("%Y-%m-%d")
        expired_items = []
        for item in self.items.values():
            for date in item.expiration_dates:
                if date < current_date:
                    expired_items.append(item.name)
        return expired_items
