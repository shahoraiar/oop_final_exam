# from Bank import *
class User :
    def __init__(self , name , inital_depostie,user_id , password) -> None:
        self.name = name
        self.password = password
        self.user_id = user_id
        self.balance = inital_depostie
        self.transaction_history = []

    def deposit(self , amount , bank) :
        self.balance += amount
        self.transaction_history.append(f'deposite : {amount}')
        bank.update_total_balance(amount)

    def withdraw(self , amount, password , bank) :
        if password != self.password :
            print(f'{self.name} !! password is invalid')
            return False
        
        if self.balance >= amount :
            self.balance -= amount
            self.transaction_history.append(f'withdrawn : {amount}')
            bank.update_total_balance(-amount)
            print(f'{self.name} !! successfull withdraw/transfer : {amount}')
            return True
        
        else :
            print('insufficient balance !')
            return False
        
    def transfer(self , recipient , amount , password , bank) :
        if self.withdraw(amount , password , bank) :
            recipient.deposit(amount , bank)
            self.transaction_history.append(f'tranferred : {amount}')
            return True
        else :
            return False
        
    def  view_transaction_history(self) :
        return self.transaction_history
    
    def take_loan(self , bank) :
        # print('hi')
        if bank.provide_loan(self) :
            # loan_amount = self.balance * 2
            print(f'{self.name} !! successful got loan : {bank.loan_amount}')
            # self.transaction_history.append(f'loan taken : {loan_amount - self.balance}')

    def check_balance(self) :
        return self.balance

    def __repr__(self) -> str:
        print('------users all details-----')
        return f'name : {self.name} \nuser_id : {self.user_id} \npassword : {self.password} \ntotal balance : {self.balance}'



