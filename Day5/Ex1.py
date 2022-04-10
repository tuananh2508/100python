# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_sum=0
total_students=0
for heights in student_heights:
    height_sum+=heights
    total_students+=1
res=round(height_sum/total_students)

print(res)