while True:
  try:
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))

    while True:
      operators = input("enter one of the followings: + ,- ,/ ,*.")
      if operators == "+":
        print(num1 + num2)
        break
      elif operators == "-":
        print(num1 - num2)
        break
      elif operators == "*":
         print(num1 * num2)
         break
      elif operators == "/":
        if num2 != 0:
           print(num1 / num2) 
        else:
          print("cant be divided by zero")
        break
      else:
        print("operators not available")

    again = input("do want to calculate again:(y/n)")
  
    while again.lower() != "y" and again.lower() != "n":
      print("please enter y or n!")
      again = input("do want to calculate again:(y/n)")
      
    if again.lower() == "n":
       print("Goodbye")
       break
      
  except ValueError:
    print("thats not a number!please enter a number")
    continue
