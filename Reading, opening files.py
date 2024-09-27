# from employees.txt read thorugh every lline with for loop
"""
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():

    print(employee)

employee_file.close()
"""
#writing and appending to files

employee_file = open("example.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()

#You can create different format files
