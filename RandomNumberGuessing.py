import random
hidden=random.randint(1,11)
choice=int(input("Enter your choice: "))
if choice>hidden:
  print("Your guess is above by ",choice-hidden)
else:
  print("Your guess is below by ",hidden-choice)  
print(hidden)  
