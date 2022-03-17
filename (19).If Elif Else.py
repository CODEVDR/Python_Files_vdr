#INCOME TAX
#NET INCOME RANGE                                     RATE OF INTREST
#--------------------------------------------------------------------
#UPTO 60000                                            NILL
#ABOVE 60000 AND LESS THAN 100000                      10% OF THE AMOUNT WHICH THE TOTAL INCOME EXCEEDS RS 60000
#ABOVE RS 100000 AND LESS THAN 150000                  20% OF THE AMOUNT WHICH THE TOTAL INCOME EXCEEDS RS 100000
#ABOVE 150000                                          30% OF THE AMOUNT WHICH THE TOTAL INCOME EXCEEDS RS 150000
#n=int(input("Enter your monthly income in ₹:"))
#if n>=1 and n<=60000:
#    print("You don't have to pay any tax")
#elif n>=60001 and n<=100000:
#    tax=n-60000*10/100
#    print("Out of ₹",n,"You have to pay ₹",tax,"to Government")
#elif n>=100001 and n<=150000:
#    tax=((n-60000)*10/100)+((n-100000)*20/100)
#    print("Out of ₹",n,"You have to pay ₹",tax,"to Government")
#elif n>=150001:
#    tax=((n-60000)*10/100)+((n-100000)*20/100)+((n-150000)*30/100)
#    print("Out of ₹",n,"You have to pay ₹",tax,"to Government")
#=======================================================================
#ELECTRIC BILL
#------------------------------------------------------------------------
#UNITS CONSUMED                            CHARGES
#---------------------------------------------------
#UPTO 100 UNITS                             2.50
#100 AND UPTO 200 UNITS                     3.50
#200 UNITS                                  5.00
#+50 for every consumer
#n=int(input("Enter Units Consumed:"))
#if n>=1 and n<=100:
#    print("Your electricity bill price:₹",(n*2.50)+50)
#elif n>=101 and n<=200:
#    print("Your Electricity bill price:₹",(n*3.50)+50)
#else:
#    print("Your electricity bill price:₹",(n*5.00)+50)
#========================================================================
