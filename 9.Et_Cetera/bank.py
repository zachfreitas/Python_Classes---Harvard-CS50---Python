# Global Variables
# balance = 0 # Global Variable

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     print("Balance:", balance)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main()
    


# The following is better than using global variables.

class Account:
    def __init__(self):
        self._balance = 0
    
    def __str__(self) -> str:
        return f"{self._balance}"
    
    # Getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n



def main():
    account = Account()
    print(account)
    account.deposit(100)
    account.withdraw(50)
    print(account)
    
    
if __name__ == "__main__":
    main()