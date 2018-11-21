
def initial():
    with open("data.txt","r")as file:
        user_data = file.readlines()
        for item in user_data:
            user_data[user_data.index(item)]=item.replace("\n",' ')
        return user_data

def choose_number(user_data):
    number = raw_input("\n1.Withdraw \t2.Change pin \t3.Balance inquiry \t4.Exit\n")
    if number=='1':
        Withdraw(user_data)
    elif number=='2':
        Change_pin(user_data)
    elif number=='3':
        Balance_inquiry(user_data)
    else:
        print"enter correct choice"

def writefile(user_data):
    with open("data.txt","w")as file:
        for item in user_data:
            file.write(str(item)+"\n")

def verify_information(user_data):
    username=raw_input("enter valied user name")
    password=raw_input("enter valied password")
    if username==user_data[0]and password==user_data[1]:
        return True
    else:
        return "enter valied username and password"

def Withdraw(user_data):
    amount= int(raw_input("enter a amount you want"))
    if amount < user_data[2]:
        user_data[2] = int(user_data[2])- amount
        print "Transaction is complite.Your current balance is Rs: "+str(user_data[2])
        writefile(user_data)
    else:
        print "you do not have sufficient amount"

def Change_pin(user_data):
    cpassword=raw_input("enter current password")
    if cpassword == user_data[1]:
        user_data[1]=raw_input("enter new password: ")
        writefile(user_data)
    else:
        print "wrong password"

def  Balance_inquiry(user_data):
    print "your balance is "+str(user_data[2])
