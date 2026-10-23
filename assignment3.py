#Take input in celsius and equivalent in farenheit and kelvin 
#Farenheit = (celsius *9/5) + 32)
#Kelvin =  celsius + 273.15

Celsius = int(input("Enter the tempreature in celsius:"))
Farenheit = ((Celsius*9/5)+32)
Kelvin = (Celsius+273.15)
print("The temp of farenheit is:", Farenheit)
print("The temp of kelvin is:", Kelvin)
print("data type is:", type(Kelvin))

##Bill split calculator 
#Write a program that take total bill amount and number of friends as input and calculate how much each friend has to pay 

Total_bill = int(input("Enter total bill amount:"))
No_of_friends = int(input("Enter no of friends:"))
amount_per_friend = float(Total_bill/No_of_friends)
print("Each friend has to pay:", amount_per_friend)
print("Data type of amount_per_friend is:", type(amount_per_friend))

#application/output based 

x=5
y=2.0
print(x//y)
print(x**y)

#Identity and correct the error
sum=10
print(sum)




