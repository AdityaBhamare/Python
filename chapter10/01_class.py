class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000

Aadi = Employee()
Aadi.name = "Aadi Bhamare" # This is a class attribute
print(Aadi.name, Aadi.language, Aadi.salary)

rohan = Employee()
rohan.name = "Rohan Zenin"
print(rohan.name ,rohan.salary, rohan.language)

# Here name is object attribute and salary and language
# are class attribute as they directly belong to the class