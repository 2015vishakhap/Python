import ATM_dfunction_code as f
print ("Welcome")

user_data=f.initial()

if (f.verify_information(user_data)):

     f.choose_number(user_data)
     if f.choose_number == '1':
        f.receipt(user_data)

else:
    print ("your password or username is incorrect.Please enter it again")


