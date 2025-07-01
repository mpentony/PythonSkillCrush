print("Which two numbers do you want to add together?")

user_input1 = input("Input your first number: ")
user_input2 = input("Input your second number: ")
is_good = True

try:
    float(user_input1)
except:
    print("Your first number needs to be an integer!")
    is_good = False
try:
    float(user_input2)
except:
    print("Your second number needs to be an integer!")
    is_good = False

if (is_good):
   sum = float(user_input1) + float(user_input2)    
   print("Your sum is :", sum)
else:
   print ()
   print("Your numnbers are not valid.  Please check your inputs and try again.")

