# Nicholas Bryan - 201531951
# COMP517 - CA4 Bank Accounts

# import the random and datetime module for use in class methods
import random
import datetime

class BasicAccount:
    """BasicAccount provides account holder with an account number and bank card, allowing customer to perform deposit, withdrawal and balance transactions"""

    # account numbers are serialised, so acNum is set to 0 to begin with
    acNum = 0

    def __init__(self, acName, openingBalance):
        """Initialiser creates an instance of the BasicAccount
        
        Attributes:
            name (str): stores name of the account holder
            acNum (int): stores account number
            balance (float): stores account balance in GBP
            cardNum (str): stores 16-digit bank card number
            cardExp (:obj:'tuple' of :obj:'int'): stores month and year of bank card expiration as tuple (mm,yy)

        Args:
            acName (str): name of the account holder
            openingBalance (float): amount in GBP to open account

        Raises:
            ValueError: if invalid data type is entered as openingBalance
            AttributeError: if PremiumAccount is created
        """

        print("\nOpening new account...")
        self.balance = float(openingBalance)
        self.name = str(acName)
        BasicAccount.acNum += 1 # increment acNum by 1 for account number serialisation
        self.acNum = BasicAccount.acNum
    
        # if a BasicAccount is being created, try block is executed
        try:
            print(self)
            self.issueNewCard()
            print("\n{self.name}'s account is now active.".format(self=self))
        # AttributeError occurs when PremiumAccount is being created because cannot print(self) from super().__init__ method before all parameters of PremiumAccount have been assigned to self
        except AttributeError:
            return


    def __str__(self):
        """Returns string representation of an instance, giving the account name, account number and available balance
                
        Returns:
            str: string representation of instance
        """

        return "\nBasic Account\nAccount Name: {self.name}\nAccount Number: {self.acNum:03d}\nAvailable Balance: £{self.balance:.2f}".format(self=self)


    def deposit(self, amount):
        """Adds the stated amount to the account balance.

        Args: 
            amount (float): amount to be deposited in pounds (GBP), must be a positive amount
        """

        print("\nDeposit - {self.name}".format(self=self))

        # checks for negative amount value
        if amount < 0:
            print("Cannot deposit £{0:.2f}".format(amount))
            print("Deposit amount cannot be a negative value.")
        
        # adds amount to account balance
        else:
            self.balance += amount
            print("{0} has deposited £{1:.2f}. New balance is £{2:.2f}".format(self.name, amount, self.balance))


    def withdraw(self, amount):
        """Withdraws the stated amount from the account, by subtracting the amount from the balance
        
        Args: 
            amount (float): amount to be withdrawn in pounds (GBP), must be a positive amount
        """

        print("\nWithdrawal - {self.name}".format(self=self))

        # retrieves the available balance in the account
        availableBalance = self.getAvailableBalance()
        
        # checks for negative amount value       
        if amount < 0:
            print("Cannot withdraw £{0:.2f}".format(amount))
            print("Deposit amount cannot be a negative value.")

        # checks whether amount requested is greater than the available balance
        elif amount > availableBalance:
            print("Cannot withdraw £{0:.2f}".format(amount))
            print("Insufficient funds.")

        # subtracts amount from account balance
        else:
            self.balance -= amount
            print("{0} has withdrew £{1:.2f}. New balance is £{2:.2f}".format(self.name, amount, self.balance))


    def getAvailableBalance(self):
        """Returns the total balance that is available in the account as a float
        
        Returns:
            availableBalance (float): balance of the account in pounds (GBP), must be a positive value
        """

        # there are no overdrafts for a BasicAccount, therefore available balance is equal to the account balance
        availableBalance = self.balance
        return availableBalance


    def getBalance(self):
        """Returns the balance of the account as a float. If the account is overdrawn, then it should return a negative value
 
        Returns:
            balance (float): balance of the account in pounds (GBP), can be positive or negative value
        """

        return self.balance


    def printBalance(self):
        """Prints to screen the balance of the account"""

        print("\nBalance - {self.name}".format(self=self))
        print("Account balance: £{self.balance:.2f}".format(self=self))


    def getName(self):
        """Returns the name of the account holder as a string
        
        Returns:
            name (str): name of the account holder
        """

        return self.name


    def getAcNum(self):
        """Returns the account number as a string
        
        Returns:
            strAcNum (str): string representation of the account number
        """

        # stores the integer account number as a formatted 3-digit string (in which 0's occupy unused digits)
        strAcNum = str("{self.acNum:03d}".format(self=self))
        return strAcNum


    def addThreeYears(self, today):
        """Adds three years to current date to find expiry date of card
        
        Args:
            today (:obj: datetime.date): today's date

        Raises:
            ValueError: if today's date is 29th February (in a leap year)

        Returns:
            threeYearsToday (:obj: datetime.date): date three years from today (to the month)
        """

        # if today's date is any date except for 29th February (in a leap year), try block is executed, adding 3 years to current date
        try:
            threeYearsToday = today.replace(year = today.year + 3)
            return threeYearsToday

        # if today's date is 29th February (in a leap year), a ValueError is raised when 3 years are added because 29th Feb will only occur every 4 years
        except ValueError:
            # adds 3 years, then subtracts 1 day, so that resulting date is 28th Feb in three years, therefore expiry date will still be in the same month in 3 years time
            threeYearsToday = today.replace(year = today.year + 3, month = today.month, day = today.day - 1)
            return threeYearsToday


    def issueNewCard(self):
        """Generates a new 16-digit card number, with the expiry date of the card being 3 years to the month from now. (eg: if today is 03/01/21, then the expiry date would be (01/24))"""

        print("\nIssue New Card - {self.name}".format(self=self))
        
        # stores new card number an integer that has been randomly generated between 1 and the largest 16-digit number
        intCardNum = random.randint(1,9999999999999999)
        # formats the card number integer as a 16-digit string (in which 0's occupy unused digits)
        self.cardNum = str("{0:016d}".format(intCardNum))
        
        # stores today's date as today
        today = datetime.date.today()
        # calls the addThreeYears method and assigns this as the expiry date
        expiryDate = self.addThreeYears(today)
        # formats the year of the expiry date in the 2-digit 'yy' form and casts to an integer
        formattedExpiryYear = int(expiryDate.strftime("%y"))
        # stores the expiry date as a tuple of integers (mm, yy)
        self.cardExp = (expiryDate.month, formattedExpiryYear)
        
        print("Card Number: {self.cardNum}\nExpiry Date (mm/yy): {self.cardExp[0]:02d}/{self.cardExp[1]:02d}".format(self=self))


    def printCardDetails(self):
        """Prints the 16-digit number and mm/yy expiry date of the customer's card"""
        
        print("\nCard Details - {self.name}\nCard Number: {self.cardNum}\nExpiry Date (mm/yy): {self.cardExp[0]:02d}/{self.cardExp[1]:02d}".format(self=self))


    def closeAccount(self):
        """Closes customer's account by withdrawing total balance from the account and returning true (note: instance is not actually deleted).
        
        Returns:
            boolean: true if account has been closed
        """

        print("\nClosing {self.name}'s account...".format(self=self))
        # withdraws remaining account balance
        self.withdraw(self.balance)
        print("Account closed.")
        return True


