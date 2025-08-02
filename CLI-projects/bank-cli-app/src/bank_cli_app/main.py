from abc import ABC,abstractmethod 
from bank_cli_app.utility import generate_account_number,generate_pin



class BankAccount(ABC):
    def __init__(self,account_number: str, account_type: str, account_holder: str) -> None:
        self.account_type: str = account_type
        self.account_holder: str =  account_holder
        self.account_number: str = account_number
        self.balance: float = 0.0  # Initial balance is set to zero
        self.pin: int = generate_pin()
        
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass
    

    def transfer(self,amount:float,recipient_account: "BankAccount") -> None:
        if self.verify_pin():
            if amount>0 and amount <= self.balance:
                self.balance -= amount 
                recipient_account.balance += amount 
                print(f"Transfer successful! ${amount:.2f} has been transferred to {recipient_account.account_holder}.")
                print(f"Your new balance is: ${self.balance:.2f}")
            elif amount > self.balance:
                print("Insufficient funds for this transfer.")
            else:
                print("Invalid transfer amount. Please enter a value greater than zero.")

    
    
    def verify_pin(self) -> bool:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False
    
    def display_balance(self) -> float:
        if self.verify_pin():
            return self.balance
    
    def display_account_details(self) -> None:
        # print("This is one time information show")
        
        print("=" * 30)  # Separator for clarity
        print("Please save your pin and account number")
        
        print("Account Information:")
        
        print(f"Account Type: {self.account_type}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account PIN: {self.pin}")
        print(f"Account Balance: ${self.balance:.2f}")
        
        print("=" * 30)  # Separator for clarity

class SavingsAccount(BankAccount):
    
    def deposit(self, amount: float) -> None:
        if self.verify_pin():
            if amount > 0:
                self.balance += amount 
                print(f"Deposit successful, {self.account_holder}! Your new balance is: ${self.balance:.2f}")
        
            else:
                print("Invalid deposit amount. Please enter a value greater than zero.")
            
    def withdraw(self, amount: float) -> None:
        if self.verify_pin():
            if amount > 0 and amount <= self.balance:
                self.balance -= amount 
                print(f"Withdrawal successful, {self.account_holder}! Your new balance is: ${self.balance:.2f}")

            elif amount > self.balance:
                print("Insufficient funds for this withdrawal.")

            else:
                print("Invalid withdrawal amount. Please enter a value greater than zero.")
        




class CurrentAccount(BankAccount):

    def __init__(self, account_number:str,account_type: str,  account_holder: str,overdraft_limit: float = 100.00) -> None:
        super().__init__(account_number,account_type,  account_holder)
        self.overdraft_limit: float = overdraft_limit

    
    def deposit(self, amount: float) -> None:
        if self.verify_pin():
            if amount > 0:
                self.balance += amount 
                print(f"Deposit successful, {self.account_holder}! Your new balance is: ${self.balance:.2f}")
    
            else:
                print("Invalid deposit amount. Please enter a value greater than zero.")

    def withdraw(self, amount: float) -> None:
        if self.verify_pin():
            if amount > 0 and amount <= (self.balance + self.overdraft):
                self.balance -= amount 
                print(f"Withdrawal successful, {self.account_holder}! Your new balance is: ${self.balance:.2f}")
            elif amount > self.balance:
                print("Insufficient funds for this withdrawal.")

            else:
                print("Invalid withdrawal amount. Please enter a value greater than zero.")


accounts = {}

account_numbers = {}

options = ['create account', 'deposit', 'withdraw', 'transfer', 'display balance', 'quit'] 


while True:
    
    print("Please select an option:")
    for index, option in enumerate(options, start=1):
        print(f'Press {index} {option}\n')
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\n\n\n")  
        account_type = input("Enter account type (Current/Savings): ")
        account_number = generate_account_number()
        account_holder = input("Enter account holder name: ")

        if account_number in account_numbers:
            print("An account with this account number already exists.\n")

        else:
            if account_type.lower() == "savings" or account_type.lower() == "current":
                if account_type.lower() == "savings":
                    accounts[account_number] = SavingsAccount(account_type, account_number, account_holder)

                elif account_type.lower() == "current":
                    accounts[account_number] = CurrentAccount(account_type, account_number, account_holder)
                
                account_numbers[account_number] = account_number 
                # print(f'Account successfully created for {account_holder} with account type: {account_type}.\n')
                accounts[account_number].display_account_details()

            else: 
                print("Invalid account type. Please enter either 'Current' or 'Savings'.\n")
        print("\n\n\n")  


    elif choice == "2":
        print("\n\n\n")  
        account_number = input("Enter account holder number for deposit: ")

        if account_number in accounts:
            account_type = accounts[account_number].account_type
            account_holder = accounts[account_number].account_holder
            amount = float(input(f"Enter deposit amount for {account_holder}, Account Type: {account_type}: "))
            accounts[account_number].deposit(amount)
            print()
            
        else:
            print(f"Account holder '{account_holder}' not found. Please create an account first.\n")
        print("\n\n\n")  


    elif choice == "3":
        print("\n\n\n")  
        account_number = input("Enter account holder number for withdrawal: ")
        if account_number in accounts:
            account_type = accounts[account_number].account_type
            account_holder = accounts[account_number].account_holder
            amount = float(input(f"Enter withdrawal amount for {account_holder}, Account Type: {account_type}: "))
            accounts[account_number].withdraw(amount)
            print()
        else:
            print(f"Account holder '{accounts[account_number].account_holder}' not found. Please create an account first.\n")
        print("\n\n\n")  
    
    elif choice == "4":
        print("\n\n\n")  
        account_number = input("\n\n\nEnter your account number for transfer: ")
        transfer_account_number = input("Enter the account number to transfer money to: ")
        if account_number in accounts and transfer_account_number in accounts:
            amount = float(input("Enter the amount to transfer: "))
            accounts[account_number].transfer(amount=amount,recipient_account=accounts[transfer_account_number])
        else:
             print("The account numbers to transfer to does not exist.\n")
        print("\n\n\n")  
        


    elif choice == "5":
        print("\n\n\n")  
        account_number = input("Enter account holder name for balance display: ")

        if account_number in accounts:
            account_type = accounts[account_number].account_type
            balance = accounts[account_number].display_balance()
            account_holder = accounts[account_number].account_holder
            print(f"\n\n\nAccount Holder: {account_holder}\nAccount Type: {account_type}\nCurrent Balance: ${balance:.2f}\n\n\n")
        else:
            print(f"Account holder '{accounts[account_number].account_holder}' not found. Please create an account first.\n")
        print("\n\n\n")  
            
    elif choice == "6":
        print("\n\n\n")  
        print("\nThank you for using our banking app! 😊 Have a great day!\n")
        print("\n\n\n")  
        break
    
    else:
        print("\nInvalid input choice. Please enter a number between 1 and 5.\n")





            
        
    