age = int(input("Enter Your age: "))
print("Your age is:", age)

is_student = input("Are you a student? (yes/no): ").strip().lower()
print("Student Status:", is_student)

if age <= 12:
    ticket_price = 200

elif age >= 65:
    ticket_price = 300

elif age >= 13 and age <= 64 and is_student == "yes":
    ticket_price = 400

else:
    ticket_price = 600

print("Your ticket price is: Rs.", ticket_price)

marks = int(input("Enter your marks (0-100): "))
print("Your marks are : ",marks)

if marks >=90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Grade F")

if age < 0:
    print("Invalid age")