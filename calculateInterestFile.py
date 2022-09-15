from calculateInterestPackage import simpleInterest, compoundInterest

print("==== Calculate Simple and Compound Interests ====")
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter number of years: "))
print("Simple Interest: ", simpleInterest(p, r, t))
print("Compound Interest: ", compoundInterest(p, r, t))
