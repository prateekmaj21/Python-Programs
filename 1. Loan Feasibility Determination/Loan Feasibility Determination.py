#Loan Feasibility Determination
#Check if paying back a certain loan is possible
#Based on loan interest rate and monthly payments the user wants to make

def get_loan_info():
    
    #Getting the basic information about the loan
    loan={}
    
    #User input
    #These are important inputs we have to take
    #Interest to be calculated as simple interest
    loan['principal'] = float(input("Enter the loan amount you have taken: "))
    loan['rate'] = float(input("Enter the loan interest rate: "))/100
    loan['monthly payment'] = float(input("Enter the monthly payment amount you want to pay monthly: "))
    loan['money paid'] = 0
    
    return loan

def show_loan_info(loan, number):
    
    #To show about the current loan status
    print("\n-----Loan Status-----")
    print("\n----Loan information after " + str(number) + " months----")
    for key, value in loan.items():
        print(key.title() + ": " + str(value))
        
def collect_interest(loan):
    #Update loan accorfing to the interest rate
    #Dividing the value by 12, as monthly calculations to be done
    loan['principal'] = loan['principal'] + loan['principal']*loan['rate']/12
    
def make_monthly_payment(loan):
    #The monthly payment to be made by the user
    loan['principal'] = loan['principal'] - loan['monthly payment']
    
    if loan['principal'] > 0:
        loan['money paid'] += loan['monthly payment']
        
    else:
        #If loan principle is negative
        loan['money paid'] += loan['monthly payment'] + loan['principal']
        loan['principal'] = 0
        
def summarize_loan(loan, number, initial_principal):
    #Displaying the loan results
    #Printing the information
    print("\nCongraulations! You can pay your loan in= " + str(number) + "months!")
    print("Your initial loan amount was= " + str(initial_principal) + " at a rate of "+ str(100*loan['rate']) + "%.")
    print("Your monthly payment was= " + str(loan['monthly payment']) + ".")
    print("You spent amount= " + str(round(loan['money paid'], 2)) + " in total.")
    
    #Calculate money spent on interest
    
    interest = round(loan['money paid'] - initial_principal, 2)
    print("You spent= " + str(interest) + " on interest!")
    
    

        
        
#The main code

print("---Loan Feasibility Determination---\n")

#Initialize variables

month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

#Display starting conditions of loan
show_loan_info(my_loan, month_number)
input("---Press 'Enter' to begin.---")

#Simulate paying off the loan as long as the loan's principal > 0

while my_loan['principal'] > 0:
    
#You cannot get ahead of the interest, you will never pay off the loan so break

    if my_loan['principal'] > starting_principal:
    
        break

    #It is possible to pay off the loan, so simulate a single month
    #Increment month number, collect interest, make a payment, add data to plot, and show loan info
    
    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)
    
    #The loan is either paid off in full or it can NEVER be paid off
    #The loan was paid off in full
    if my_loan['principal'] <= 0:
        summarize_loan(my_loan, month_number, starting_principal)
        
        #The loan can NEVER be paid off, can't get ahead of interest
        
    else:
        print("\nYou will NEVER pay off your. Interest value will keep on rising.")
        print("You cannot get ahead of the interest.")

    
    
 
    
        
        
        
    

    