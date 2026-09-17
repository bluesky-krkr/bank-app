class BankAccount:
    def __init__(self,name,balance,acc_no):
        self.name=name

        self.balance=balance
        self.acc_no=acc_no

    def check_bal(self):
        print(f'Remaining balance of the account holder {self.name} is {self.balance}')


    def add_money(self):
        try:
            cash=int(input('Enter the amount you want to deposit:'))
        except ValueError:
            print('invalid input')
            return
        if  cash<0 :
            print('Amount should not be negative')
        elif cash==0:
            print('Amount can not be zero')
        else:
            self.balance+=cash
            print(f'Amount has been succesfully transfered and the balance is {self.balance}')
            
    def withdrawal(self):
        try:
            with_amount=int(input('Enter the amount you want to withdrawal: '))
        except ValueError:
            print('invalid input')
            return
        if with_amount<0:
            print('Amount should not be negative')
        elif with_amount==0:
            print('Amount cannot be zero')
        elif with_amount>self.balance:
            print(f'Insuffient balance,Remaining balance {self.balance}')
        else:
            self.balance-=with_amount
            print(f'Amount has been succesfully withdrawn from your bank accout the current balance is {self.balance}')

accounts={}
next_acc_no=1
def create_account():
    global next_acc_no
    name=input('Enter your name:')
    try:
        balance=int(input('Enter your initail deposit: '))
    except ValueError:
        print('Invalid input try again')
    acc=BankAccount(name,balance,next_acc_no)
    accounts[next_acc_no]=acc
    print(f'Account created!,Your account number is {next_acc_no} with the user name of {name}')
    next_acc_no+=1
    return acc

def login():
    while True:
        try:
            acc_no=int(input('Enter your account number: '))
        except ValueError:
            print('Invalid input try again')
        if acc_no in accounts:
            return accounts[acc_no]
        print('Details not found')

print('----XYZ BANKING SERVICES----')
current_acc=create_account() if input('New user?(yes=Y,no=N):').lower()=='y' else login()
if current_acc:
    while True:
        try:
            service=int(input('--------\nChoose from the below services we provide\n1-Check balance\n2-Deposit\n3-Withdrawal\n4-Exit\n----------\n'))
        except ValueError:
            print('Invalid input')
        if service==1:
            current_acc.check_bal()
        elif service==2:
            current_acc.add_money()
        elif service==3:
            current_acc.withdrawal()
        elif service==4:
            print('Thanks for choosing us')
            break
