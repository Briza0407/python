# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

n1 = t+r+u+e
n2 = l+o+v+e

total = n1*10+n2

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}.")
