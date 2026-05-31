def employee_info (name , age , department  , salary = 50000 ):
    data = "Name: " + name + ", Age: " + str(age) + ", Department: " + department + ", Salary: " + str(salary)
    return data
info = employee_info("Rishabh ", 30, "IT")
info1 = employee_info("Alice ", 25, "HR")   

print(info)
print(info1)


def student_grade (name , grade = "E"):
    return "Student: "+name + ", Grade: " + grade
student = student_grade("Bob")
student1 = student_grade("Alice", "A")
print(student)
print(student1)
