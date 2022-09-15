
def calculateSalary(basic):
    """
    This function calculates the HRA, DA and gross salary from the basic salary
    """
    hra = basic * 0.4
    da = basic * 0.2
    gross = basic + hra + da
    return hra, da, gross


basic = input("Enter basic salary: ")
hra, da, gross = calculateSalary(basic)

print("Basic Salary: ", basic)
print("HRA: ", hra)
print("DA: ", da)
print("Gross Salary: ", gross)
