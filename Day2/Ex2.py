# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
hfloat=float(height)
wfloat=float(weight)

result = int(wfloat/(pow(hfloat,2)))

print(result)