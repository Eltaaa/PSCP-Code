"""aaa"""
 
 
def is_odd():
    """fff"""
    xxx = float(input())
    yyy = float(input())
 
    if xxx > 0 and yyy > 0:
        print("Q1")
    elif xxx < 0  and yyy > 0:
        print("Q2")
    elif xxx < 0 and yyy < 0:
        print("Q3")
    elif xxx > 0 and yyy < 0:
        print("Q4")
    elif yyy == 0 and xxx != 0:
        print("X")
    elif xxx == 0 and yyy != 0:
        print("Y")
    else:
        print("O")
 
 
is_odd()