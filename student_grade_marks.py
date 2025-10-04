student1=int(input("enter the marks of student1:"))
student2=int(input("enter the marks of student2:"))
student3=int(input("enter the marks of student3:"))

average_marks=(student1+student2+student3)/3

if average_marks>=90:
    print("A GRADE")
elif average_marks>=75 and average_marks<=89:
    print("B GRADE")
elif average_marks>=60 and average_marks<=74:
    print("C GRADE")
else:
    print("D GRADE")
    