principle = int(input("Enter the principle"))
rate = int(input("Enter the rate"))
years = int(input("Enter the years"))

amount = (principle*rate*years)/100
monthlyAmount= amount/12
print("Monthly Amount: ",monthlyAmount)