days = int(input('How many days left till your birthday: '))
week = int(0 if days < 7 else days / 7)
leftOverDays = days if days < 7 else days % 7

myList = []


print(f" {week} weeks and {leftOverDays} days left")
