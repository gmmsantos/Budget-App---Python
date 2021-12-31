class Category:
    def __init__(self, category):
        self.category = category
        self.list_ledger = []
        self.balance = 0

    def __str__(self) -> str:
        return (
            self.title_line()
            + "\n"
            + self.display_ledger()
            + "\n"
            + "Total: "
            + str(self.balance)
        )

    def title_line(self):
        name_length = len(self.category)
        if name_length % 2 == 0:
            stars_number = int((15 - (name_length / 2)))
            title = (stars_number * "*") + self.category + (stars_number * "*")
        else:
            stars_number = int((15 - (name_length // 2)))
            title = (stars_number * "*") + self.category + ((stars_number - 1) * "*")

        return title

    def display_ledger(self):
        lines = ""
        for i in range(len(self.list_ledger)):
            value_description = self.list_ledger[i]["description"]
            value_amount = self.list_ledger[i]["amount"]
            spaces = 29 - len(value_description)
            lines = (
                lines
                + (
                    value_description[:23]
                    + " "
                    + str("%0.2f" % value_amount).rjust(spaces)
                )
                + "\n"
            )
        return lines

    def deposit(self, amount, description=" "):

        dict_deposit = {"amount": amount, "description": description}
        self.list_ledger.append(dict_deposit)
        self.balance += amount

    def withdraw(self, amount, description=" "):

        if self.balance >= amount:
            dict_withdraw = {"amount": 0 - amount, "description": description}
            self.list_ledger.append(dict_withdraw)
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, another_category):

        if self.withdraw(amount, description="Tranfer to " + another_category.category):
            another_category.deposit(
                amount, description="Tranfer from " + self.category
            )
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
