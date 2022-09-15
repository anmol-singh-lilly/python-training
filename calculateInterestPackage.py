# Package to find simple and compound interest

def simpleInterest(p, r, t):
    """
    Function to calculate Simple Interest
    """
    si = (p*r*t)/100
    return si


def compoundInterest(p, r, t):
    """
    Function to calculate Compound Interest
    """
    amount = p * ((1+(r/100)) ** t)
    ci = amount - p
    return ci
