# #write a python function that takes one argument as a list a=[2,4,6,8] and remove the second last item from that list and returns the whole list without the removed item

a=[2,4,6,8]
def list(a):
  a.pop(2)
  print(a)
list([2,4,6,8])

# # #write a python program that has list days =["Monday","Tuesday","Friday","Monday"] and cunts the number of occurences of Monday

# # #write  a python function named smallest that accepts a list of unsorted intrgers and return the smallest number in the list a.smallest ([36,8,2,4,1,5,7]) returns 1
smallest=[3,6,7,4,5,9,1]
def numbers (smallest):
    smallest.sort()
    print(smallest(min))
numbers(56)


# #write a function named divisible_by_seven that using the range functionand a for loop returns a list containing all the numbers between (100,200) that are divisible by seven
def divisible_by_seven():
  for x in range (100,200):
    if x%7==0:
      print(x)
divisible_by_seven()
    # else:
    #   print("not divisble")

# #write a python program that takes two inputs(as intergers)
# #from a user and adds the 2 numbers,checks if the sum is greater than 10,less than 10 or equal 10 and prints a statement after each check
num1=(input("Enter a number"))
num2=(input("Enter a number"))
sum=num1+num2

if (sum>10):
    print ("sum is greater than 10")
elif (sum ==10):
  print("sum is equal to 10")


# #write a function that takes one argument which is a list ,a[1,2,3,4,,5] and rturns true if 4 is [present] in the list and false if 4 is not in the list
  a=[1,2,3,4,5,6]
  def list(a):
    if 4 in a:
      return True
    else:
      return False

# #write a function that takes one argument which is a lsit fruit=["apples","grapes","pineapple"] and removes the last fruit from the list then returns the list without the removed fruit
  

  def fruits(matunda):
    matunda.pop()
    print(matunda)
  fruits(["maembe","ndizi","mananasi","tikiti","machungwa"])

# #write a python program that takes in a list of cars cars=["ford","bmw","volvo"] and returns a sorted list
cars =["ford","bmw","volvo"]
cars.sort()
print(cars)