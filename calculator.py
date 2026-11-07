
# def add(a,b):
#    return a+b
# def subtrac(a,b):
#    return a-b
# def multipy(a,b):
#    return a*b
# def divide(a,b):
#    if b == 0:
#       return "Cannot divide by zero"
#    return a/b
# while True:
#    print("/n====================================")
#    print("             CALCULATOR               ")
#    print("======================================")
#    print("1.Addition")
#    print("2.Subtrction")
#    print("3.Multiplication")
#    print("4.Division")
#    print("5.Exit")
#    choice  = input("Enter yourchoice")
#    if choice == "5":
#       print("Thank you for using calculator")
#       break
#    if choice in ["1", "2", "3", "4"]:
#        num1 = float(input("Enter first number: "))
#        num2 = float(input("Enter second number: "))
#        if choice == "1":
#           print("result", add(num1,num2))
#        elif choice == "2":
#           print("result", subtrac(num1,num2))
#        elif choice == "3":
#           print("result", multipy(num1,num2))
#        elif choice == "4":
#           if num2 == 0:
#             print(" Zero can't divide")
#           else:
#             print("result", divide(num1,num2))  
#        else:
#           print("invlade Numaber")     
    
      
   
def add(a,b):
   return a + b
def subtrac(a,b):
   return a - b
def multipy(a,b):
   return a * b
def divide(a,b):
   if b == 0:
      return "Cannot divide by zero"
   return a / b
while True:
   print("/n====================================")
   print("             CALCULATOR               ")
   print("======================================")
   print("1.Addition")
   print("2.Subtrction")
   print("3.Multiplication")
   print("4.Division")
   print("5.Exit")
   choise = input("Enter your Choice: ")
   if choise == "5":
      print("Thanks for useing calaulator")
      break
   if choise in ["1", "2", "3", "4"]:
      num1 = float(input("Enter your 1st Number:  "))
      num2 = float(input("Enter your 2nd Number:  "))
      if choise == "1":
         print("Result:", add(num1,num2))
      elif choise == "2":
         print("Result:", subtrac(num1,num2))
      elif choise == "3":
         print("Result:", multipy(num1,num2))
      elif choise == "4":
         print("Result:",divide(num1,num2))
      else:
         print("wrong choice")   
