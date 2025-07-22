# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior
# Your code here:

age = int(input("Enter how old are you ? :"))

if age<=12:
    print("Your are :Child")

elif age>=13 and age<=19:
    print("Your are :Teenager")

elif age>=20 and age<=59:
    print("Your are :Adult")

elif age>=60:
    print("Your are :Senior")    

else : 
    print("Invaild")    