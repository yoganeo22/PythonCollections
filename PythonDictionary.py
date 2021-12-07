import os

dictionary = {
    "employees": [{"name": "Rickaard", "age":28, "income":3750}
                ,{"name": "Meyer", "age":33, "income":5080}
                ,{"name": "Nelson", "age":29, "income":4980}
                ,{"name": "Billy", "age":28, "income":4980}
                ,{"name": "Costa", "age":40, "income":9000}
                ,{"name": "Daniel", "age":27, "income":7200}
                ,{"name": "Faustin", "age":39, "income":7890}],
    "students": [{"name": "Rickaard", "age":16, "major":"Medical"}
                ,{"name": "Meyer", "age":18, "major":"Engineering"}
                ,{"name": "Nelson", "age":18, "major":"Engineering"}
                ,{"name": "Billy", "age":17, "major":"Engineering"}
                ,{"name": "Costa", "age":20, "major":"Medical"}
                ,{"name": "Daniel", "age":17, "major":"Engineering"}
                ,{"name": "Faustin", "age":17, "major":"Medical"}]
}

if __name__ == "__main__":
    print("Starting...")

    # Accessing the key:value pair of the dictionary
    #print("Data: {}".format(dictionary["employees"][0]["name"]))

    # -------------------------------------------------------------------------- #
    # Get the average age of employees? #

    # Get total employees and total students
    TotalEmployees = len(dictionary["employees"])
    TotalStudents = len(dictionary["students"])
    print("Total Employees: {} | Total Students: {}".format(TotalEmployees, TotalStudents))
    # print out: Total Employees: 7 | Total Students: 7

    # loop and add-up the employees age.
    TotalEmpAges = 0
    for x, element in enumerate (dictionary["employees"]):
        #print("x: {} | {}".format(x, element))
        TotalEmpAges += int(dictionary["employees"][x]["age"])

    # Get employees' average age
    EmpAveAge = TotalEmpAges/TotalEmployees
    print("[1] Total Employees Age: {} | Average Employees Age {}".format(TotalEmpAges, EmpAveAge))
    # print out: [1] Total Employees Age: 224 | Average Employees Age 32.0

    # -------------------------------------------------------------------------- #
    # The average income of employees greater than average age?

    TotalEmpAboveAveAge = 0 # total number of employees with income greater than average age
    TotalIncAboveAveAge = 0 # total income for employees with income greater than average age
    SpecialAgeAveIncome = 0 # Average income for employees with age greater than average age

    # loop and get total employee above ave age and total income above ave age
    for x, element in enumerate(dictionary["employees"]):
        if dictionary["employees"][x]["age"] > EmpAveAge:
            TotalEmpAboveAveAge += 1
            TotalIncAboveAveAge += dictionary["employees"][x]["income"]

    print("TotalEmpAboveAveAge: {} | TotalIncAboveAveAge: {}".format(TotalEmpAboveAveAge, TotalIncAboveAveAge))
    # print out : TotalEmpAboveAveAge: 3 | TotalIncAboveAveAge: 21970

    SpecialAgeAveIncome = TotalIncAboveAveAge/TotalEmpAboveAveAge
    print("[2] SpecialAgeAveIncome: {}".format(SpecialAgeAveIncome))
    # print out: [2] SpecialAgeAveIncome: 7323.333333333333

    # -------------------------------------------------------------------------- #
    # Which major is being studied by most student?
    MajorA_StudentCount = 0
    MajorB_StudentCount = 0
    for x, element in enumerate(dictionary["students"]):
        #print(x, element["major"])
        if element["major"] == "Medical":
            MajorA_StudentCount += 1
        elif element["major"] == "Engineering":
            MajorB_StudentCount += 1

    if MajorA_StudentCount > MajorB_StudentCount:
        print("[3] There is more students majoring in Medical")
    else:
        print("[3] There is more students majoring in Engineering")
    # print out : [3] There is more students majoring in Engineering




