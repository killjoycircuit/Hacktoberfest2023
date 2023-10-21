#Volume Calcualor
name=input("Enter the name of shape ")
print("You entered",name)
if name =='cube':
    l=float(input("Enter edge length "))
    print("The volume is ",l*l*l)


elif name =='cuboid':
    l = float(input("Enter length "))
    b = float(input("Enter breadth "))
    h = float(input("Enter height "))
    print("The volume is",l*b*h )

elif name =='sphere':
    r = float(input("Enter radius "))
    print("The volume is", r*r*r)

elif name =='cylinder':
    r = float(input("Enter radius "))
    h = float(input("Enter height "))
    print("The volume is", 3.14*r*r*h)

elif name =='cone':
    r = float(input("Enter radius "))
    h = float(input("Enter height "))
    print("The volume is", 0.33*3.14*r*r*h)

elif name =='rectangular prism':
    l = float(input("Enter length "))
    b = float(input("Enter breadth\width "))
    h = float(input("Enter height "))
    print("The volume is", l * b * h)

else:
    print("Error invalid choice")
