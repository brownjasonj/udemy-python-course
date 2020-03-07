class Account:
    def __init__(self, owner: str, initial_balance: float) -> None:
        self.owner = owner
        self.balance = initial_balance
    
    def __str__(self) -> str:
        return f"Account Owner: {self.owner} \nAccount Balance: {self.balance}"

    def deposit(self, deposit_amount: float) -> float:
        self.balance += deposit_amount
        print("Deposit Accepted")
        return self.balance
    
    def withdraw(self, withdrawal_amount: float) -> float:
        if self.balance < withdrawal_amount:
            print("Funds unavailable")
        else:
            print("Withdrawal Accepted")
            self.balance -= withdrawal_amount
        return self.balance



jose = Account("Jose", 100)
print(jose)

print(jose.deposit(50))

print(jose.withdraw(75))

print(jose.withdraw(500))





