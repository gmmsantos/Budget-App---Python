class Category:

    def __init__(self, category):
        self.category = category
        self.list_ledger = []

    def deposit(self, amount, description=""):

        dict_deposit = {"amount": amount, "description": description}
        self.list_ledger.append(dict_deposit)

    def withdraw(self, amount, description="", funds):
        funds = get_balance()
        dict_withdraw = {"amount": 0 - amount, "description": description}
        if funds > amount:
            self.list_ledger.append(dict_withdraw)
        return False

    def get_balance(self):

        total = 0
        the_key = "amount"
        values_of_the_key = [d[the_key] for d in self.list_ledger]

        for value in values_of_the_key:
            total = total + value
        return total

    def transfer(self, amount, another_category):

        dict_transfer = {"amount": 0 - amount,
                         "description": "Tranfer to " + another_category.category}
        self.list_ledger.append(dict_transfer)

        dict_transfer_deposit = {"amount": amount,
                                 "description": "Tranfer from " + self.category}

        another_category = Category()  # VER COM FELIPE
        another_category.list_ledger.append(dict_transfer_deposit)

    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass
