"""docstring"""
 
 
def main():
    """C:  3, 0: Missing function docstring (missing-docstring)"""
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
 
 
def bmi(name, weight, height):
    """dsdsd"""
    beeemi = weight / ((height/100)**2)
    print("%s's  BMI = %.2f" % (name, beeemi))
 
 
main()