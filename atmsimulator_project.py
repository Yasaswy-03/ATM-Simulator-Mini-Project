print("Welcome to ABC Bank")
All_acc = ["1234 5678 9012", "2463 1384 2745" , "2748 4342 2466" , "3213 1435 2456"]
acc_no = str(input("Enter your Acc_No:"))
Acc_pin = {"1234 5678 9012" : 1234 , "2463 1384 2745" : 5678 , "2748 4342 2466" :7890 , "3213 1435 2456" : 3356}
if(acc_no in All_acc):
  pin_no = int(input("Enter your Pin: "))
  Balance = 10000
  if acc_no != ""  :
    a = "Deposit"
    b = "Withdraw"
    c = "Balance"
    User = str(input("Enter any Deposit | Withdraw | Balance : "))
    match User: 
        
        case "Deposit" :
           print("Thank you for entering Deposit")
           Amount_deposit = int(input("Enter amont :"))
           Balance+=Amount_deposit
           print("Your Balance : " , Balance)
    
    if ( User == a):
       print("Loading Deposit ")
       Amount_deposit = int(input("Enter the amount :"))
       Balance+=Amount_deposit
       print("Balance in account :",Balance) 
       
    elif (User == b):
        print("Loading Withdraw ")   
        Amount_withdraw = int(input("Enter the amount :"))
        if(Amount_withdraw <= Balance):
           Balance-=Amount_withdraw
           print("Balance in account :",Balance)
        else :
            print("Insufficient funds")
            
    elif (User == c):
        print("Balance in account :",Balance)
        
    else :    
        print("Enter any valid option")
        
  else :
    print("Enter valid Acc_Number")    
    
else :
    print("Enter your 12 digit number")