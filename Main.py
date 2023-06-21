from User import User
from Bank import Bank

def main():
    ibbl_bank = Bank()

    user1 = ibbl_bank.create_an_account('rahim' , 232424 , 2000 , 2222)
    user1.deposit(1000 , ibbl_bank) 
    # user1.check_balance()

    user2 = ibbl_bank.create_an_account('karim' , 898939, 8000, 2222)
    user2.withdraw(500 , 44 , ibbl_bank)
    user2.withdraw(1000 , 2222 , ibbl_bank)
    user2.transfer(user1 , 1000 , 2222 , ibbl_bank)
    print(f'bank total balance : {ibbl_bank.check_bank_total_balance()} ')
    # print(f'after transfer user1 balance : {user1.check_balance()}')

    ibbl_bank.toggle_loan_feature() 
    print(f'user1 balance before loan : {user1.check_balance()}')
    user1.take_loan(ibbl_bank) 
    # user2.take_loan(ibbl_bank)
    # user1.transaction_history()

    print(f'bank total balance : {ibbl_bank.check_bank_total_balance()} ')
    print(f'bank total loan balance : {ibbl_bank.total_loan_amount}')
    user2.check_balance()
    user1.check_balance()

    print(user1.view_transaction_history())

if __name__ == '__main__':
    main()
