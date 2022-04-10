# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tvar = name1.lower().count('t') + name2.lower().count('t')
rvar = name1.lower().count('r') + name2.lower().count('r')
uvar = name1.lower().count('u') + name2.lower().count('u')
evar = name1.lower().count('e') + name2.lower().count('e')
true_var= tvar + rvar + uvar + evar
lvar = name1.lower().count('l') + name2.lower().count('l')
ovar = name1.lower().count('o') + name2.lower().count('o')
vvar = name1.lower().count('v') + name2.lower().count('v')
evar = name1.lower().count('e') + name2.lower().count('e')
love_var= lvar+ovar+vvar+evar

res=true_var*10+love_var


if res <10 or res >90:
    print(f"Your score is {res}, you go together like coke and mentos.")
elif res >= 40 and res <=50:
    print(f"Your score is {res}, you are alright together.")
else:
    print(f"Your score is {res}.")