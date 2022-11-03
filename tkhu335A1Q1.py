"""
Name: Khuth Taiyo
Username: tkhu335
StudentID: 929289904

Calculate Incomes after deduction of KiwiSaver
"""
import math
prompt1 = input("Please enter your name: ")
name_length = len(prompt1)
prompt2 = int(input(prompt1+", please enter you yearly salary: "))
prompt3 = int(input("Please enter your KiwiSaver percentage: "))
fortnight_year = 26
before_deduction = round(prompt2/fortnight_year, 2)
kiwi_deduction = round((before_deduction*prompt3)/100, 2)
after_deduction = round(before_deduction - kiwi_deduction, 2)
income_after_kiwi = round(after_deduction/80, 2)
                     
print (prompt1+"'s Fortnightly Pay")             
print ("="*(18+name_length))
print ("Fortnightly pay before deducting Kiwisaver: $"+str(before_deduction))
print ("Fortnightly KiwiSaver deduction: $"+str(kiwi_deduction))
print ("Fortnightly pay after Kiwisaver deduction is $"+str(after_deduction))
print ("Income per hour after Kiwisaver deduction is $"+str(income_after_kiwi))              
