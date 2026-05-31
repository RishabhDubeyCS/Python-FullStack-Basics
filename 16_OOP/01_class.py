#Class : Class i a blueprint or a template . eg  Form for an Exam that contain name , age , electives , father name etc
# object : Specific instance created from the template (class) eg form which contain the data for john doe


class Employee:
    company = "Stream Talk"
    def get_salary(self): #self is importand here because self is a way to refernce the object of the class which is being created 
        return 35000
    

e = Employee()#An object of class Employee is created here
print(e.get_salary()) #Employee es get salary method is called 
print(e.company)
e2 = Employee()
print(e2.get_salary())
print(e2.company)



