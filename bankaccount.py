class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"${amount} Withdrawal successful. Available balance: {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} Deposited successfully. Available balance: {self.balance}")

ac1 = BankAccount()
ac1.set_details("Alice", 1000)
ac1.display()
ac1.deposit(500)
ac1.withdraw(2000)
ac1.display()

print("\n----------------\n")

# Creating second instance
account2 = BankAccount()
account2.set_details("Bob")
account2.display()
account2.deposit(200)
account2.withdraw(100)
account2.display()
