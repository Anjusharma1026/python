title = input("Enter The Book Title :")
author = input("Enter The Book Author :")
price = input("Enter The Book Price :")
quantity = input("Enter The Stock Quantity :")
purchase = input("Enter The Purchase Quantity  :")


print("Book Details:")
print("Title:"+title)
print("Author: "+author)
print("Price: "+price)
print("Stock: "+quantity)

if(purchase<=quantity):
      print("The Book "+title+ "is in stock")
else:
      print("The Book is Out Of Stock")
 