class PremiumAccount(BasicAccount):
    """PremiumAccount is a subclass of BasicAccount, providing the customer with all the features of a BasicAccount, as well as eligibility for an overdraft"""

    def __init__(self, acName, openingBalance, initialOverdraft):
        """Initialiser creates an instance of the PremiumAccount

        Attributes (inherits all attributes of BasicAccount, plus following):
            overdraft (boolean): true if the account can have an overdraft (default), false if overdraft not available
            overdraftLimit (float): amount in GBP that the account can go overdrawn by

        Args:
            acName (str): name of the account holder
            openingBalance (float): amount in GBP to open account
            initialOverdraft (float): amount in GBP that the account can go overdrawn by (must be >= 0)
        """
        
        super().__init__(acName, openingBalance)
        
        self.overdraftLimit = initialOverdraft
        # defines overdraft boolean as true, regardless of initial overdraft, therefore overdraft is an option for a PremiumAccount upon account creation
        self.overdraft = True
        
        print(self)
        self.issueNewCard()
        print("\n{self.name}'s account is now active.".format(self=self))


    def __str__(self):
        """Returns string representation of an instance, giving the the account name, account number, available balance and overdraft limit
        
        Returns:
            str: string representation of instance
        """

        availableBalance = self.getAvailableBalance()
        return "\nPremium Account\nAccount Name: {0}\nAccount Number: {1:03d}\nAvailable Balance: £{2:.2f}\nOverdraft Limit: £{3:.2f}".format(self.name, self.acNum, availableBalance, self.overdraftLimit)


    def setOverdraftLimit(self, newLimit):
        """Sets the overdraft limit to the stated amount, if an overdraft is available on the account
        
        Args:
            newLimit (float): amount in GBP that the account can go overdrawn by (must be >= 0), updates the overdraft limit
        """

        # checks if account can have an overdraft
        if self.overdraft == False:
            print("\nUpdate Overdraft Limit - {self.name}\nOverdraft unavailable".format(self=self))
        # if overdraft available, updates overdraft limit with newLimit
        else:
            print("\nUpdate Overdraft Limit - {self.name}".format(self=self))
            print("Updated from £{self.overdraftLimit:.2f}".format(self=self), end = " ")
            self.overdraftLimit = newLimit
            print("to £{self.overdraftLimit:.2f}".format(self=self))


    def getAvailableBalance(self):
        """Returns the total balance that is available in the account as a float, including any remaining overdraft amount
        
        Returns:
            availableBalance (float): total available balance of the account including any overdraft in pounds (GBP), must be a positive value
        """

        # calculates the available balance as the sum of the account balance and the overdraft limit
        availableBalance = self.balance + self.overdraftLimit
        return availableBalance


    def printBalance(self):
        """Prints to screen the balance of the account and, if an overdraft is available, the remaining overdraft and overdraft limit"""

        print("\nBalance - {self.name}".format(self=self))
        print("Account balance: £{self.balance:.2f}".format(self=self))
        
        # if overdraft is available, also prints overdraft details
        if self.overdraft == True:
            availableBalance = self.getAvailableBalance()
            print("Remaining overdraft: £{0:.2f}\nOverdraft limit: £{1:.2f}".format(availableBalance, self.overdraftLimit))


    def closeAccount(self):
        """Closes customer's account by withdrawing total balance from the account and returning true (note: instance is not actually deleted). If account is overdrawn, account not closed.
        
        Returns:
            boolean: true if account has been closed and balance is 0, false if account not closed due to overdrawn account balance
        """
        
        print("\nClosing {self.name}'s account...".format(self=self))
        
        # if account balance is >= 0, account can be closed
        if self.balance >= 0:
            # withdraws remaining account balance
            self.withdraw(self.balance)
            print("Account closed.")
            return True
        
        # if account balance is < 0, account is overdrawn and cannot be closed
        else:
            # calculates the amount that the account is overdrawn by substracting the negative balance from 0
            amountOverdrawn = 0 - self.balance
            print("Cannot close account due to customer being overdrawn by £{0:.2f}".format(amountOverdrawn))
            return False

def main():
    # EXAMPLE INSTANCES
    print("this has been run in the source file")
    c1 = BasicAccount("Ringo Starr", 90)
    c2 = PremiumAccount("John Lennon", 2000.039, 500.00)

if __name__ == "__main__":
    main()