from User import *
class Bank :
    default_id = 5500
    def __init__(self) -> None:
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = False
        self.initial_deposite = 0
        self.user_id = 0

    def create_an_account(self , name , nid , initial_deposite , password) :
        self.user_id = self.default_id + 1
        user = User(name , initial_deposite , self.user_id, password)
        Bank.default_id +=1
        self.total_balance += initial_deposite
        self.users.append(user)
        self.password = password
        return user
        # print(f'account create successfull !!! \nremaind id : {self.user_id} password : {self.password}')
           
    def print_id(self) :
        print(self.id)

    def update_total_balance(self , amount) :
        self.total_balance += amount

    def check_bank_total_balance(self) :
        return self.total_balance
    
    def check_bank_total_loan_amount(self) :
        return self.total_loan_amount
    #if false and call this method , it set true
    def toggle_loan_feature(self) :
        self.loan_feature = not self.loan_feature

    def provide_loan(self, user):
        if not self.loan_feature:
            print('The loan feature is currently off')
            return False

        loan_amount = user.balance * 2
        # print(f'{user.balance} and {loan_amount}')
        self.loan_amount = loan_amount
        if loan_amount > self.total_balance:
            print('Insufficient bank funds')
            return False

        self.total_balance -= loan_amount
        self.total_loan_amount += loan_amount
        user.balance += loan_amount
        user.transaction_history.append(f'Loan taken: {loan_amount}')
        return True
    def loan_amount(self) :
        return self.loan_amount
    

