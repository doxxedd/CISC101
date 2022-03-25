###############################################################
pay_rate = float(input('What is your hourly pay rate?'))
print(pay_rate)

###############################################################
k = int(input())
d = float(input())
s = input()

###############################################################
print('One', 'Two', 'Three', sep='*')

###############################################################
print('One', end='')
print('Two')

###############################################################
print('One\nTwo\nThree')

###############################################################
print(format(12345.6789, '.2f'))
print(format(12345.6789, '.2e'))
###############################################################
month = int(input('Enter month (numeric):'))
day = int(input('Enter day:'))
year = int(input('Enter two digit year:'))
monthTimesDay = day * month

if year == monthTimesDay:
    print("This date is magic!")
else:
    print("This date is not magic.")

###############################################################
tuition = 8000

for i in range(1, 6):
    tuition *= 1.03

    if i == 1:
        print("In 1 year, the tuition will be $" + str(tuition) + ".")
    else:
        print("In " + str(i) + " years, the tuition will be $" + str(tuition) + ".")

############################################################### 
