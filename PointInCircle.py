"""aaa"""
 
 
def is_odd():
    """fff"""
    x_cir = float(input())
    y_cir = float(input())
    radius = float(input())
    x_point = float(input())
    y_point = float(input())
 
    distance = ((x_cir - x_point)**2 + (y_cir - y_point)**2)**0.5
    if distance <= radius:
        print("True")
    else:
        print("False")
 
 
is_odd()