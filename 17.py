class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit (self, amount):
        self.__balance += amount
        print(f"u deposited {amount}, ur balance is :{self.__balance}")
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Not enough money, ur blance is: {self.__balance} ")
            return False, self.__balance 
        else:
            self.__balance -= amount
            print(f"u withdrawn {amount}, ut balance is: {self.__balance}")
            return True, self.__balance  # возвращаем кортеж (статус, баланс)
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Beka", 2000)
print(account1.get_balance())

print(account1.deposit(200))
print(account1.withdraw(500))
print(account1.get_balance())
