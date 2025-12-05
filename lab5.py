




class BankAccount():
    """
    Клас, що представляє банківський рахунок.
    """
    def __init__(self, id = 0, owner_name = "", balance = 0):

        if owner_name is None or owner_name == "":
            raise TypeError("Некоректне ім'я")
        
        if id < 0:
            raise ValueError("Айді не може бути від'ємним")
        
        self.__id = id
        self.owner_name = owner_name
        self.__balance = float(balance)
    
    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_balance(self):
        return self.__balance
    
    
    def add_funds(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Рахунок #{self.__id} поповнено на {amount} UAH.")
        else:
            raise ValueError("Сумма поповнення має бути додатньою")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатнім числом")
        elif amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        else:
            self.__balance -= amount
            print(f"З рахунку #{self.__id} знято {amount} UAH.\n Поточний баланс: {self.__balance:.2f}")

    def show_account(self):
        print(f"\nінформація про аккаунт\n \
            ID: {self.__id}\n \
            Власник: {self.owner_name}\n \
            Баланс:{self.__balance:.2f} UAH")
        
    def __del__(self):
        print(f"\nАккаунт користувач {self.owner_name} (ID #{self.__id}) видаляється")



class Bank():
    """Клас банку. Сховище рахунків"""
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, BankAccount):
            self.accounts.append(account)
            print(f"Аккаунт {account.get_id} додано до банку {self.name}")
        else:
            raise TypeError("Об'єкт не є типу 'BankAccount'")
        
    def remove_account(self, account_id):
        for account in self.accounts:
            if account.id == account_id:
                self.accounts.remove(account)
                print(f"Аккаунт #{account_id} видалено з банку")
                return
        print(f"Аккаунт з ID {account_id} не знайдено")

    def sort_by_balance(self):
        self.accounts.sort(key = lambda acc: acc.balance)
        print("Рахунки відсортовані за балансом")

    def show_all_accounts(self):
        print(f"\n\nВсі рахунки в банку {self.name}")
        if self.accounts:
            for account in self.accounts:
                account.show_account()

    def avg_balance_odd_ids(self):
        total_sum = 0
        count = 0
        for account in self.accounts:
            if account.get_id % 2 != 0:
                count += 1
                total_sum += account.get_balance
        avg_balance = total_sum / count
        print(f"\nСереднє значення балансу непарних id {avg_balance:.2f}")

def main():
    bank1 = Bank("Monobank")
    acc1 = BankAccount(0, "Іван Петренко", 500)
    acc2 = BankAccount(1, "Марія Коваль", 103.06)
    acc3 = BankAccount(2, "Олексій Сидоренко", 340.2)
    acc4 = BankAccount(3, "Іван Петренко", 608)
    acc5 = BankAccount(4, "Марія Коваль", 1003)
    acc6 = BankAccount(5, "Олексій Сидоренко", 242.33)

    bank1.add_account(acc1)
    bank1.add_account(acc2)
    bank1.add_account(acc3)
    bank1.add_account(acc4)
    bank1.add_account(acc5)
    bank1.add_account(acc6)
    bank1.show_all_accounts()
    bank1.avg_balance_odd_ids()


if __name__ == "__main__":
    main()