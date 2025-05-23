from datetime import datetime, timedelta

class FoodItem:
    """
    Represents a food item stored in the fridge, tracking its quantity and expiration dates.

    Attributes:
    - name (str): Name of the food item.
    - quantity (int): Number of units of the item.
    - date_added (datetime): Timestamp when the item was first added.
    - expiration_dates (list of str): List of expiration dates for each unit (in 'YYYY-MM-DD' format).
    """

    def __init__(self, name, quantity=1, date_added=None, expiration_date=None):
        """
        Initializes a FoodItem instance.

        Parameters:
        - name (str): Name of the food item.
        - quantity (int): Number of units added (default is 1).
        - date_added (datetime, optional): Date the item was added. Defaults to current time.
        - expiration_date (str, optional): Expiration date for the item(s) in 'YYYY-MM-DD' format.
                                            If provided, creates one entry per quantity unit.
        """
        self.name = name
        self.quantity = quantity
        self.date_added = datetime.now() if date_added is None else date_added
        self.expiration_dates = []

        if expiration_date:
            for i in range(quantity):
                self.expiration_dates.append(expiration_date)
    
    def add_quantity(self, quantity, expiration_date=None):
        """
        Adds more units of the food item, optionally with their expiration dates.

        Parameters:
        - quantity (int): Number of units to add.
        - expiration_date (str, optional): Expiration date for the added units.
        """
        self.quantity += quantity
        if expiration_date:
            for i in range(quantity):
                self.expiration_dates.append(expiration_date)
    
    def add_expiration_date(self, expiration_date):
        """
        Adds a single expiration date to the expiration_dates list.

        Parameters:
        - expiration_date (str): Expiration date to add.
        """
        self.expiration_dates.append(expiration_date)

    def __str__(self):
        """
        Returns a readable string representation of the FoodItem.

        Example output:
        "Milk: 3 total, Added on 2025-05-23 14:33:10.123456, Expiration dates: 2025-06-01, 2025-06-02, 2025-06-03"
        """
        return f"{self.name}: {self.quantity} total, Added on {self.date_added}, Expiration dates: {', '.join(self.expiration_dates)}"
